import type { PageServerLoad } from './$types';
import type { Post } from '$lib/types'; // Make sure this path is correct

export const load: PageServerLoad = async ({ params }) => {
    try {
        const res = await fetch(`http://localhost:8000/posts/${params.id}`); // Your API endpoint
        if (!res.ok) {
            const errorText = await res.text(); // Get error text from response
            console.error(`Error fetching post ${params.id}: ${res.status} - ${errorText}`);
            return {
                status: res.status, // Return the actual status code
                error: new Error(`Failed to fetch post: ${res.status} - ${errorText}`)
            };

        }
        const post: Post = await res.json();
        return { post };
    } catch (error) {
        console.error(`Error fetching post ${params.id}:`, error);
        return {
            status: 500, // Or another appropriate status code
            error: new Error("An unexpected error occurred")
        };
    }
};

export const prerender = true;