# Clawd de paseo mirando arriba

Variante de `paseo/`: el mismo paseo, pero cada vez que el original baja la
vista, este la sube. Recorrido, ritmo, brinco, caminata y salto son idénticos.

101 cuadros únicos · 20 ms (50 fps) · ciclo de 11.52 s · 1008×544 px.
Receta: `Animaciones - Clawd/scripts/clawd_paseo_arriba.py`.

## Qué se cambió

No se redibujó nada. En la línea de tiempo GSAP del componente original solo se
tocaron los cuatro movimientos de los ojos hacia abajo:

| Momento | Original | Aquí |
|---|---|---|
| Inclinado mirando al lado | ojos `y: 12` | `y: -5` |
| Mirando abajo (dos veces) | ojos `y: 23` | `y: -9` |

Con `-9` los ojos quedan pegados al borde de arriba del cuerpo; más arriba se
saldrían de él. El componente modificado está en
`_fuentes/codrops-ayotomcs/componente-630665-mirando-arriba.js`, y de ahí salió
por el mismo proceso que `paseo/` (ver su `LEEME.md`).

## Verificación

- IoU de silueta contra el componente modificado corrido en Chrome: mínimo
  0.876, media 0.918.
- `SVG infieles: ninguno`. GIF y MP4 de 11.52 s.
- `comparativa-demo-vs-reconstruccion.png`.

Es una animación nueva, no una réplica: no existe un original de Anthropic que
mire hacia arriba.
