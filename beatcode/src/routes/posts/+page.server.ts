import type { Post } from '$lib/types';
import type { PageServerLoad } from '../$types';

async function fetchPosts(): Promise<Post[]> {

    try {
        const res = await fetch('http://localhost:8000/posts');
        if (!res.ok) {
            console.error(`Failed to fetch posts: ${res.status} - ${await res.text()}`);
            return [];
        }
        return await res.json();
    } catch (error) {
        console.error("Error fetching posts:", error);
        return [];
    }
}

export const load: PageServerLoad = async () => {
    const posts = await fetchPosts();
    if (posts.length === 0) {
        return {
            status: 500,
            error: new Error("Failed to load posts")
        };
    }
    return { posts };
};

export const prerender = true; // Essential!