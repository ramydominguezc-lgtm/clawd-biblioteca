# Bandera por piezas: cada pieza se transcribe una vez en reposo y se mueve en celdas enteras.
import glob, json, re
import xml.etree.ElementTree as ET
from transcribir_svg import transcribir, recortar, U

NS = '{http://www.w3.org/2000/svg}'
ET.register_namespace('', 'http://www.w3.org/2000/svg')
fs = sorted(glob.glob('cap_flag/t*.svg'))
T_CUERPO = {'#DD775B': '#', '#000000': '@'}
T_TELA = {'#000000': '@', '#FFFFFF': 'w'}
cols, filas = 32, 29
x0, y0 = 21.6589 - 6 * U, 146 - filas * U
TX0, TY0, TC, TF = 40, -10, 24, 14


def limpiar(s):
    return s.replace('fill="black"', 'fill="#000000"').replace('fill="white"', 'fill="#FFFFFF"')


def doc(elems):
    cuerpo = ''.join(re.sub(r'\s(style|data-svg-origin|transform)="[^"]*"', '', ET.tostring(e, encoding='unicode'))
                     for e in elems)
    return f'<svg xmlns="http://www.w3.org/2000/svg">{cuerpo}</svg>'


def pieza(elems):
    return recortar(transcribir(doc(elems), T_CUERPO, x0, y0, cols, filas))


raiz = ET.fromstring(limpiar(open(fs[0]).read()))
hijos = list(raiz)
bajas = [e for e in hijos if e.tag == f'{NS}rect']                       # dleg*: no se mecen
g_cuerpo = [e for e in hijos if e.tag == f'{NS}g'][0]
g_mano = [g for g in g_cuerpo.findall(f'{NS}g') if g.get('data-svg-origin') == '92 0'][0]
mano_izq = [e for e in g_cuerpo if e.get('id') == 'left-hand'][0]
resto = [e for e in g_cuerpo if e is not g_mano and e is not mano_izq]  # patas altas, cuerpo, ojos
mano_der = [e for e in g_mano if e.tag == f'{NS}rect']

piezas = {'bajas': pieza(bajas), 'cuerpo': pieza(resto), 'mano_izq': pieza([mano_izq]),
          'mano_der': pieza(mano_der)}
telas = []
for g in g_mano.findall(f'{NS}g'):
    s = re.sub(r'\sstyle="[^"]*"', '', ET.tostring(g, encoding='unicode'))
    telas.append(transcribir(f'<svg xmlns="http://www.w3.org/2000/svg">{s}</svg>', T_TELA, TX0, TY0, TC, TF, u=5))

# movimiento por cuadro, leido del SVG capturado (no de las constantes: es lo que de verdad pinto)
movs = []
for f in fs:
    r = ET.fromstring(limpiar(open(f).read()))
    gc = [e for e in r if e.tag == f'{NS}g'][0]
    gm = [g for g in gc.findall(f'{NS}g') if g.get('data-svg-origin') == '92 0'][0]
    mi = [e for e in gc if e.get('id') == 'left-hand'][0]
    mx = lambda e: float(re.search(r'matrix\(1,0,0,1,(-?[\d.]+),', e.get('transform')).group(1))
    visible = [i for i, g in enumerate(gm.findall(f'{NS}g')) if 'inline' in g.get('style', '')][0]
    movs.append({'sway': mx(gc), 'mano': mx(gm), 'izq_y': float(mi.get('y')) - 90, 'tela': visible})

json.dump({'piezas': piezas, 'telas': telas, 'movs': movs, 'x0': x0, 'y0': y0,
           'caja_tela': [TX0, TY0, TC, TF]}, open('flag_piezas.json', 'w'), indent=1)
for k, (p, c, f) in piezas.items():
    print(k, c, f); print(p)
print([(m['sway'], m['mano'], m['izq_y'], m['tela']) for m in movs])
