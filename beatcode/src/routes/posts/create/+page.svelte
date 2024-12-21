<script lang="ts">
	import type { Post } from '$lib/types';
	import { goto } from '$app/navigation';

	let title = '';
	let subtitle = '';
	let content = '';
	let base64Image = '';
	let error: string | null = null;
	let loading = false;

	async function handleSubmit() {
		loading = true;
		error = null;

		const newPost: Omit<Post, 'id'> = {
			title,
			subtitle,
			content,
			base64_image: base64Image
		};

		try {
			const response = await fetch('http://localhost:8000/posts/', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(newPost)
			});

			if (!response.ok) {
				const errorData = await response.json();
				error = errorData.detail || `HTTP error ${response.status}`;
				throw new Error(error);
			}

			goto('/'); // Redirect to the home page after successful creation
		} catch (err) {
			console.error('Error creating post:', err);
			error = 'An error occurred while creating the post.';
		} finally {
			loading = false;
		}
	}

	function handleFileChange(event: Event) {
		const input = event.target as HTMLInputElement;
		const file = input.files?.[0];

		if (file) {
			const reader = new FileReader();
			reader.onloadend = () => {
				base64Image = reader.result?.toString().split(',')[1] || '';
			};
			reader.readAsDataURL(file);
		}
	}
</script>

<h1>Create New Post</h1>

{#if error}
	<p style="color: red;">{error}</p>
{/if}

<form on:submit|preventDefault={handleSubmit}>
	<label for="title">Title:</label><br />
	<input class="border-2" type="text" id="title" bind:value={title} required /><br /><br />

	<label for="subtitle">Subtitle:</label><br />
	<input class="border-2" type="text" id="subtitle" bind:value={subtitle} /><br /><br />

	<label for="content">Content:</label><br />
	<textarea id="content" bind:value={content}></textarea><br /><br />

	<label for="image">Image:</label><br />
	<input class="border-2" type="file" id="image" accept="image/*" on:change={handleFileChange} /><br
	/><br />

	<button type="submit" disabled={loading}>
		{#if loading}Creating...{:else}Create Post{/if}
	</button>
</form>
