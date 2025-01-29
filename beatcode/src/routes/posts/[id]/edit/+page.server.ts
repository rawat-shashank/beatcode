import { error } from '@sveltejs/kit';

export async function load({ params }) {
	const post_id = params.id;
	try {
		// Fetch product data using post_id
		const response = await fetch(`http://localhost:8000/posts/${post_id}`, {
			method: 'GET'
		});
		if (!response.ok) {
			throw error(response.status, 'Could not find post');
		}
		const post = await response.json();
		return { post, post_id };
	} catch (err) {
		throw error(500, 'Could not load post');
	}
}
