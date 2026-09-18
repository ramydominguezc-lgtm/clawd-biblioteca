# Escribe las recetas clawd_paseo.py, clawd_pesas.py y clawd_bandera.py a partir
# de las transcripciones. Las recetas quedan autonomas: solo importan el motor.
import json

SKILL = 'C:/Users/alfav/OneDrive/Desktop/Animaciones - Clawd/scripts/'
U = 16 / 3


def bloque_pose(nombre, texto):
    return f'{nombre} = (0, """\n{texto}\n""")\n'


def ajustar(colocaciones):
    """Recorta el mundo al area usada, con 1 celda de margen. Devuelve (dx, dy, w, h)."""
    c0 = min(c for _, c, _ in colocaciones) - 1
    f0 = min(f for _, _, f in colocaciones) - 1
    c1 = max(c + len(p.split('\n')[0]) for p, c, _ in colocaciones) + 1
    f1 = max(f + len(p.split('\n')) for p, _, f in colocaciones)   # el suelo es la ultima fila
    return c0, f0, c1 - c0, f1 - f0


def tramos_de(lista):
    """[(clave, col, fila)] por instante -> [[clave, col, fila, n]] agrupando iguales seguidos."""
    out = []
    for x in lista:
        if out and out[-1][:3] == list(x):
            out[-1][3] += 1
        else:
            out.append([*x, 1])
    return out


def nombrar(poses_texto):
    orden = []
    for p in poses_texto:
        if p not in orden:
            orden.append(p)
    return {p: f'P{i:02d}' for i, p in enumerate(orden)}, orden


PIE = '''

def cuadros():
    """(poses, secuencia) para el motor: una pose compuesta por combinacion unica."""
    poses, secuencia, claves = {{}}, [], {{}}
    for pose, col, fila, tiempos in TRAMOS:
        k = (pose, col, fila)
        if k not in claves:
            claves[k] = f'f{{len(claves):03d}}'
            poses[claves[k]] = componer(LIENZO, [(POSES[pose], col, fila)])
        secuencia.append((claves[k], tiempos))
    return poses, secuencia


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
        print(__doc__ + "\\nUso:  python {script} CARPETA_DESTINO")
        sys.exit(0)
    destino = sys.argv[1] if len(sys.argv) > 1 else 'salida'
    poses, secuencia = cuadros()
    orden, medida, lienzo = construir(
        destino, poses, secuencia, PALETA, nombre='{nombre}', lienzo=LIENZO,
        escala=ESCALA, tiempo_ms=TIEMPO_MS, fps_video=FPS_VIDEO)
    print('fotogramas unicos:', len(orden), '· medida:', medida, '· lienzo en U:', lienzo)
    print('duracion del ciclo:', sum(t for _, t in secuencia) * TIEMPO_MS / 1000, 's')
    try:
        malos = verificar(pathlib.Path(destino), '{nombre}', orden, ESCALA)
        print('SVG infieles:', malos or 'ninguno')
    except ImportError:
        print('SVG sin verificar (falta cairosvg)')
'''


def escribir_simple(archivo, nombre, doc, paleta, rec, tiempos_por_instante, tiempo_ms, fps, escala):
    mapa, orden = nombrar([r[0] for r in rec])
    dx, dy, w, h = ajustar(rec)
    lista = [(mapa[p], c - dx, f - dy) for p, c, f in rec]
    # agrupar instantes iguales seguidos sumando sus tiempos
    tramos = []
    for (k, c, f), t in zip(lista, tiempos_por_instante):
        if tramos and tramos[-1][:3] == [k, c, f]:
            tramos[-1][3] += t
        else:
            tramos.append([k, c, f, t])
    src = '#!/usr/bin/env python3\n"""' + doc + '"""\nimport pathlib\nimport sys\n\n'
    src += 'from animar_pixel import componer, construir, verificar\n\n'
    src += 'PALETA = {\n' + ''.join(f"    '{ch}': {rgb},    # {com}\n" for ch, rgb, com in paleta) + '}\n\n'
    src += f'LIENZO = ({w}, {h})           # en U. La ultima fila apoya en el suelo.\n'
    src += f'ESCALA = {escala}\nTIEMPO_MS = {tiempo_ms}\nFPS_VIDEO = {fps}\n\n'
    src += '# ' + '-' * 74 + '\n# POSES  recortadas a su caja; TRAMOS las coloca en el lienzo\n# ' + '-' * 74 + '\n\n'
    src += '\n'.join(bloque_pose(mapa[p], p) for p in orden)
    src += '\nPOSES = {' + ', '.join(f"'{mapa[p]}': {mapa[p]}" for p in orden) + '}\n\n'
    src += '# (pose, columna, fila, tiempos) en orden de reproduccion\nTRAMOS = [\n'
    src += ''.join(f"    ('{k}', {c}, {f}, {t}),\n" for k, c, f, t in tramos) + ']\n'
    src += PIE.format(script=archivo, nombre=nombre)
    open(SKILL + archivo, 'w', encoding='utf-8', newline='\n').write(src)
    print(archivo, 'poses', len(orden), 'tramos', len(tramos), 'lienzo', (w, h),
          'duracion', sum(t for *_, t in tramos) * tiempo_ms / 1000)


CLAWD = [('#', (217, 119, 87), 'd97757  cuerpo'), ('@', (20, 20, 19), '141413  ojo')]

# ------------------------------------------------------------------ paseo
rec = [tuple(x) for x in json.load(open('walk_rec.json'))]
escribir_simple('clawd_paseo.py', 'clawd-paseo', DOC_PASEO := open('doc_paseo.txt', encoding='utf-8').read(),
                CLAWD, rec, [1] * len(rec), 40, 50, 6)

# ------------------------------------------------------------------ pesas
rec = [tuple(x) for x in json.load(open('gym_rec.json'))]
d = json.load(open('gym_t.json'))['d']
escribir_simple('clawd_pesas.py', 'clawd-pesas', open('doc_pesas.txt', encoding='utf-8').read(),
                CLAWD + [('d', (26, 76, 129), '1a4c81  barra (de la demo)'),
                         ('g', (93, 91, 86), '5d5b56  gris (de la demo)')],
                rec, [round(x * 1000 / 5) for x in d], 5, 60, 16)
