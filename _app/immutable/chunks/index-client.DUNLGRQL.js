import{am as o,a9 as t,an as c,ae as a}from"./runtime.DFhORxxn.js";function i(n){{const e=new Error(`lifecycle_outside_component
\`${n}(...)\` can only be used during component initialisation
https://svelte.dev/e/lifecycle_outside_component`);throw e.name="Svelte error",e}}function u(n){o===null&&i("onMount"),t&&o.l!==null?l(o).m.push(n):c(()=>{const e=a(n);if(typeof e=="function")return e})}function l(n){var e=n.l;return e.u??(e.u={a:[],b:[],m:[]})}export{u as o};
