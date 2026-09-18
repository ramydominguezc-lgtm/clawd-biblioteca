# Escribe scripts/clawd_bandera.py por piezas: cada pieza se mueve en celdas enteras.
import json

SKILL = 'C:/Users/alfav/OneDrive/Desktop/Animaciones - Clawd/scripts/'
U = 16 / 3
d = json.load(open('flag_piezas.json'))
P = d['piezas']
x0, y0 = d['x0'], d['y0']
TX0, TY0, TC, TF = d['caja_tela']

PATAS = '##..##....##..##'
cuerpo = P['cuerpo'][0].split('\n')
assert len(cuerpo[-1]) == 16
cuerpo[-2:] = [PATAS, PATAS]          # correccion por medicion: las 4 patas son rects identicos
bajas = [PATAS, PATAS]

telas = d['telas']
fil = [j for t in telas for j, f in enumerate(t) if set(f) != {'.'}]
col = [i for t in telas for f in t for i, ch in enumerate(f) if ch != '.']
fa, fb, ca, cb = min(fil), max(fil) + 1, min(col), max(col) + 1
telas = ['\n'.join(f[ca:cb] for f in t[fa:fb]) for t in telas]
asta = (100 - TX0) // 5 - ca
asta_mundo = round((100 - x0) / U)                    # columna del asta en reposo
fila_tela = round((46 - y0) / U - ((46 - TY0) / 5 - fa))

movs = []
for m in d['movs']:
    movs.append((round(m['sway'] / U), round(m['mano'] / U), round(m['izq_y'] / U), m['tela']))

# posiciones en reposo de cada pieza (col, fila) y ajuste del lienzo
pos = {'bajas': P['bajas'][1:], 'cuerpo': P['cuerpo'][1:], 'mano_izq': P['mano_izq'][1:],
       'mano_der': P['mano_der'][1:]}
c_min = min(pos['mano_izq'][0] + min(s for s, *_ in movs), asta_mundo - asta + min(s + h for s, h, *_ in movs)) - 1
f_min = fila_tela - 1
dc, df = -c_min, -f_min
ancho_tela = len(telas[0].split('\n')[0])
W = max(pos['cuerpo'][0] + 16 + max(s for s, *_ in movs),
        asta_mundo - asta + ancho_tela + max(s + h for s, h, *_ in movs)) + dc + 1
H = pos['bajas'][1] + 2 + df

doc = open('doc_bandera.txt', encoding='utf-8').read()
src = '#!/usr/bin/env python3\n"""' + doc + '"""\nimport pathlib\nimport sys\n\n'
src += 'from animar_pixel import componer, construir, verificar\n\n'
src += """PALETA = {
    '#': (217, 119, 87),    # d97757  cuerpo
    '@': (20, 20, 19),      # 141413  ojos, asta y cuadros negros
    'w': (255, 255, 255),   # ffffff  cuadros blancos (de la demo)
}

"""
src += f'LIENZO = ({W}, {H})           # en U. La ultima fila apoya en el suelo.\n'
src += 'ESCALA = 16\nTIEMPO_MS = 70\nFPS_VIDEO = 100\n\n'
src += '# ' + '-' * 74 + '\n# PIEZAS  cada una transcrita una vez, en reposo\n# ' + '-' * 74 + '\n\n'
src += '# patas de abajo: no se mecen (los pies quedan plantados)\n'
src += 'PATAS_BAJAS = (0, """\n' + '\n'.join(bajas) + '\n""")\n\n'
src += ('# cuerpo, ojos "^ ^" y patas de arriba. Las dos ultimas filas se fijaron a mano\n'
        '# por medicion: en la fuente las 4 patas son rectangulos identicos de 11 px, y\n'
        '# la de la derecha caia a media celda.\n')
