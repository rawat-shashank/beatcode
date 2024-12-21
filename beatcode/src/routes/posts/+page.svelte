<script lang="ts">
	import type { Post } from '$lib/types';
	import { base } from '$app/paths';

	export let data: {
		error: any;
		posts: Post[];
	};
</script>

<h1>Blog Posts</h1>

{#if data.error}
	<p style="color: red;">Error: {data.error.message}</p>
{:else if data.posts}
	<ul>
		{#each data.posts as post}
			<li>
				<a href={`${base}/posts/${post.id}`}>
					<h2>{post.title}</h2>
					{#if post.subtitle}
						<h3>{post.subtitle}</h3>
					{/if}
					{#if post.base64_image}
						<img
							src={`data:image/jpeg;base64,${post.base64_image}`}
							alt={post.title}
							style="max-width: 200px; max-height: 150px;"
						/>
					{/if}
					<p>{post.content?.substring(0, 100)}...</p>
				</a>
			</li>
		{/each}
	</ul>
{:else}
	<p>Loading posts...</p>
{/if}

<style>
	/* ... (styles from previous responses) */
</style>
