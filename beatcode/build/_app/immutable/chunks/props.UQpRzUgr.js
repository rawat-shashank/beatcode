import{a8 as N,a9 as $,aa as z,W as m,ab as W,ac as y,ad as D,ae as c,e as P,O as F,af as J,g as Q,C as X,B as k,h as C,A as p,ag as ee,H as ae,E as re,x as te,F as M,K as Y,M as j,N as U,G as ne,ah as ie,ai as fe,aj as se,ak as ue,a1 as G,l as le,al as _e,am as ve,an as de,d as H,j as K,ao as ce,ap as oe,aq as be,ar as ge,as as he,V as ye}from"./runtime.CarZVSJz.js";function w(n,u=null,g){if(typeof n!="object"||n===null||N in n)return n;const v=Q(n);if(v!==$&&v!==z)return n;var i=new Map,_=X(n),o=m(0);_&&i.set("length",m(n.length));var h;return new Proxy(n,{defineProperty(f,e,a){(!("value"in a)||a.configurable===!1||a.enumerable===!1||a.writable===!1)&&W();var t=i.get(e);return t===void 0?(t=m(a.value),i.set(e,t)):y(t,w(a.value,h)),!0},deleteProperty(f,e){var a=i.get(e);if(a===void 0)e in f&&i.set(e,m(c));else{if(_&&typeof e=="string"){var t=i.get("length"),r=Number(e);Number.isInteger(r)&&r<t.v&&y(t,r)}y(a,c),V(o)}return!0},get(f,e,a){var d;if(e===N)return n;var t=i.get(e),r=e in f;if(t===void 0&&(!r||(d=D(f,e))!=null&&d.writable)&&(t=m(w(r?f[e]:c,h)),i.set(e,t)),t!==void 0){var s=P(t);return s===c?void 0:s}return Reflect.get(f,e,a)},getOwnPropertyDescriptor(f,e){var a=Reflect.getOwnPropertyDescriptor(f,e);if(a&&"value"in a){var t=i.get(e);t&&(a.value=P(t))}else if(a===void 0){var r=i.get(e),s=r==null?void 0:r.v;if(r!==void 0&&s!==c)return{enumerable:!0,configurable:!0,value:s,writable:!0}}return a},has(f,e){var s;if(e===N)return!0;var a=i.get(e),t=a!==void 0&&a.v!==c||Reflect.has(f,e);if(a!==void 0||F!==null&&(!t||(s=D(f,e))!=null&&s.writable)){a===void 0&&(a=m(t?w(f[e],h):c),i.set(e,a));var r=P(a);if(r===c)return!1}return t},set(f,e,a,t){var R;var r=i.get(e),s=e in f;if(_&&e==="length")for(var d=a;d<r.v;d+=1){var E=i.get(d+"");E!==void 0?y(E,c):d in f&&(E=m(c),i.set(d+"",E))}r===void 0?(!s||(R=D(f,e))!=null&&R.writable)&&(r=m(void 0),y(r,w(a,h)),i.set(e,r)):(s=r.v!==c,y(r,w(a,h)));var b=Reflect.getOwnPropertyDescriptor(f,e);if(b!=null&&b.set&&b.set.call(t,a),!s){if(_&&typeof e=="string"){var S=i.get("length"),O=Number(e);Number.isInteger(O)&&O>=S.v&&y(S,O+1)}V(o)}return!0},ownKeys(f){P(o);var e=Reflect.ownKeys(f).filter(r=>{var s=i.get(r);return s===void 0||s.v!==c});for(var[a,t]of i)t.v!==c&&!(a in f)&&e.push(a);return e},setPrototypeOf(){J()}})}function V(n,u=1){y(n,n.v+u)}function Ee(n,u,g=!1){C&&p();var v=n,i=null,_=null,o=c,h=g?ee:0,f=!1;const e=(t,r=!0)=>{f=!0,a(r,t)},a=(t,r)=>{if(o===(o=t))return;let s=!1;if(C){const d=v.data===ae;!!o===d&&(v=re(),te(v),M(!1),s=!0)}o?(i?Y(i):r&&(i=j(()=>r(v))),_&&U(_,()=>{_=null})):(_?Y(_):r&&(_=j(()=>r(v))),i&&U(i,()=>{i=null})),s&&M(!0)};k(()=>{f=!1,u(e),f||a(null,null)},h),C&&(v=ne)}let T=!1;function Pe(n){var u=T;try{return T=!1,[n(),T]}finally{T=u}}function Z(n){for(var u=F,g=F;u!==null&&!(u.f&(se|ue));)u=u.parent;try{return G(u),n()}finally{G(g)}}function Re(n,u,g,v){var B;var i=(g&ge)!==0,_=!le||(g&_e)!==0,o=(g&ve)!==0,h=(g&he)!==0,f=!1,e;o?[e,f]=Pe(()=>n[u]):e=n[u];var a=N in n||de in n,t=((B=D(n,u))==null?void 0:B.set)??(a&&o&&u in n?l=>n[u]=l:void 0),r=v,s=!0,d=!1,E=()=>(d=!0,s&&(s=!1,h?r=H(v):r=v),r);e===void 0&&v!==void 0&&(t&&_&&ie(),e=E(),t&&t(e));var b;if(_)b=()=>{var l=n[u];return l===void 0?E():(s=!0,d=!1,l)};else{var S=Z(()=>(i?K:ce)(()=>n[u]));S.f|=fe,b=()=>{var l=P(S);return l!==void 0&&(r=void 0),l===void 0?r:l}}if(!(g&oe))return b;if(t){var O=n.$$legacy;return function(l,I){return arguments.length>0?((!_||!I||O||f)&&t(I?b():l),l):b()}}var R=!1,q=!1,x=ye(e),A=Z(()=>K(()=>{var l=b(),I=P(x);return R?(R=!1,q=!0,I):(q=!1,x.v=l)}));return i||(A.equals=be),function(l,I){if(arguments.length>0){const L=I?P(A):_&&o?w(l):l;return A.equals(L)||(R=!0,y(x,L),d&&r!==void 0&&(r=L),H(()=>P(A))),l}return P(A)}}export{w as a,Ee as i,Re as p};