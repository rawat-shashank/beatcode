<script lang="ts">
	import type { Post } from '$lib/types';
	import { goto } from '$app/navigation';
  
	let title = '';
	let description = '';
	let url = '';
	let inputConstraints: string[] = [];
	let examples: { input: any; output: any; explanation?: string }[] = [];
	let exampleInput = '';
	let exampleOutput = '';
	let exampleExplanation = '';
	let currentExampleIndex = -1;
	let error: string | null = null;
	let loading = false;
  
	function addExample() {
	  examples.push({
		input: exampleInput,
		output: exampleOutput,
		explanation: exampleExplanation,
	  });
	  exampleInput = '';
	  exampleOutput = '';
	  exampleExplanation = '';
	}
  
	function editExample(index: number) {
	  currentExampleIndex = index;
	  const example = examples[index];
	  exampleInput = example.input;
	  exampleOutput = example.output;
	  exampleExplanation = example.explanation || '';
	}
  
	function saveExample() {
	  if (currentExampleIndex !== -1) {
		examples[currentExampleIndex] = {
		  input: exampleInput,
		  output: exampleOutput,
		  explanation: exampleExplanation,
		};
		currentExampleIndex = -1;
		exampleInput = '';
		exampleOutput = '';
		exampleExplanation = '';
	  }
	}
  
	function deleteExample(index: number) {
	  examples = examples.filter((_, i) => i !== index);
	}
  
	async function handleSubmit() {
	  loading = true;
	  error = null;
  
	  const newPost: Omit<Post, 'id'> = {
		title,
		description,
		url,
		input_constraints: inputConstraints,
		examples,
	  };
  
	  try {
		const response = await fetch('http://localhost:8000/posts/', {
		  method: 'POST',
		  headers: {
			'Content-Type': 'application/json',
		  },
		  body: JSON.stringify(newPost),
		});
  
		if (!response.ok) {
		  const errorData = await response.json();
		  error = errorData.detail || `HTTP error ${response.status}`;
		  throw new Error(error);
		}
  
		goto('/posts'); // Redirect to posts list
	  } catch (err) {
		console.error('Error creating post:', err);
		error = 'An error occurred while creating the post.';
	  } finally {
		loading = false;
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

	<label for="description">Description:</label><br />
	<textarea id="description" bind:value={description}></textarea><br /><br />

	<label for="url">URL:</label><br />
	<input class="border-2" type="url" id="url" bind:value={url} required /><br /><br />

	<fieldset>
		<legend>Input Constraints</legend>
		{#each inputConstraints as constraint, index}
			<div class="flex">
				<input type="text" bind:value={inputConstraints[index]} />
				<button
					type="button"
					on:click={() => (inputConstraints = inputConstraints.filter((_, i) => i !== index))}
					>-</button
				>
			</div>
		{/each}
		<button type="button" on:click={() => (inputConstraints = [...inputConstraints, ''])}
			>Add Constraint</button
		>
	</fieldset>
	<br />
	<fieldset>
		<legend>Examples</legend>
		{#each examples as example, index}
			<div class="mb-2 border p-2">
				<p><b>Example {index + 1}</b></p>
				<p>Input: {JSON.stringify(example.input)}</p>
				<p>Output: {JSON.stringify(example.output)}</p>
				{#if example.explanation}<p>Explanation: {example.explanation}</p>{/if}
				<button type="button" on:click={() => editExample(index)}>Edit</button>
				<button type="button" on:click={() => deleteExample(index)}>Delete</button>
			</div>
		{/each}
		<div class="border p-2">
			<label for="exampleInput">Example Input:</label><br />
			<input type="text" id="exampleInput" bind:value={exampleInput} /><br /><br />

			<label for="exampleOutput">Example Output:</label><br />
			<input type="text" id="exampleOutput" bind:value={exampleOutput} /><br /><br />

			<label for="exampleExplanation">Example Explanation:</label><br />
			<textarea id="exampleExplanation" bind:value={exampleExplanation}></textarea><br /><br />

			{#if currentExampleIndex !== -1}
				<button type="button" on:click={saveExample}>Save Example</button>
			{:else}
				<button type="button" on:click={addExample}>Add Example</button>
			{/if}
		</div>
	</fieldset>

	<button type="submit" disabled={loading}>
		{#if loading}Creating...{:else}Create Post{/if}
	</button>
</form>
