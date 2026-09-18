# Comparativa de los paseos v2: la demo se dibuja desde su geometria capturada.
import glob, json, sys
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, 'C:/Users/alfav/OneDrive/Desktop/Animaciones - Clawd/scripts')
from animar_pixel import pintar, componer
U = 16 / 3
PX = 8
B = 'C:/Users/alfav/OneDrive/Desktop/Clawd - Biblioteca/'
COL = {'#DD775B': (217, 119, 87, 255), 'black': (20, 20, 19, 255)}
x0, y0, W, H = 11 - 4 * U, 86 - 36 * U, 68, 36


def demo(cap):
    im = Image.new('RGBA', (W * PX, H * PX), (0, 0, 0, 0))
    for pz in cap['piezas']:
        capa = Image.new('RGBA', im.size, (0, 0, 0, 0))
        f = lambda p: ((p[0] - x0) / U * PX, (p[1] - y0) / U * PX)
        ImageDraw.Draw(capa).polygon([f(p) for p in pz['pts']], fill=COL[pz['fill']])
        if pz.get('recorte'):
            m = Image.new('L', im.size, 0)
            ImageDraw.Draw(m).polygon([f(p) for p in pz['recorte']], fill=255)
            capa.putalpha(Image.fromarray(np.minimum(np.array(capa)[..., 3], np.array(m))))
        im.alpha_composite(capa)
    return np.array(im)


def iou(a, b):
    ma, mb = a[..., 3] > 128, b[..., 3] > 128
    ya, xa = np.where(ma); yb, xb = np.where(mb)
    Hh, Ww = ma.shape[0] + 200, ma.shape[1] + 200
    A = np.zeros((Hh, Ww), bool); A[ya + 100, xa + 100] = True
    best = 0
    for dy in range(-PX, PX + 1, 2):
        for dx in range(-PX, PX + 1, 2):
            oy = ya.min() + 100 - yb.min() + dy; ox = xa.min() + 100 - xb.min() + dx
            Bm = np.zeros((Hh, Ww), bool)
            ys, xs = yb + oy, xb + ox
            ok = (ys >= 0) & (ys < Hh) & (xs >= 0) & (xs < Ww)
            Bm[ys[ok], xs[ok]] = True
            best = max(best, (A & Bm).sum() / (A | Bm).sum())
    return best


for mod, geo, carpeta in [('clawd_paseo', 'geo_abajo', 'paseo'), ('clawd_paseo_arriba', 'geo_arriba', 'paseo-arriba')]:
    R = __import__(mod)
    fr = []
    for p, c, f, t in R.TRAMOS:
        fr += [(p, c, f)] * t
    fs = sorted(glob.glob(f'{geo}/t*.json'))[:576]
    ious, pares = [], []
    muestra = list(range(0, 576, 38))[:15]
    for i in range(576):
        a = demo(json.load(open(fs[i])))
        b = np.array(pintar(componer(R.LIENZO, [(R.POSES[fr[i][0]], fr[i][1], fr[i][2])]), R.PALETA, R.LIENZO, PX))
        ious.append(iou(a, b))
        if i in muestra:
            pares.append((a, b, i))
    print(carpeta, 'IoU silueta min %.3f media %.3f max %.3f' % (min(ious), np.mean(ious), max(ious)))
    # hoja: demo arriba, replica abajo; se recorta cada cuadro alrededor del personaje
    tw, th = 34 * PX, 36 * PX
    sh = Image.new('RGB', (tw * len(pares) // 2, (th * 2 + 30) // 2), (255, 255, 255))
    d = ImageDraw.Draw(sh)
    for k, (a, b, i) in enumerate(pares):
        for fila, arr in ((0, a), (1, b)):
            if arr.shape[0] < th:      # la replica es mas baja: se rellena arriba (el suelo queda abajo)
                arr = np.pad(arr, ((th - arr.shape[0], 0), (0, 0), (0, 0)))
            m = arr[..., 3] > 0; xs = np.where(m.any(0))[0]
            c0 = max(0, xs.min() - 5 * PX)
            pad = np.pad(arr, ((0, 0), (0, 40 * PX), (0, 0)))[:, c0:c0 + tw]
            base = Image.new('RGBA', (tw, arr.shape[0]), (250, 249, 245, 255))
            base.alpha_composite(Image.fromarray(pad))
            base = base.crop((0, arr.shape[0] - th, tw, arr.shape[0])).resize((tw // 2, th // 2), Image.NEAREST)
            sh.paste(base.convert('RGB'), (k * tw // 2, 14 + fila * (th // 2 + 2)))
        d.text((k * tw // 2 + 2, 0), f'{i * 0.02:.2f}s', fill='black')
    sh.save(B + carpeta + '/comparativa-demo-vs-reconstruccion.png')
