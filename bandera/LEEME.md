# Clawd con bandera

Réplica de "The Flag Waver" (Codrops, mayo 2026; demo en ayotomcs.me/claude-mascot).
Clawd ondea una bandera a cuadros; el cuerpo se mece al revés que la tela y los
pies no se mueven. Reemplaza a la bandera anterior, borrada por mal hecha.

Receta: `Animaciones - Clawd/scripts/clawd_bandera.py`. Lienzo 34×31 U · 544×496 px.

| Archivo | Qué es | Para |
|---|---|---|
| `clawd-bandera.*` | Solo el bucle: 9 cuadros × 70 ms = 0.63 s | GIF, web, todo lo que se repite |
| `clawd-bandera-con-subida.*` | La tela sube una vez + 6 vueltas = 3.99 s | Video (reel, story) |

## De dónde salió

Del código de la demo (módulo 4030), con el GSAP real. Se armó **por piezas**:
patas de abajo (fijas), cuerpo con ojos "^ ^", mano izquierda, mano derecha y
12 telas. Cada pieza se transcribió una vez en reposo y se mueve en celdas
enteras según los valores de la demo:

- balanceo del cuerpo `[0,0,-5,-5,0,4,4,4,0,0,-5,-5]` px → `[0,0,-1,-1,0,1,1,1,0,0,-1,-1]` celdas
- mano `[0,-6,-12,-14,-8,-2,0,0,-4,-10,-16,-18]` px → `[0,-1,-2,-3,-2,0,0,0,-1,-2,-3,-3]` celdas
- mano izquierda baja 4 px (1 celda) en los cuadros del balanceo a la izquierda

## Diferencias deliberadas con la demo

| Demo | Aquí | Por qué |
|---|---|---|
| Desplazamientos de 2–18 px | Redondeados a celdas enteras | Transcribir cuadro por cuadro dejaba el cuerpo de 15 o 16 celdas según el cuadro |
| Tela en retícula de 5 px sobre un cuerpo de 5.33 px | Tela de 1 celda = 1U, anclada al asta | Muestrearla en U hacía muaré en el damero |
| Una pata a media celda | Las 4 patas iguales | En la fuente son 4 rectángulos idénticos de 11 px |

## Verificación

- IoU de silueta contra la demo: mínimo 0.889, media 0.907. Queda más bajo que
  en las demás porque la tela es 6.7 % más grande (5 px → 5.33 px por celda);
  forma y movimiento coinciden cuadro por cuadro en la comparativa.
- `SVG infieles: ninguno` en las dos versiones. GIF y MP4 duran exactamente 0.63 s y 3.99 s.