src += 'CUERPO = (0, """\n' + '\n'.join(cuerpo) + '\n""")\n\n'
src += 'MANO_IZQ = (0, """\n' + P['mano_izq'][0] + '\n""")\n\n'
src += 'MANO_DER = (0, """\n' + P['mano_der'][0] + '\n""")\n\n'
src += '# 12 telas en su reticula de 5 px (1 celda = 1U), misma caja; el asta en la columna ASTA\n'
src += '\n'.join(f'T{i:02d} = (0, """\n{p}\n""")\n' for i, p in enumerate(telas))
src += '\nTELAS = [' + ', '.join(f'T{i:02d}' for i in range(len(telas))) + ']\n'
src += f'ASTA = {asta}\n\n'
src += '# posicion en reposo (columna, fila) dentro del lienzo\n'
src += f"POS_BAJAS = ({pos['bajas'][0] + dc}, {pos['bajas'][1] + df})\n"
src += f"POS_CUERPO = ({pos['cuerpo'][0] + dc}, {pos['cuerpo'][1] + df})\n"
src += f"POS_MANO_IZQ = ({pos['mano_izq'][0] + dc}, {pos['mano_izq'][1] + df})\n"
src += f"POS_MANO_DER = ({pos['mano_der'][0] + dc}, {pos['mano_der'][1] + df})\n"
src += f"POS_ASTA = ({asta_mundo + dc}, {fila_tela + df})    # columna del asta y fila superior de la tela\n\n"
src += ('# por cuadro: (balanceo del cuerpo, mano derecha, mano izquierda hacia abajo, tela)\n'
        '# en celdas. De la demo en px: balanceo [0,0,-5,-5,0,4,4,4,0,0,-5,-5],\n'
        '# mano [0,-6,-12,-14,-8,-2,0,0,-4,-10,-16,-18], mano izq [0,0,4,4,0,0,0,0,0,0,4,4],\n'
        '# redondeados a celdas enteras (U = 16/3 px).\n')
src += 'SUBIDA = [\n' + ''.join(f'    {m},\n' for m in movs[:3]) + ']\n'
src += 'BUCLE = [\n' + ''.join(f'    {m},\n' for m in movs[3:12]) + ']\n'
src += '''

def cuadro(sway, mano, izq, tela):
    capas = [
        (PATAS_BAJAS, *POS_BAJAS),
        (CUERPO, POS_CUERPO[0] + sway, POS_CUERPO[1]),
        (MANO_IZQ, POS_MANO_IZQ[0] + sway, POS_MANO_IZQ[1] + izq),
        (MANO_DER, POS_MANO_DER[0] + sway + mano, POS_MANO_DER[1]),
        (TELAS[tela], POS_ASTA[0] + sway + mano - ASTA, POS_ASTA[1]),
    ]
    return componer(LIENZO, capas)


def cuadros(entrada):
    """(poses, secuencia). entrada=False: solo el bucle. True: subida + 6 vueltas."""
    movs = (SUBIDA + BUCLE * 6) if entrada else BUCLE
    poses, secuencia, claves = {}, [], {}
    for m in movs:
        if m not in claves:
            claves[m] = f'f{len(claves):02d}'
            poses[claves[m]] = cuadro(*m)
        secuencia.append((claves[m], 1))
    return poses, secuencia


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].startswith('-'):
        print(__doc__ + "\\nUso:  python clawd_bandera.py CARPETA_DESTINO")
        sys.exit(0)
    destino = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'salida')
    for nombre, entrada in [('clawd-bandera', False), ('clawd-bandera-con-subida', True)]:
        poses, secuencia = cuadros(entrada)
        orden, medida, lienzo = construir(
            destino, poses, secuencia, PALETA, nombre=nombre, lienzo=LIENZO,
            escala=ESCALA, tiempo_ms=TIEMPO_MS, fps_video=FPS_VIDEO)
        print(nombre, '· fotogramas unicos:', len(orden), '· medida:', medida,
              '· duracion:', len(secuencia) * TIEMPO_MS / 1000, 's')
        try:
            malos = verificar(destino, nombre, orden, ESCALA)
            print('SVG infieles:', malos or 'ninguno')
        except ImportError:
            print('SVG sin verificar (falta cairosvg)')
'''
open(SKILL + 'clawd_bandera.py', 'w', encoding='utf-8', newline='\n').write(src)
print('lienzo', (W, H), 'movs', movs)
