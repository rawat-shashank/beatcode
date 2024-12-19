<script lang="ts">
	import type { Post } from '$lib/types';
	export let data: {
		error: any;
		posts: Post[];
	};
</script>

<h1>Blog Posts</h1>

{#if data.error}
	<p style="color: red;">Error: {data.error.message}</p>
{:else if data.posts}
	{#each data.posts as post}
		<div>
			<h2>{post.title}</h2>
			{#if post.subtitle}
				<h3>{post.subtitle}</h3>
			{/if}
			{#if post.base64_image}
				<img src={`data:image/jpeg;base64,${post.base64_image}`} alt={post.title} />
			{/if}
			<p>{post.content}</p>
		</div>
	{/each}
{:else}
	<p>Loading posts...</p>
{/if}
