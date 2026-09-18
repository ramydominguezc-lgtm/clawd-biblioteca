# Clawd con confeti

Réplica de "Confetti Claude" (Codrops, mayo 2026; demo en
ayotomcs.me/claude-mascot). Clawd pisotea de un lado a otro y lanza dos ráfagas
de confeti, una con cada brazo.

8 cuadros · 125 ms cada uno · ciclo de 1 s · lienzo 40×36 U · 640×576 px.

## De dónde salió

No se recortó ningún video. Se extrajo el componente SVG de la demo, se ejecutó
su línea de tiempo GSAP en Node y cada dibujo se transcribió a la retícula de
Clawd (U = 16/3 px, la misma de la caminata). Receta:
`Animaciones - Clawd/scripts/clawd_confeti.py`.

## Diferencias deliberadas con la demo

| Demo | Aquí | Por qué |
|---|---|---|
| El ciclo dura 0.875 s y el cuadro 8 nunca se ve | 8 cuadros, 1 s | Error de GSAP en la demo; el artículo describe 8 cuadros a 125 ms |
| Cuadros levantados corridos 2–4 px (<1U) | Pies fijos en la retícula | En pixel art no hay media celda |
| Cuerpo `#DD775B` | `#d97757` | Hex canónico de Clawd |
| Confeti de 5 px contra un cuerpo de 5.33 px | 1 celda = 1U | Una sola retícula para todo |

## Verificación

- IoU de forma del personaje contra la demo, alineado: 0.944–0.961. El desfase
  sin alinear es exactamente el corrimiento de 2–4 px de la demo.
- `SVG infieles: ninguno`.
- GIF, WebP y MP4 decodificados y revisados cuadro por cuadro.
- `comparativa-demo-vs-reconstruccion.png`: arriba la demo, abajo la réplica.

## Qué usar

| Destino | Archivo |
|---|---|
| Web | `clawd-confeti.webp` |
| WhatsApp, Notion | `clawd-confeti.gif` (crema) · `-transparente.gif` |
| Reel, story, post | `clawd-confeti.mp4` (24 fps) |
| Canvas, Claude Design | `clawd-confeti-bloque.html` |
| Sitio propio | `clawd-confeti-hoja.png` + `.css` |

El GIF solo admite centésimas: guarda los cuadros alternando 120 y 130 ms para
que el ciclo dure exactamente 1.000 s.
