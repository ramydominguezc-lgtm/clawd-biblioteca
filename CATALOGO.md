# Clawd — catálogo de animaciones

Almacén de la skill `clawd-biblioteca`. Las recetas que regeneran cada
animación viven en la skill `clawd-animaciones` (`Desktop\Animaciones - Clawd\scripts\`).

Antes de generar algo nuevo, buscar aquí. Si ya existe, se entrega el archivo.

| Animación | Carpeta | Receta | Cuadros · ritmo | Verificación | Estado |
|---|---|---|---|---|---|
| Clawd caminando (en el sitio) | `caminando\` | `clawd_caminando.py` | 13 únicos · 80 ms · 2.64 s (todos los formatos) | IoU 0.973 contra captura | **aprobada** |
| Clawd con confeti | `confeti\` | `clawd_confeti.py` | 8 · 125 ms · 1 s | IoU de forma 0.944–0.961 contra la demo | **aprobada** |
| Clawd con pesas | `pesas\` | `clawd_pesas.py` | 30 únicos · 85–1500 ms · 7.125 s | IoU silueta 0.937–0.977 | **aprobada** |
| Clawd con bandera | `bandera\` | `clawd_bandera.py` | bucle 9 · 70 ms · 0.63 s; con subida 3.99 s | IoU silueta 0.889–0.920 | **aprobada** |
| Clawd saltando | `saltando\` | `clawd_saltando.py` | 13 · 83 ms · 1.74 s · 448×496 | IoU naranja 0.951–0.958 contra video | **aprobada** |
| Clawd de paseo (avanza, mira abajo) | `paseo\` | `clawd_paseo.py` | 106 únicos · 20 ms · 11.52 s · 1008×544 | IoU silueta 0.861–0.963 | **aprobada** (v5: se agacha al mirar abajo) |
| Clawd de paseo mirando arriba | `paseo-arriba\` | `clawd_paseo_arriba.py` | 101 únicos · 20 ms · 11.52 s · 1008×544 | IoU silueta 0.876–0.963 | **aprobada** |

## Labels de carga

`labels\` · receta `label_carga.py` · especificación de Claude Code 2.1.274.

| Label | Modo | Vuelta | Estado |
|---|---|---|---|
| Thinking | pensando | 5.76 s | **aprobado** |
| Working · Researching · Clauding · Pondering · Cogitating · Brewing · Noodling · Percolating · Crafting | solicitando | 1.44 s | **aprobados** |

Todos en claro y oscuro: GIF, MP4, WebP transparente y bloque HTML.

"Lista" = verificada contra su fuente y pendiente de tu visto bueno. "Aprobada"
= la revisaste tú.

## Fuentes

`_fuentes\codrops-ayotomcs\`: artículo de Codrops, código de los cuatro
componentes de la demo de ayotomcs.me/claude-mascot, videos del artículo y
scripts de transcripción. Las cuatro animaciones de esa página ya están
replicadas.

## Cómo regenerar

```
En Claude Code (recomendado):
cd "C:\Users\alfav\OneDrive\Desktop\Animaciones - Clawd"
python scripts\clawd_<receta>.py "C:\Users\alfav\OneDrive\Desktop\Clawd - Biblioteca\<carpeta>"

En claude.ai web, desde la carpeta de la skill clawd-animaciones:
python3 scripts/clawd_<receta>.py <carpeta de salida>/<carpeta>
```

En claude.ai lo regenerado sale para descargar; la biblioteca de la web no cambia
hasta que se vuelva a subir su ZIP.

`caminando` se queda en 80 ms (decidido el 16/09/2026): se puede regenerar
sobre su carpeta sin cuidado especial. `prompt-claude-design.md`, las
comparativas y los `LEEME.md` no los escribe el motor y no se tocan.
