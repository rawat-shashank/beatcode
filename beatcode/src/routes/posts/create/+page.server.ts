// +page.server.ts
import type { Post } from '$lib/types';
import type { Actions } from './$types';

async function createPost(postData: any): Promise<Post | null> {
	try {
		const res = await fetch('http://localhost:8000/posts', {
			// Or your actual API URL
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(postData)
		});

		if (!res.ok) {
			console.error(`Failed to create post: ${res.status} - ${await res.text()}`);
			return null;
		}

		return await res.json();
	} catch (error) {
		console.error('Error creating post:', error);
		return null;
	}
}

export const actions: Actions = {
	create: async ({ request }) => {
		const data = await request.formData(); // Get form data

		const newPost = {
			number: data.get('number'),
			title: data.get('title'),
			url: data.get('url'),
			description: data.get('description'),
			difficulty: data.get('difficulty'),
			input_constraint: data.get('input_constraint'),
			examples: data.get('examples'),
			topics: data.get('topics')
		};

		console.log(data);

		const createdPost = await createPost(newPost);

		if (createdPost) {
			return {
				status: 201, // Created
				body: { message: 'Post created', post: createdPost }
			};
		} else {
			return {
				status: 500,
				body: { message: 'Failed to create post' }
			};
		}
	}
};

export const prerender = false;
