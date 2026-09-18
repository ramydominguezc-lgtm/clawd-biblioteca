# Escribe clawd_paseo.py y clawd_paseo_arriba.py (version 2, por piezas, 20 ms).
import json

# reusar las funciones de generar_recetas.py sin ejecutar su parte final
fuente = open('generar_recetas.py', encoding='utf-8').read().split('CLAWD = [')[0]
exec(fuente)

CLAWD = [('#', (217, 119, 87), 'd97757  cuerpo'), ('@', (20, 20, 19), '141413  ojo')]
for archivo, nombre, datos, doc in [
        ('clawd_paseo.py', 'clawd-paseo', 'paseo_abajo_rec.json', 'doc_paseo.txt'),
        ('clawd_paseo_arriba.py', 'clawd-paseo-arriba', 'paseo_arriba_rec.json', 'doc_paseo_arriba.txt')]:
    rec = [tuple(x) for x in json.load(open(datos))]
    _, _, w, h = ajustar(rec)
    escala = 1080 // w
    escala -= escala % 2          # MP4 exige medidas pares
    escribir_simple(archivo, nombre, open(doc, encoding='utf-8').read(), CLAWD, rec,
                    [1] * len(rec), 20, 50, escala)
