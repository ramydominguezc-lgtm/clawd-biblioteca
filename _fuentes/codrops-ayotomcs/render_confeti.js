// Ejecuta el componente React del confeti con un React y un GSAP falsos,
// y escribe un SVG por instante de tiempo (cada 125 ms) para analizarlo.
const fs = require('fs');
const src = fs.readFileSync(__dirname + '/confeti_modulo.js', 'utf8');
const cuerpo = src.slice(src.indexOf('t=>') + 3);

// --- React falso: jsx arma un arbol; los refs apuntan al nodo ---
const jsx = (type, props) => ({ type, props: { ...props } });
const refs = [];
const react = { useRef: (v) => ({ current: v }), useEffect: (fn) => refs.push(fn) };

// --- GSAP falso: guarda los set() de cada timeline ---
const lineas = [];
const gsap = {
  default: {
    timeline: (op) => {
      const tl = { op, sets: [], kill() {} };
      tl.set = (target, vars, time) => { tl.sets.push({ target, vars, time }); return tl; };
      lineas.push(tl);
      return tl;
    },
  },
};
let componente;
const t = {
  i: (id) => (id === 843476 ? { jsx, jsxs: jsx } : id === 271645 ? react : gsap),
  s: (exp) => { componente = exp[1](); },
};
new Function('t', cuerpo)(t);
const arbol = componente();

// conectar refs: cada nodo con ref recibe un objeto "vivo"
function conectar(n) {
  if (!n || typeof n !== 'object') return;
  if (Array.isArray(n)) return n.forEach(conectar);
  if (typeof n.props.ref === 'function') n.props.ref(n);
  else if (n.props.ref) n.props.ref.current = n;
  conectar(n.props.children);
}
conectar(arbol);
refs.forEach((fn) => fn());

const inicial = JSON.parse(JSON.stringify(arbol, (k, v) => (k === 'ref' ? undefined : v)));

const kebab = (k) => (k === 'viewBox' ? k : k.replace(/[A-Z]/g, (m) => '-' + m.toLowerCase()));
function svg(n) {
  if (n == null || n === false) return '';
  if (typeof n !== 'object') return String(n);
  if (Array.isArray(n)) return n.map(svg).join('');
  const { children, ref, className, id, ...p } = n.props;
  const at = Object.entries(p).map(([k, v]) => ` ${kebab(k)}="${v}"`).join('');
  return `<${n.type}${at}>${svg(children)}</${n.type}>`;
}

// estado en el instante T: aplicar los set() que ya pasaron en cada timeline
function estado(T) {
  // restaurar atributos iniciales en todos los nodos
  (function rest(n, ini) {
    if (!n || typeof n !== 'object') return;
    if (Array.isArray(n)) return n.forEach((x, i) => rest(x, ini[i]));
    for (const k of ['display', 'transform']) {
      if (ini.props[k] === undefined) delete n.props[k]; else n.props[k] = ini.props[k];
    }
    rest(n.props.children, ini.props.children);
  })(arbol, inicial);
  for (const tl of lineas) {
    const D = tl.op.delay || 0;
    const L = Math.max(...tl.sets.map((s) => s.time));
    if (T < D - 1e-9) continue;
    const local = L > 0 ? ((T - D) % L + L) % L : 0;
    for (const s of tl.sets) {
      if (s.time <= local + 1e-9) {
        if (s.vars.display) s.target.props.display = s.vars.display;
        if (s.vars.attr) Object.assign(s.target.props, s.vars.attr);
      }
    }
  }
  return svg(arbol);
}

const out = __dirname + '/confeti_svg';
fs.mkdirSync(out, { recursive: true });
console.log('timelines:', lineas.map((l) => ({ op: l.op, n: l.sets.length, L: Math.max(...l.sets.map((s) => s.time)) })));
for (let k = 0; k < 32; k++) {
  const T = k * 0.125;
  fs.writeFileSync(`${out}/t${String(k).padStart(2, '0')}.svg`, estado(T));
}
// cuadros sueltos (todo visible uno por uno) para ver los dibujos
fs.writeFileSync(out + '/arbol.json', JSON.stringify(inicial, null, 1));
