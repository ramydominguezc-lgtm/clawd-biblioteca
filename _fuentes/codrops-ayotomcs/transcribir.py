# Transcribe los dibujos SVG de la demo a rejillas de texto en unidades U.
# Metodo: rasterizar a alta resolucion, buscar la fase de reticula que minimiza
# el error de color, y tomar la moda por celda (no el centro: es robusto a
# rectangulos corridos fracciones de unidad).
import io, json, re
from collections import Counter
import numpy as np, cairosvg
from PIL import Image

kids = json.load(open('kids.json'))
K = 12  # px de raster por px SVG
TINTA = {(221, 119, 91): '#', (0, 0, 0): '@', (221, 131, 97): 'n',
         (124, 164, 208): 'a', (200, 115, 146): 'r', (203, 112, 143): 'r'}

def raster(contenido, vb):
    x, y, w, h = vb
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
         f'width="{w*K}" height="{h*K}" shape-rendering="crispEdges">{contenido}</svg>')
    a = np.array(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=s.encode()))).convert('RGBA'))
    return a

def celda_tinta(bloque):
    px = bloque.reshape(-1, 4)
    cuenta = Counter()
    for r, g, b, al in px[::7]:
        cuenta[TINTA.get((r, g, b), '?') if al > 128 else '.'] += 1
    return cuenta.most_common(1)[0][0], cuenta

def muestrear(a, u, fx, fy, vb, W, H):
    """Rejilla W x H con celda de u px SVG; la celda (0,0) empieza en (vb.x+fx, vb.y+fy)."""
    filas, err = [], 0
    for j in range(H):
        fila = ''
        for i in range(W):
            x0 = round((i * u + fx) * K); y0 = round((j * u + fy) * K)
            b = a[y0:y0 + round(u * K), x0:x0 + round(u * K)]
            if b.size == 0:
                fila += '.'; continue
            ch, cuenta = celda_tinta(b)
            err += sum(cuenta.values()) - cuenta[ch]
            fila += ch
        filas.append(fila)
    return filas, err

def mejor(contenido, u, vb, W, H, fases_x, fases_y):
    a = raster(contenido, vb)
    res = min((muestrear(a, u, fx, fy, vb, W, H) + (fx, fy) for fx in fases_x for fy in fases_y),
              key=lambda r: r[1])
    return res

U = 16 / 3
# personaje: caja SVG x -8..136, y 113-26U..113 ; fila inferior apoya en 113
W, H = 27, 26
vb = (-8, 113 - H * U, 27 * U, H * U)
# una sola fase para todos: las patas no deben brincar entre cuadros
pasos = [k * U / 8 for k in range(8)]
import sys
ras = [raster(kids[i], vb) for i in range(8)]
tot = {p: sum(muestrear(a, U, p, 0, vb, W, H)[1] for a in ras) for p in pasos}
print('error total por fase:', {round(k, 2): v for k, v in tot.items()})
FASE = min(tot, key=tot.get)
pers = {}
for i in range(8):
    filas, err = muestrear(ras[i], U, FASE, 0, vb, W, H); fx = FASE
    pers[f'p{i}'] = filas
    print(f'p{i} err={err} fase_x={fx:.2f}')
    print('\n'.join(filas))

# confeti: la raiz es el grupo que se mueve; sus hijos son los 8 cuadros
raiz = kids[8]
interior = raiz[len('<g>'):-len('</g>')]
cuadros = re.findall(r'<g>(.*?)</g>', interior)
print('cuadros de confeti:', len(cuadros))
vbc = (-15, -15, 90, 90)
Wc, Hc = 18, 18
# una sola fase para los 8 cuadros: se buscan juntas
todo = ''.join(f'<g>{c}</g>' for c in cuadros)
_, _, fx, fy = mejor(todo, 5, vbc, Wc, Hc, range(5), range(5))
print('fase confeti', fx, fy)
conf = {}
for i, c in enumerate(cuadros):
    filas, err = muestrear(raster(c, vbc), 5, fx, fy, vbc, Wc, Hc)
    conf[f'c{i}'] = filas
    print(f'c{i} err={err}'); print('\n'.join(filas))
json.dump({'personaje': pers, 'confeti': conf, 'fase_confeti': [fx, fy], 'vb_confeti': vbc,
           'vb_personaje': vb}, open('transcripcion.json', 'w'), indent=1)
