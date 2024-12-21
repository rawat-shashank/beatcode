import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = ({ }) => {
    return {};
};

export const prerender = true;
export const csr = false;
export const ssr = true;