# Transcribe "Clawd saltando" del video: 3 ciclos, 12 tiempos de movimiento + pausa.
import glob, json
from collections import Counter
import numpy as np
from PIL import Image

fs = sorted(glob.glob('frames/*.png'))
U = 568 / 24                 # px por celda: el reposo mide 24 U de ancho
X0 = 694 - 2 * U             # 2 columnas de margen a la izquierda del reposo
SUELO = 872                  # borde de abajo de las patas en reposo
COLS, FILAS = 28, 32
Y0 = SUELO - FILAS * U
NARANJA = np.array([215, 119, 87])


def celdas(i):
    a = np.array(Image.open(fs[i]).convert('RGB')).astype(int)
    g = np.zeros((FILAS, COLS), dtype='<U1')
    for f in range(FILAS):
        for c in range(COLS):
            x0 = X0 + c * U; y0 = Y0 + f * U
            blk = a[int(y0 + U * .3):int(y0 + U * .7), int(x0 + U * .3):int(x0 + U * .7)]
            naranja = np.abs(blk - NARANJA).sum(2) < 90
            g[f, c] = '#' if naranja.mean() > .5 else '.'
    return g


def ojos(g):
    """Las celdas oscuras que no se alcanzan desde el borde son ojos."""
    g = g.copy()
    visto = np.zeros(g.shape, bool)
    pila = [(f, c) for f in range(FILAS) for c in (0, COLS - 1)] + [(f, c) for c in range(COLS) for f in (0, FILAS - 1)]
    while pila:
        f, c = pila.pop()
        if not (0 <= f < FILAS and 0 <= c < COLS) or visto[f, c] or g[f, c] != '.':
            continue
        visto[f, c] = True
        pila += [(f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)]
    g[(g == '.') & ~visto] = '@'
    return g


# cortes medidos (diferencia entre cuadros): inicio de cada tiempo, por ciclo
CICLOS = [
    [14, 17, 19, 22, 24, 27, 29, 32, 34, 37, 39, 41, 44, 67],
    [67, 69, 72, 74, 77, 79, 82, 84, 87, 89, 92, 94, 97, 120],
    [120, 122, 125, 127, 130, 132, 135, 137, 140, 142, 145, 147, 150, 173],
]


def cuadros_del_tiempo(k):
    """Cuadros de video del tiempo k (0-11 movimiento, 12 pausa) en los 3 ciclos.
    En tiempos de 3 cuadros se descarta el primero, que trae mezcla de la transicion."""
    out = []
    for c in CICLOS:
        idx = list(range(c[k], c[k + 1]))
        if 3 <= len(idx) <= 4:
            idx = idx[1:]
        elif len(idx) > 4:
            idx = idx[2:-2]
        out += idx
    return out


poses = []
for k in range(13):
    rej = [ojos(celdas(i)) for i in cuadros_del_tiempo(k)]
    moda = np.empty((FILAS, COLS), dtype='<U1')
    acuerdo = []
    for f in range(FILAS):
        for c in range(COLS):
            cnt = Counter(r[f, c] for r in rej)
            moda[f, c], n = cnt.most_common(1)[0]
            acuerdo.append(n / len(rej))
    texto = [''.join(fila) for fila in moda]
    poses.append(texto)
    print(f'tiempo {k}: {len(rej)} cuadros, acuerdo minimo por celda {min(acuerdo):.2f}')
json.dump(poses, open('poses.json', 'w'), indent=1)
for k, p in enumerate(poses):
    filas = [i for i, l in enumerate(p) if set(l) != {'.'}]
    print('== tiempo', k)
    print('\n'.join(p[filas[0]:]))
