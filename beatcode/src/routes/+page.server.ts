import type { PageServerLoad } from './$types';
import type { Post } from '$lib/types';

export const load: PageServerLoad = async ({ fetch }) => {
    try {
        const res = await fetch('http://localhost:8000/posts'); // Replace with your FastAPI URL
        if (!res.ok) {
            const errorText = await res.text();
            throw new Error(`Failed to fetch posts: ${res.status} - ${errorText}`);
        }
        const posts: Post[] = await res.json();
        return { posts };
    } catch (error) {
        console.error("Error fetching posts:", error);
        return {
            status: 500,
            error: new Error("Failed to load posts")
        };
    }
};