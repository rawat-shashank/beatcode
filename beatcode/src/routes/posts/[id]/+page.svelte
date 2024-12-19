<script lang="ts">
	import type { PageData } from './$types';
	import type { Post } from '$lib/types';

	export let data: PageData;

	$: post = data.post;
</script>

{#if post}
	<h1>{post.title}</h1>
	{#if post.subtitle}
		<h2>{post.subtitle}</h2>
	{/if}
	{#if post.base64_image}
		<img src={`data:image/jpeg;base64,${post.base64_image}`} alt={post.title} />
	{/if}
	<p>{post.content}</p>
{:else}
	<p>Loading post...</p>
{/if}
