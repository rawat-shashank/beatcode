import type { PageServerLoad } from './$types';
import type { Post } from '$lib/types';

export const load: PageServerLoad = async ({ params, fetch }) => {
    const { id } = params;

    try {
        const res = await fetch(`http://localhost:8000/posts/${id}`);
        if (!res.ok) {
            const errorText = await res.text();
            throw new Error(`Failed to fetch post: ${res.status} - ${errorText}`);
        }
        const post: Post = await res.json();
        return { post };
    } catch (error) {
        console.error("Error fetching post:", error);
        return {
            status: 404, // Or 500 if it's a server error
            error: new Error("Post not found")
        };
    }
};