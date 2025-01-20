import type { PageServerLoad } from "./$types";

export const load: PageServerLoad = ({ }) => {
    return {};
};

export const prerender = true;
export const ssr = true;