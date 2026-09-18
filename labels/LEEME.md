# Labels de carga de Claude

La estrella animada con una palabra que brilla: `✻ Thinking…`. Es el indicador
de carga de Claude Code, replicado a partir de su propio código (versión
2.1.274, leído del programa instalado), no de capturas.

Receta: `Animaciones - Clawd/scripts/label_carga.py`. Especificación completa:
`Animaciones - Clawd/references/labels-carga.md`.

## Juego base

| Label | Por qué está | Brillo |
|---|---|---|
| `label-thinking` | Estado fijo cuando el modelo razona | derecha → izquierda, lento (5.76 s) |
| `label-working` | Palabra de respaldo de Claude Code | izquierda → derecha (1.44 s) |
| `label-researching` | Modo Research de claude.ai | izquierda → derecha |
| `label-clauding` | El verbo propio de Claude | izquierda → derecha |
| `label-pondering` · `cogitating` · `brewing` · `noodling` · `percolating` · `crafting` | Verbos de la lista de Claude Code que más se reconocen | izquierda → derecha |

Claude Code elige el verbo al azar entre 188 con la misma probabilidad, así que
no existe un "más usado" que se pueda medir. El juego base cubre los estados
fijos y los verbos con más identidad. `muestrario.png` los muestra todos en los
dos temas.

## Qué archivo usar

| Destino | Archivo |
|---|---|
| Fondo claro (crema) | `<label>-claro.gif` o `-claro.mp4` |
| Fondo oscuro | `<label>-oscuro.gif` o `-oscuro.mp4` |
| Web, encima de cualquier fondo | `<label>-claro.webp` / `-oscuro.webp` — transparentes |
| Claude Design, artifact, sitio | `<label>-bloque.html` — anima en vivo; tema con `data-tema="claro"` u `"oscuro"` |

Cada label mide ~300 px de ancho por 96 de alto (letra de 40 px). Para otro
tamaño o palabra se genera uno nuevo (abajo).

## Labels propios

En Claude Code (recomendado), desde `Desktop\Animaciones - Clawd`:

```
python scripts\label_carga.py "Investigando" "C:\Users\alfav\OneDrive\Desktop\Clawd - Biblioteca\labels"
python scripts\label_carga.py "Pensando" "...\labels" --modo pensando
python scripts\label_carga.py "Diseñando" "...\labels" --tamano 64
```

En claude.ai web, desde la carpeta de la skill `clawd-animaciones`:
`python3 scripts/label_carga.py "Investigando" <carpeta de salida>`. Ahí usa las
fuentes que trae la skill (la estrella cambia apenas de trazo) y, si no hay
ffmpeg, no sale el MP4.

Se escribe la palabra sin los tres puntos: los agrega el script. `--modo`
`solicitando` (por defecto) hace el brillo rápido de izquierda a derecha;
`pensando`, el lento de derecha a izquierda.

## Reglas

- **No van en piezas fijas.** En un PDF o flyer el label congelado parece un
  error de carga.
- **El color es el del producto** (`rgb(215,119,87)`, casi el `#d97757` de marca).
  No se recolorea: el label es reconocible por ser idéntico al de Claude.
