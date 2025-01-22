<script lang="ts">
	import type { Post } from '$lib/types';
	import { base } from '$app/paths';
	import Listing from '../../components/Posts/PostsListing.svelte';
	import PostsListing from '../../components/Posts/PostsListing.svelte';

	export let data: {
		error: any;
		posts: Post[];
	};
</script>

{#if data.error}
	<p style="color: red;">Error: {data.error.message}</p>
{:else if data.posts}
	<PostsListing postsListingData={data.posts} />
	<!-- <ul>
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
	</ul> -->
{:else}
	<p>Loading posts...</p>
{/if}

<style>
	/* ... (styles from previous responses) */
</style>
