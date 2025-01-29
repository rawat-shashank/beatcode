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
	<div class="grid w-full grid-cols-[1fr_auto] gap-4">
		<a
			href="{base}/posts/create"
			class="mr-5 justify-self-end font-semibold text-indigo-600 hover:text-indigo-800 dark:text-indigo-400 dark:hover:text-indigo-200"
			>Create Post</a
		>
		<div class="col-span-2 w-full">
			<PostsListing postsListingData={data.posts} />
		</div>
	</div>
{:else}
	<p>Loading posts...</p>
{/if}

<style>
	/* ... (styles from previous responses) */
</style>
