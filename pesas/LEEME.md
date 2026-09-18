# Clawd con pesas

Réplica de "Gym Claude" (Codrops, mayo 2026; demo en ayotomcs.me/claude-mascot).
Clawd levanta una mancuerna por encima de la cabeza, hace dos repeticiones y la
deja.

30 dibujos únicos · 48 tiempos · ciclo de 7.125 s · lienzo 32×25 U · 512×400 px.
Receta: `Animaciones - Clawd/scripts/clawd_pesas.py`.

## De dónde salió

Del código de la demo, ejecutado con el GSAP real en Chrome (`capturar_gsap.js`)
y pasado a la retícula de Clawd (`transcribir_svg.py`). Los 36 dibujos de la
fuente dan 30 rejillas únicas: algunos dibujos casi iguales colapsan en la
retícula. Las dos pasadas de los dibujos repetidos dieron idéntico.

## Ritmo

85 ms por cuadro; 270 ms arriba del levantamiento (dibujos 6 y 7); 400 ms entre
repeticiones (15 y 21); 1.5 s en el último cuadro.

## Diferencias deliberadas con la demo

| Demo | Aquí | Por qué |
|---|---|---|
| Los 1.5 s finales no se ven: la línea de tiempo acaba cuando aparece el último cuadro | Se sostienen 1.5 s | Es lo que dice el artículo; mismo error de GSAP que el confeti |
| Cuerpo `#DD775B` | `#d97757` | Hex canónico |
| Mancuerna en retícula de 5–6 px | En U (5.33 px) | Una sola retícula; algún borde gana o pierde una celda |

La mancuerna conserva los colores de la demo (`#1A4C81`, `#5D5B56`): no son de
marca, pero son el objeto original.

## Verificación

- IoU de silueta contra la demo (mejor alineación): mínimo 0.937, media 0.951.
- `SVG infieles: ninguno`. GIF 7.12 s, MP4 7.13 s.
- `comparativa-demo-vs-reconstruccion.png`: 15 momentos, demo arriba y réplica abajo.
