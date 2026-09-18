# Clawd caminando

Animación de la mascota reconstruida desde una captura de pantalla de 60 fps.
No es un recorte del video: se recuperó la retícula lógica del sprite, se
transcribió cada pose y se volvió a dibujar en los hex reales de la paleta.

13 fotogramas únicos · 80 ms por tiempo · ciclo de 2.64 s · IoU 0.973 contra el original.

## Qué usar según el destino

| Destino | Archivo |
|---|---|
| Web, landing | `clawd-caminando.webp` — alfa real, 8 KB |
| WhatsApp, correo, Notion | `clawd-caminando.gif` — fondo crema horneado |
| Fondo claro que no es crema | `clawd-caminando-transparente.gif` |
| Reel, story | `clawd-caminando.mp4` — 60 fps, 2.63 s |
| Sitio propio | `clawd-caminando-hoja.png` + `clawd-caminando.css` |
| Canvas, artifact, Claude Design | `clawd-caminando-bloque.html` + `prompt-claude-design.md` |
| Imagen fija de esta versión | `svg/clawd-caminando-quieto.svg` (se genera, ver abajo) |

**Nunca sobre fondo naranja**: Clawd es naranja y desaparece. Blanco, crema y
oscuro funcionan.

**No va en piezas fijas.** Si el destino es un flyer o un PDF, usa un Clawd
quieto de `anthro-pic-brand/assets/clawd/`; una animación exportada a imagen
pierde lo único que aportaba.

## Tiempo

El video fuente mostraba cada tiempo durante 5 cuadros a 60 fps, o sea 83.3 ms.
La receta usa `tiempo_ms=80`, **y así se queda** (decidido por Ramses el
16/09/2026). Todos los formatos duran 2.64 s; el MP4 ahora también (2.63 s, por
el redondeo a 60 fps). Antes el MP4 redondeaba cada tiempo a 5 cuadros y duraba
2.75 s.

**No mezclar con `clawd-base`.** Es otro dibujo: cuerpo de 8 celdas de ancho
contra 12, ojos en otra posición. Son dos versiones válidas de la mascota, pero
juntas en una misma pieza se leen como un error.

## Contenido

```
clawd-caminando.webp / .gif / -transparente.gif / .mp4
clawd-caminando-hoja.png        hoja de sprites, 13 × 448×320
clawd-caminando.css / .html     keyframes listos para pegar, más demo
clawd-caminando-bloque.html     SVG en línea autónomo, 5.9 KB
prompt-claude-design.md         prompt validado para un post en Claude Design
comparativa-original-vs-reconstruccion.png
prueba-bloque-en-navegador.png
```

Esta carpeta es el **almacén** (skill `clawd-biblioteca`). El método y la receta
están en la skill generadora `clawd-animaciones` (`Desktop\Animaciones - Clawd`):
`references/animacion-pixel.md`, `scripts/animar_pixel.py` y
`scripts/clawd_caminando.py`.

La demo `clawd-caminando.html` enseña la animación, pero su tira de poses pide
`fotogramas/`, que no se guarda aquí. Para verla completa, ábrela desde una
carpeta regenerada.

## Para hacer una animación nueva

Leer `references/animacion-pixel.md`. El motor no sabe nada de Clawd: recibe
poses escritas como texto, una secuencia con duraciones y una paleta.

```python
from animar_pixel import construir, espejo

PALETA = {'#': (217, 119, 87), '@': (20, 20, 19)}
POSE = (4, """
..####..
..#@@#..
..#..#..
""")
construir('salida', {'a': POSE}, [('a', 2)], PALETA, nombre='mi-animacion')
```

Regenerar esta (desde `Desktop\Animaciones - Clawd`):
`python scripts/clawd_caminando.py "C:\Users\alfav\OneDrive\Desktop\Clawd - Biblioteca\caminando"`

Después, borrar `fotogramas/` y `svg/`: aquí no se guardan. El motor no toca
este `LEEME`, el prompt ni las imágenes de prueba.

## Colores

```
cuerpo   #d97757
sombra   #b8654a      el naranja × 0.85
ojo      #141413
```

La captura venía en `#d46c4d` por la compresión del códec. El 0.85 no es
criterio: es la razón medida entre las dos tintas del sprite original, idéntica
en los tres canales.

Desde septiembre de 2026 la animación ya no vive en la skill de marca: la receta
está en `clawd-animaciones` y los archivos, aquí.

## Lo que no está en esta carpeta

Los 13 fotogramas en PNG y los 13 SVG por pose **no se guardan**: son 26
archivos derivados que se regeneran con la orden de arriba.

Verificado el 16 de septiembre de 2026 en Windows:

- GIF, GIF transparente, WebP y bloque: **idénticos byte por byte** al original.
- CSS y demo: iguales salvo el comentario, que ahora dice "Tiempo base: 80 ms"
  en vez de "12 fps" (corregido el 16/09/2026).
- Hoja de sprites: idéntica píxel por píxel (cambia solo la compresión del PNG).
- MP4: regenerado el 16/09/2026 con el redondeo acumulado: 158 cuadros, 2.63 s.
- Los 13 SVG pintan exactamente lo mismo que sus PNG.
