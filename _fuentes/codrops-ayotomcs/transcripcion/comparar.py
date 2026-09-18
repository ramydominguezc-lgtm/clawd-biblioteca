# Comparativa demo vs replica: IoU de silueta (mejor alineacion entera) + imagen lado a lado.
import glob, io, json, re, sys
import numpy as np, cairosvg
from PIL import Image, ImageDraw
sys.path.insert(0, 'C:/Users/alfav/OneDrive/Desktop/Animaciones - Clawd/scripts')
from animar_pixel import pintar
U = 16 / 3
PX = 8          # px por celda en la comparacion
B = 'C:/Users/alfav/OneDrive/Desktop/Clawd - Biblioteca/'
FONDO = (250, 249, 245)


def fuente(svg, x0, y0, w, h):
    interior = re.sub(r'^<svg[^>]*>|</svg>\s*$', '', svg.strip())
    d = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {w*U} {h*U}" width="{w*PX}" '
         f'height="{h*PX}" shape-rendering="crispEdges">{interior}</svg>')
    return np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=d.encode()))).convert('RGBA'))


def mejor_iou(a, b):
    ma, mb = a[..., 3] > 128, b[..., 3] > 128
    H = max(ma.shape[0], mb.shape[0]) + 80; W = max(ma.shape[1], mb.shape[1]) + 80
    A = np.zeros((H, W), bool); A[40:40 + ma.shape[0], 40:40 + ma.shape[1]] = ma
    # alinear por esquina de la caja y buscar +-1 celda alrededor
    ya, xa = np.where(A); yb, xb = np.where(mb)
    best = 0
    for dy in range(-PX, PX + 1, 2):
        for dx in range(-PX, PX + 1, 2):
            Bm = np.zeros((H, W), bool)
            oy = ya.min() - yb.min() + dy; ox = xa.min() - xb.min() + dx
            ys, xs = yb + oy, xb + ox
            ok = (ys >= 0) & (ys < H) & (xs >= 0) & (xs < W)
            Bm[ys[ok], xs[ok]] = True
            v = (A & Bm).sum() / (A | Bm).sum()
            best = max(best, v)
    return best


def plano(im):
    base = Image.new('RGBA', im.size, (*FONDO, 255)); base.alpha_composite(im); return base


def hoja(nombre, pares, ancho_tile):
    tiles = [(plano(Image.fromarray(a.astype('uint8'))), plano(b)) for a, b in pares]
    w, h = tiles[0][0].size
    esc = ancho_tile / w
    tw, th = int(w * esc), int(h * esc)
    sh = Image.new('RGB', (tw * len(tiles), th * 2 + 36), (255, 255, 255))
    dr = ImageDraw.Draw(sh)
    for i, (a, b) in enumerate(tiles):
        sh.paste(a.resize((tw, th), Image.NEAREST), (i * tw, 16))
        sh.paste(b.resize((tw, th), Image.NEAREST).convert('RGBA'), (i * tw, th + 34))
    dr.text((4, 2), 'arriba: demo original (GSAP real)', fill='black')
    dr.text((4, th + 20), 'abajo: replica con la skill', fill='black')
    sh.save(B + nombre)


def ajustar_lienzo(ours, w, h):
    """El cuadro nuestro puede ser de otro tamano; se pega en un lienzo del tamano de la fuente."""
    im = Image.new('RGBA', (w * PX, h * PX), (0, 0, 0, 0))
    im.paste(ours, (0, 0))
    return im


que = sys.argv[1]
if que == 'pesas':
    import clawd_pesas as R
    fs = sorted(glob.glob('cap_gym/t*.svg'))
    x0, y0, W, H = 36 - 8 * U, 128 - 28 * U, 34, 28
    poses, sec = R.cuadros()
    idx = list(range(len(fs)))
    frames = [poses[k] for k, _ in sec]
    muestra = [0, 3, 5, 6, 8, 12, 15, 18, 21, 24, 30, 36, 40, 44, 47]
elif que == 'bandera':
    import clawd_bandera as R
    fs = sorted(glob.glob('cap_flag/t*.svg'))
    d = json.load(open('flag_piezas.json'))
    x0, y0, W, H = d['x0'], d['y0'], 32, 29
    movs = R.SUBIDA + R.BUCLE + R.BUCLE
    frames = [R.cuadro(*m) for m in movs]
    muestra = list(range(12))
elif que == 'paseo':
    import clawd_paseo as R
    fs = sorted(glob.glob('cap_walk/t*.svg'))[:288]
    x0, y0, W, H = 11 - 4 * U, 86 - 36 * U, 176, 36
    frames = []
    for pose, c, f, t in R.TRAMOS:
        frames += [(pose, c, f)] * t
    from animar_pixel import componer
    frames = [componer(R.LIENZO, [(R.POSES[p], c, f)]) for p, c, f in frames]
    muestra = [0, 10, 40, 75, 95, 110, 130, 150, 170, 200, 225, 245, 255, 262, 280]

ious, pares = [], []
for i in range(len(frames)):
    src = fuente(open(fs[i]).read().replace('fill="black"', 'fill="#000000"'), x0, y0, W, H)
    nuestro = pintar(frames[i], R.PALETA, R.LIENZO, PX)
    v = mejor_iou(src, np.array(nuestro))
    ious.append(v)
    if i in muestra:
        if que == 'paseo':
            # recortar alrededor del personaje para que se vea
            ma = src[..., 3] > 0; xs = np.where(ma.any(0))[0]
            c0 = max(0, xs.min() - 40); c1 = c0 + 34 * PX
            nb = np.array(nuestro); mb = nb[..., 3] > 0; xb = np.where(mb.any(0))[0]
            d0 = max(0, xb.min() - 40)
            # rellenar a la derecha para que un recorte junto al borde no se estire al escalar
            pad = lambda a: np.pad(a, ((0, 0), (0, 40 * PX), (0, 0)))
            pares.append((pad(src)[:, c0:c1], Image.fromarray(pad(nb)[:, d0:d0 + 34 * PX])))
        else:
            pares.append((src, nuestro))
print(que, 'IoU silueta min %.3f  media %.3f  max %.3f' % (min(ious), sum(ious) / len(ious), max(ious)))
peor = sorted(range(len(ious)), key=lambda k: ious[k])[:3]
print('peores instantes', [(k, round(ious[k], 3)) for k in peor])
json.dump({'min': min(ious), 'media': sum(ious) / len(ious), 'por_instante': ious}, open(f'iou_{que}.json', 'w'))
hoja(f'{que}/comparativa-demo-vs-reconstruccion.png', pares, 180 if que != 'paseo' else 150)
