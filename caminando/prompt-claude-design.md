# Prompt para Claude Design

Validado en produccion: funciona. Pega todo lo que sigue en el chat de Claude
Design — el bloque de codigo va completo, sin recortar.

La skill `anthro-pic-brand` si carga en Claude Design, asi que los tokens y las
plantillas los resuelve solo. El bloque igual va incrustado aqui, porque una ruta
local no pinta dentro de un navegador.

---

Necesito un post de Instagram en formato 4:5 (1080 × 1350) para ClaudeTec, el
grupo estudiantil de Claude del Tec de Monterrey campus Monterrey.

## Contenido

- **Píldora superior derecha:** ¿Quiénes somos?
- **Titular:** Una comunidad de estudiantes de cualquier carrera que explora y comparte el potencial de la IA.
- **Bajada:** Con Claude y el ecosistema de Anthropic como punto de partida.

## Sistema visual — esto no se negocia

- Fondo crema `#faf9f5`.
- Titular en **Poppins 700**, alineado a la izquierda. Nada centrado.
- Bajada en **Lora regular**, `#7d7b74`.
- Un solo acento: naranja `#d97757`.
- Texto principal `#141413`. Máximo contraste siempre.
- Cero degradados, sombras suaves, glows y esquinas muy redondeadas.
- Márgenes amplios e iguales en los cuatro lados.

## Elemento gráfico

Usa este bloque **tal cual**, sin tocarlo. Es la mascota de la marca, Clawd,
animada caminando.

