# Clawd de paseo

Réplica de "Walking Claude" (Codrops, mayo 2026; demo en ayotomcs.me/claude-mascot).
Clawd se inclina a un lado y al otro, baja la vista, da un brinco, avanza
caminando, mira abajo, se agacha y salta.

**Versión 5** (16/09/2026) · 106 cuadros únicos · 20 ms (50 fps) · ciclo de 11.52 s ·
lienzo 63×34 U · **1008×544 px**. Receta: `Animaciones - Clawd/scripts/clawd_paseo.py`.
Variante con la mirada hacia arriba: `paseo-arriba/`.

**No es `caminando`.** Aquella camina en el sitio con 13 poses dibujadas; esta
avanza y es otro dibujo (brazos de 20U en vez de 24U). No se mezclan en una pieza.

## Qué cambió respecto a las versiones 1 y 2

La primera versión tenía errores visibles: escalones sueltos al inclinarse,
patas partidas, ojos deformes y un cuerpo que medía 15 o 16 celdas según el
cuadro. Venían de rasterizar al personaje entero a 25 fps. Ahora:

| Antes | Ahora |
|---|---|
| Captura de imagen cada 40 ms (25 fps) | Geometría exacta de cada pieza cada 20 ms (50 fps) |
| Muestreo del personaje entero | Cada pieza se dibuja sola: cuerpo 16×12, patas de 2 de ancho, ojos 2×2 |
| Rotación = escalones en cualquier columna | El cuerpo no rota: se desplaza entero y no se deforma. Las patas tampoco hacen escalón: se dibujan rectas y corridas enteras hacia donde se inclinan, como en el original |
| (v2) Las patas desaparecían al caminar | Las patas nacen siempre debajo del cuerpo: 4 filas apoyadas, 2 levantadas, nunca menos |
| Desplazamientos de fracciones de celda | El personaje se mueve en celdas enteras |
| Recorrido de 800 unidades (banner 5:1) | **Recortado a 214 unidades** (2 veces su ancho) para posts y reels |

## Diferencias deliberadas con la demo

- **Recorrido fijo y corto:** la demo lo calcula con el ancho de la página.
  Aquí se conserva la proporción de la fuente: 55 % caminando y 45 % saltando.
- **Inclinación:** en la demo el cuerpo rota de 3° a 9°. Aquí el cuerpo solo se desplaza (rotarlo lo deformaba) y las patas se corren enteras, rectas (con escalón se veían demasiado diagonales).
- **Patas al caminar:** en la demo se encogen y se despegan del cuerpo hasta desaparecer. Aquí siempre están pegadas al cuerpo, con al menos 2 filas.
- **Se agacha al mirar abajo** (idea de Ramses, no está en la demo): cuando los ojos bajan, el cuerpo baja una fila y las patas quedan una más cortas. Pasa de 3.54 a 4.04 s y de 7.58 a 8.88 s. La mirada leve de las inclinaciones no lo activa.
- **Color:** cuerpo `#d97757` en vez del `#DD775B` de la demo.

## Verificación

- IoU de silueta contra la demo (mejor alineación, 576 instantes): mínimo 0.861,
  media 0.913, máximo 0.963. Las diferencias son las decisiones de arriba:
  cuerpo sin rotar, patas siempre visibles y el agachado al mirar abajo.
- `SVG infieles: ninguno`. GIF y MP4 duran exactamente 11.52 s.
- `comparativa-demo-vs-reconstruccion.png`: 15 momentos del ciclo.

## Para redes

A 1008 px de ancho cabe en un post 4:5 (1080×1350) o en un reel 9:16 (1080×1920)
y deja espacio para texto arriba o abajo. Para Instagram se usa el `.mp4`.
