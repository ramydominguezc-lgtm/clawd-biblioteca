---
name: clawd-biblioteca
description: Almacén de animaciones de Claude ya terminadas — Clawd en pixel art (caminando, saltando, confeti, paseo, paseo mirando arriba, pesas, bandera) y labels de carga con la estrella animada (Thinking, Working, Researching, Clauding…) en GIF, WebP, MP4 y bloque HTML. Úsala para buscar y entregar una que ya existe. No genera nada: si la animación no está, se usa la skill clawd-animaciones.
---

# Clawd — biblioteca de animaciones

Esta skill **solo almacena y entrega**. No dibuja, no transcribe y no corre el
motor. Quien genera es la skill hermana **`clawd-animaciones`**
(`Desktop\Animaciones - Clawd`), que siempre escribe su salida aquí.

## Dónde corre

Se recomienda **Claude Code** en la PC de Ramses (`Desktop\Clawd - Biblioteca`),
pero también sirve en **claude.ai web**. Ahí la biblioteca es la carpeta donde está
montada esta skill y es **de solo lectura**: para entregar, se copia el archivo
a la carpeta de salida de la conversación y se da para descargar. No se escribe
nada nuevo aquí desde la web.

## Cómo entregar

1. Leer `CATALOGO.md`: una fila por animación, con su estado.
2. Elegir el archivo por destino (tabla de abajo) dentro de la carpeta de esa
   animación.
3. Entregar la ruta. Si hace falta, leer el `LEEME.md` de la carpeta para ver
   sus diferencias con la fuente y sus reglas.

**Si la animación no está o hay que cambiarla** (otro tamaño, otro fondo, otro
ritmo): no se edita aquí a mano. Se pasa a `clawd-animaciones` con su input
estricto (`modo`, `nombre`, `destino`, …), que regenera en la misma carpeta.

## Qué archivo según el destino

| Destino | Archivo |
|---|---|
| Web, landing | `<n>.webp` — alfa real |
| WhatsApp, correo, Notion | `<n>.gif` — fondo crema horneado |
| Fondo claro que no es crema | `<n>-transparente.gif` |
| Reel, story, post de Instagram | `<n>.mp4` |
| Sitio propio | `<n>-hoja.png` + `<n>.css` |
| Canvas, artifact, Claude Design | `<n>-bloque.html` — SVG en línea, autónomo |
| Una pose suelta | `svg/<n>-<pose>.svg` |

Las carpetas `fotogramas/` y `svg/` de cada animación se pueden borrar y
regenerar: no son la fuente de verdad, la receta en `clawd-animaciones` sí.

## Labels de carga

En `labels/`, cada uno en versión clara y oscura. Ver `labels/LEEME.md` y
`labels/muestrario.png`. Formatos: `-claro.gif`/`-oscuro.gif`, `.mp4` igual,
`.webp` transparente por tema y `-bloque.html` en vivo. Si la palabra no está,
se genera con `clawd-animaciones` (`label_carga.py`).

## Quién consume de aquí

La skill de marca **`anthro-pic-brand`** (`Desktop\anthro-pic-brand`) mete estas
animaciones en sus piezas. No las edita: las pide por su puente
`scripts/clawd_biblioteca.py`, que resuelve la ruta y avisa si esta biblioteca no
está instalada.

| Qué usa | Dónde |
|---|---|
| `paseo` — fotograma 62 y `clawd-paseo-transparente.gif` | su pieza de terminal (`salida/ventanas_67.py`), en PNG fijo y en MP4 |

**Si se regenera `paseo`, esa pieza cambia.** Avisar antes.

Al revés no pasa nada: los stickers **quietos** de Clawd —`clawd-base`,
`coffee`, `search`, `skateboard`, `headphones`— viven en la skill de marca y no
entran aquí. Esta biblioteca guarda animaciones; un PNG suelto no tiene ninguno
de los formatos de la tabla de entrega, y además `clawd-base` es otro dibujo
(regla 3).

## Reglas de uso (valen para todas)

1. **Nunca sobre fondo naranja.** Clawd es naranja y desaparece.
2. **No mezclar dibujos distintos en una pieza:** `caminando`, `saltando`,
   `confeti` y `pesas` usan el Clawd canónico (brazos de 24U); `paseo` y `paseo-arriba`, el
   de la demo (brazos de 20U); `bandera` tiene ojos "^ ^"; `clawd-base` de la
   skill de marca es otro dibujo. Juntos se leen como error.
4. **Labels de carga:** van con su color de producto, sin recolorear, y tampoco
   en piezas fijas.
3. **No en piezas fijas** (flyer, PDF): la animación se congela. Ahí va un Clawd
   quieto de `anthro-pic-brand`.

## Carpetas

```
CATALOGO.md            qué hay, receta, verificación, estado
<animacion>/           formatos + LEEME.md + comparativa contra su fuente
_fuentes/              material original extraído (código, videos, capturas)
Informe-*.pdf          informes de revisión
```

La guía de uso completa (qué pedir, alcances y limitaciones) está en la skill
generadora: `Animaciones - Clawd\GUIA.md`.
