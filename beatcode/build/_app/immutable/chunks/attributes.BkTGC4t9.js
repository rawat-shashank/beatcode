import{j as d,q as u,L as h,k as v,n as g,o as p}from"./runtime.DFhORxxn.js";import{b as l}from"./render.B2rDNRxt.js";function M(r){if(d){var s=!1,e=()=>{if(!s){if(s=!0,r.hasAttribute("value")){var o=r.value;n(r,"value",null),r.value=o}if(r.hasAttribute("checked")){var _=r.checked;n(r,"checked",null),r.checked=_}}};r.__on_r=e,u(e),l()}}function n(r,s,e,o){var _=r.__attributes??(r.__attributes={});if(d&&(_[s]=r.getAttribute(s),s==="src"||s==="srcset"||s==="href"&&r.nodeName==="LINK")){L(r,s,e??"");return}_[s]!==(_[s]=e)&&(s==="style"&&"__styles"in r&&(r.__styles={}),s==="loading"&&(r[h]=e),e==null?r.removeAttribute(s):typeof e!="string"&&y(r).includes(s)?r[s]=e:r.setAttribute(s,e))}var a=new Map;function y(r){var s=a.get(r.nodeName);if(s)return s;a.set(r.nodeName,s=[]);for(var e,o=r,_=Element.prototype;_!==o;){e=p(o);for(var t in e)e[t].set&&s.push(t);o=v(o)}return s}function L(r,s,e){s==="srcset"&&A(r,e)||i(r.getAttribute(s)??"",e)||g(s,r.outerHTML.replace(r.innerHTML,r.innerHTML&&"..."),String(e))}function i(r,s){return r===s?!0:new URL(r,document.baseURI).href===new URL(s,document.baseURI).href}function c(r){return r.split(",").map(s=>s.trim().split(" ").filter(Boolean))}function A(r,s){var e=c(r.srcset),o=c(s);return o.length===e.length&&o.every(([_,t],f)=>t===e[f][1]&&(i(e[f][0],_)||i(_,e[f][0])))}export{M as r,n as s};