```html
<div class="clawd-caminando">
<svg viewBox="0 0 364 20" shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">
<g transform="translate(0 0)">
<path fill="#d97757" d="M6 4h16v2h-16zM6 6h2v2h-2zM20 6h2v2h-2zM10 6h8v2h-8zM2 8h24v4h-24zM6 12h16v4h-16zM16 16h2v4h-2zM6 16h2v4h-2zM20 16h2v4h-2zM10 16h2v4h-2z"/>
<path fill="#141413" d="M8 6h2v2h-2zM18 6h2v2h-2z"/>
</g>
<g transform="translate(28 0)">
<path fill="#d97757" d="M6 5h16v3h-16zM6 8h2v1h-2zM20 8h2v1h-2zM11 8h6v1h-6zM2 9h24v4h-24zM6 13h16v4h-16zM16 17h2v3h-2zM6 17h2v3h-2zM20 17h2v3h-2zM10 17h2v3h-2z"/>
<path fill="#141413" d="M8 8h3v1h-3zM17 8h3v1h-3z"/>
</g>
<g transform="translate(56 0)">
<path fill="#d97757" d="M9 3h13v2h-13zM9 5h2v2h-2zM13 5h6v2h-6zM21 5h1v2h-1zM5 7h20v4h-20zM9 11h13v5h-13zM20 16h2v1h-2zM19 17h3v1h-3zM19 18h2v1h-2zM11 16h2v4h-2zM15 16h2v4h-2z"/>
<path fill="#b8654a" d="M6 3h3v4h-3zM2 7h3v4h-3zM6 11h3v5h-3zM6 16h2v1h-2zM6 17h3v1h-3zM7 18h2v1h-2z"/>
<path fill="#141413" d="M19 5h2v2h-2zM11 5h2v2h-2z"/>
</g>
<g transform="translate(84 0)">
<path fill="#d97757" d="M9 4h13v2h-13zM9 6h2v2h-2zM13 6h6v2h-6zM21 6h1v2h-1zM5 8h20v4h-20zM9 12h13v4h-13zM19 16h2v4h-2zM11 16h2v4h-2zM15 16h2v4h-2z"/>
<path fill="#b8654a" d="M6 4h3v4h-3zM2 8h3v4h-3zM6 12h3v4h-3zM7 16h2v4h-2z"/>
<path fill="#141413" d="M19 6h2v2h-2zM11 6h2v2h-2z"/>
</g>
<g transform="translate(112 0)">
<path fill="#d97757" d="M9 5h13v2h-13zM9 7h2v2h-2zM13 7h6v2h-6zM21 7h1v2h-1zM5 9h20v4h-20zM9 13h13v4h-13zM16 17h2v1h-2zM20 17h2v1h-2zM10 17h2v1h-2zM19 18h3v1h-3zM15 18h3v1h-3zM10 18h3v1h-3zM19 19h2v1h-2zM11 19h2v1h-2zM15 19h2v1h-2z"/>
<path fill="#b8654a" d="M6 5h3v4h-3zM2 9h3v4h-3zM6 13h3v4h-3zM6 17h2v1h-2zM6 18h3v1h-3zM7 19h2v1h-2z"/>
<path fill="#141413" d="M19 7h2v2h-2zM11 7h2v2h-2z"/>
</g>
<g transform="translate(140 0)">
<path fill="#d97757" d="M14 3h8v1h-8zM9 4h13v1h-13zM9 5h10v1h-10zM21 5h1v1h-1zM21 6h4v1h-4zM13 6h6v1h-6zM9 6h2v2h-2zM13 7h12v1h-12zM9 8h16v2h-16zM5 10h17v4h-17zM9 14h13v2h-13zM20 16h3v1h-3zM21 17h2v2h-2zM11 16h2v4h-2zM15 16h2v4h-2z"/>
<path fill="#b8654a" d="M6 4h3v6h-3zM2 10h3v4h-3zM6 14h3v2h-3zM7 16h2v4h-2z"/>
<path fill="#141413" d="M19 5h2v2h-2zM11 6h2v2h-2z"/>
</g>
<g transform="translate(168 0)">
<path fill="#d97757" d="M9 3h8v1h-8zM9 4h13v1h-13zM13 5h9v1h-9zM9 5h2v1h-2zM5 6h6v1h-6zM13 6h6v1h-6zM21 6h1v2h-1zM5 7h14v1h-14zM5 8h17v2h-17zM8 10h17v3h-17zM8 13h14v1h-14zM7 14h15v2h-15zM19 16h2v4h-2zM11 16h2v4h-2zM15 16h2v4h-2z"/>
<path fill="#b8654a" d="M6 3h3v3h-3zM2 6h3v4h-3zM6 10h2v4h-2zM22 13h3v1h-3zM5 14h2v2h-2zM4 16h3v1h-3zM4 17h2v2h-2z"/>
<path fill="#141413" d="M11 5h2v2h-2zM19 6h2v2h-2z"/>
</g>
<g transform="translate(196 0)">
<path fill="#d97757" d="M6 5h16v2h-16zM6 7h2v2h-2zM20 7h2v2h-2zM10 7h8v2h-8zM2 9h24v4h-24zM6 13h16v3h-16zM5 16h18v1h-18zM17 17h2v1h-2zM9 17h2v1h-2zM16 18h3v1h-3zM9 18h3v1h-3zM21 17h2v3h-2zM5 17h2v3h-2zM16 19h2v1h-2zM10 19h2v1h-2z"/>
<path fill="#141413" d="M8 7h2v2h-2zM18 7h2v2h-2z"/>
</g>
<g transform="translate(224 0)">
<path fill="#d97757" d="M6 3h13v2h-13zM6 5h1v2h-1zM9 5h6v2h-6zM17 5h2v2h-2zM3 7h20v4h-20zM6 11h13v5h-13zM6 16h2v1h-2zM6 17h3v1h-3zM7 18h2v1h-2zM15 16h2v4h-2zM11 16h2v4h-2z"/>
<path fill="#b8654a" d="M19 3h3v4h-3zM23 7h3v4h-3zM19 11h3v5h-3zM20 16h2v1h-2zM19 17h3v1h-3zM19 18h2v1h-2z"/>
<path fill="#141413" d="M15 5h2v2h-2zM7 5h2v2h-2z"/>
</g>
<g transform="translate(252 0)">
<path fill="#d97757" d="M6 4h13v2h-13zM6 6h1v2h-1zM9 6h6v2h-6zM17 6h2v2h-2zM3 8h20v4h-20zM6 12h13v4h-13zM11 16h2v4h-2zM15 16h2v4h-2zM7 16h2v4h-2z"/>
<path fill="#b8654a" d="M19 4h3v4h-3zM23 8h3v4h-3zM19 12h3v4h-3zM19 16h2v4h-2z"/>
<path fill="#141413" d="M15 6h2v2h-2zM7 6h2v2h-2z"/>
</g>
<g transform="translate(280 0)">
<path fill="#d97757" d="M6 5h13v2h-13zM6 7h1v2h-1zM9 7h6v2h-6zM17 7h2v2h-2zM3 9h20v4h-20zM6 13h13v4h-13zM16 17h2v1h-2zM6 17h2v1h-2zM10 17h2v1h-2zM6 18h3v1h-3zM15 18h3v1h-3zM10 18h3v1h-3zM11 19h2v1h-2zM15 19h2v1h-2zM7 19h2v1h-2z"/>
<path fill="#b8654a" d="M19 5h3v4h-3zM23 9h3v4h-3zM19 13h3v4h-3zM20 17h2v1h-2zM19 18h3v1h-3zM19 19h2v1h-2z"/>
<path fill="#141413" d="M15 7h2v2h-2zM7 7h2v2h-2z"/>
</g>
<g transform="translate(308 0)">
<path fill="#d97757" d="M6 3h8v1h-8zM6 4h13v1h-13zM9 5h10v1h-10zM6 5h1v1h-1zM9 6h6v1h-6zM3 6h4v1h-4zM17 6h2v2h-2zM3 7h12v1h-12zM3 8h16v2h-16zM6 10h17v4h-17zM6 14h13v2h-13zM5 16h3v1h-3zM5 17h2v2h-2zM11 16h2v4h-2zM15 16h2v4h-2z"/>
<path fill="#b8654a" d="M19 4h3v6h-3zM23 10h3v4h-3zM19 14h3v2h-3zM19 16h2v4h-2z"/>
<path fill="#141413" d="M7 5h2v2h-2zM15 6h2v2h-2z"/>
</g>
<g transform="translate(336 0)">
<path fill="#d97757" d="M11 3h8v1h-8zM6 4h13v1h-13zM17 5h2v1h-2zM6 5h9v1h-9zM9 6h6v1h-6zM17 6h6v1h-6zM6 6h1v2h-1zM9 7h14v1h-14zM6 8h17v2h-17zM3 10h17v3h-17zM6 13h14v1h-14zM6 14h15v2h-15zM11 16h2v4h-2zM15 16h2v4h-2zM7 16h2v4h-2z"/>
<path fill="#b8654a" d="M19 3h3v3h-3zM23 6h3v4h-3zM20 10h2v4h-2zM3 13h3v1h-3zM21 14h2v2h-2zM21 16h3v1h-3zM22 17h2v2h-2z"/>
<path fill="#141413" d="M15 5h2v2h-2zM7 6h2v2h-2z"/>
</g>
</svg>
</div>
<style>
.clawd-caminando{width:280px;aspect-ratio:28/20;overflow:hidden;position:relative}
.clawd-caminando svg{position:absolute;height:100%;width:auto;
  animation:clawd-caminando 2.64s step-end infinite}
@keyframes clawd-caminando{0.000%{transform:translateX(-0.0000%)}15.152%{transform:translateX(-7.6923%)}18.182%{transform:translateX(-15.3846%)}21.212%{transform:translateX(-23.0769%)}24.242%{transform:translateX(-30.7692%)}30.303%{transform:translateX(-38.4615%)}36.364%{transform:translateX(-30.7692%)}42.424%{transform:translateX(-46.1538%)}48.485%{transform:translateX(-30.7692%)}54.545%{transform:translateX(-15.3846%)}60.606%{transform:translateX(-53.8462%)}66.667%{transform:translateX(-61.5385%)}69.697%{transform:translateX(-69.2308%)}72.727%{transform:translateX(-76.9231%)}78.788%{transform:translateX(-84.6154%)}84.848%{transform:translateX(-76.9231%)}90.909%{transform:translateX(-92.3077%)}96.970%{transform:translateX(-76.9231%)}}
</style>
```

