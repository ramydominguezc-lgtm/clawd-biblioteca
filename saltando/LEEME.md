# Clawd saltando

Clawd se agacha, salta estirado con los brazos arriba, agita los brazos en el aire
con ojos felices "^ ^", cae, aterriza aplastado, rebota y vuelve al reposo.

13 poses · 83 ms por tiempo · ciclo de 1.74 s (12 tiempos de movimiento + 9 de
pausa) · lienzo 28×31 U · 448×496 px. Receta: `Animaciones - Clawd/scripts/clawd_saltando.py`.

## De dónde salió

Réplica desde video (Parte A del método): `Video - Clawd saltando.mp4`, grabación
de pantalla de 1920×1080 a 30 fps que entregó Ramses el 17/09/2026. Copia de la
fuente, el script de transcripción y las poses en `_fuentes/video-saltando/`.

- **Anclas:** el centro horizontal no se mueve (x = 977 px) y el suelo está en
  y = 872 px.
- **Retícula:** el reposo mide 568 px = 24 U, así que U = 23.67 px. Es la retícula
  canónica, y el reposo salió idéntico celda por celda al `QUIETO` de la caminata.
- **Compás:** los cambios alternan 3 y 2 cuadros de video, o sea 12 fps. Cada ciclo
  son 12 tiempos de movimiento y una pausa de 23 cuadros.
- **Limpieza:** el video trae el ciclo 3 veces. Cada pose es la moda por celda
  de los 3 ciclos, sin el cuadro de transición, y los tres coincidieron en el
  100 % de las celdas.
- **Ojos:** son las celdas oscuras que no se alcanzan desde el borde. Así se
  separan del fondo, que en el video es casi del mismo color.

## Diferencias con el video

| Video | Aquí | Por qué |
|---|---|---|
| Pausa de 23 cuadros (9.2 tiempos): ciclo de 1.77 s | 9 tiempos: 1.74 s | En pixel art el tiempo va entero |
| Naranja comprimido por el códec | `#d97757` | Hex canónico |
| Fondo oscuro | Transparente, o crema en el GIF y el MP4 | Formatos estándar de la biblioteca |

## Verificación

- IoU del naranja contra el video, promedio de los cuadros de cada pose: mínimo
  0.951, media 0.954. Lo que falta es el borde suavizado y comprimido del video.
- `SVG infieles: ninguno`. GIF de 1.74 s y MP4 de 1.75 s.
- `comparativa-video-vs-reconstruccion.png`: las 13 poses, video arriba y réplica abajo.

## Qué usar

| Destino | Archivo |
|---|---|
| Instagram (post, reel, story) | `clawd-saltando.mp4` |
| Web | `clawd-saltando.webp` |
| WhatsApp, Notion | `clawd-saltando.gif` (crema) · `-transparente.gif` |
| Claude Design, artifacts | `clawd-saltando-bloque.html` |
| Sitio propio | `clawd-saltando-hoja.png` + `.css` |

Sobre fondo oscuro, los ojos (`#141413`) se confunden con el fondo en los huecos
entre las patas; el cuerpo se lee bien.
