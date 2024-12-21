<script lang="ts">
    import type { Post } from '$lib/types';
    import { error } from '@sveltejs/kit';
    export let data: { post?: Post; error?: Error, status?: number };
    $: if (data.error && data.status === 404) {
        throw error(404, data.error.message); // Throw a 404 error if post not found
    }
</script>

{#if data.post}
    <h1>{data.post.title}</h1>
    {#if data.post.subtitle}
        <h2>{data.post.subtitle}</h2>
    {/if}
    {#if data.post.base64_image}
        <img src={`data:image/jpeg;base64,${data.post.base64_image}`} alt={data.post.title} />
    {/if}
    <p>{data.post.content}</p>
{:else if data.error}
    <p style="color: red;">Error: {data.error.message}</p>
{:else}
    <p>Loading post...</p>
{/if}