### Reglas del bloque

1. **No redibujes el SVG ni cambies un solo `path`.** Es pixel art medido; el
   dibujo está en una retícula exacta y cualquier retoque lo rompe.
2. **No le pongas contorno, sombra, borde ni filtro.** Va limpio sobre el fondo.
3. **Nunca sobre fondo naranja.** Clawd es naranja y desaparece.
4. Para escalarlo, cambia solo el `width` de `.clawd-caminando`. Conserva
   `aspect-ratio` y `overflow:hidden` — son lo que hace que la animación
   funcione.
5. Es el **único** elemento gráfico de la pieza. No agregues otro.
6. No cambies los tiempos de `@keyframes`. Las duraciones son desiguales a
   propósito: ese es el ritmo de la caminata.

## Composición

Clawd va en la mitad inferior, apoyado sobre una línea imaginaria de suelo, con
aire alrededor. El titular arriba a la izquierda, la píldora arriba a la
derecha, la bajada debajo del titular. Que se lea claro en miniatura.

Evita que la composición quede plana. Si hace falta, mete contraste de fondo y
figura: un bloque de color a sangre de un lado al otro con la tarjeta encima, o
la mitad inferior en un tono distinto — pero recuerda que Clawd no puede quedar
sobre naranja.

## Al terminar

Exporta como HTML autónomo y también compárteme el URL en vivo. En PDF y PPTX la
animación se congela, así que esos formatos solo sirven si el destino es
impreso.
