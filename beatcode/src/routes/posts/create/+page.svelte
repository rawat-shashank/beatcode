<script lang="ts">
	import { themes } from '$lib/theme/themes';
	import { currentTheme } from '$lib/theme/ThemeManager';
	import Dropdown from '$components/Dropdown.svelte';
	import { Difficulty } from '$lib/types.js';
	import { isValidURL } from '$lib';

	$: theme = themes[$currentTheme] || themes.default;

	type CreatePostType = {
		number: string;
		title: string;
		url: string;
		description: string;
		difficulty: Difficulty;
		input_constraint: string[];
		examples: string[];
		topics: number[];
	};

	interface PostFormErrors {
		number?: string;
		title?: string;
		url?: string;
		description?: string;
		difficulty?: string;
		input_constraint?: string[];
		examples?: string[];
		topics?: number[];
	}

	const initialData: CreatePostType = {
		number: '',
		title: '',
		url: '',
		description: '',
		difficulty: Difficulty.Easy,
		input_constraint: [],
		examples: [],
		topics: []
	};

	let loading = false;
	let formData: CreatePostType = { ...initialData };
	let errors: PostFormErrors = {};

	const handleSubmit = async (event: Event) => {
		event.preventDefault();
		errors = {};

		if (!formData.number.trim()) {
			errors.number = 'Number is required.';
		} else if (isNaN(Number(formData.number))) {
			errors.number = 'Number must be a valid number.';
		} else if (Number(formData.number) < 0) {
			errors.number = 'Number must be positive.';
		}

		if (!formData.title.trim()) {
			errors.title = 'Title is required.';
		} else if (formData.title.length < 3) {
			errors.title = 'Title must be at least 3 characters.';
		}

		if (!formData.url.trim()) {
			errors.url = 'URL is required.';
		} else if (!isValidURL(formData.url)) {
			errors.url = 'Invalid URL.';
		}

		if (!formData.description.trim()) {
			errors.description = 'Description is required.';
		}

		if (Object.keys(errors).length > 0) {
			return;
		}

		loading = true;
		try {
			const response = await fetch('http://localhost:8000/posts', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(formData)
			});

			if (!response.ok) {
				const errorData = await response.json();
				console.error('API Error', errorData);
			} else {
				formData = { ...initialData }; // Reset the form after successful submission
			}
		} catch (error) {
			console.error('Fetch error:', error);
		} finally {
			loading = false;
		}
	};
</script>

<div class="grid grid-cols-[1fr_auto] gap-4">
	<button
		on:click={() => history.back()}
		class="mr-5 justify-self-end font-semibold text-indigo-600 hover:text-indigo-800 dark:text-indigo-400 dark:hover:text-indigo-200"
		>Back</button
	>

	<div class="col-span-2">
		<form on:submit={handleSubmit}>
			<div class="grid grid-cols-[3fr_9fr] gap-4">
				<div>
					<label for="num" class="block text-sm font-medium {theme.text}">Number:</label>
					<input
						type="text"
						id="num"
						name="num"
						bind:value={formData.number}
						class:border-red-500={errors?.number}
						class="mt-1 block w-full rounded-md border border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
					/>
					{#if errors?.number}<span class="mt-1 text-sm text-red-500">{errors.number}</span>{/if}
				</div>
				<div>
					<label for="title" class="block text-sm font-medium {theme.text}">Title:</label>
					<input
						type="text"
						id="title"
						name="title"
						bind:value={formData.title}
						class:border-red-500={errors?.title}
						class="mt-1 block w-full rounded-md border border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
					/>
					{#if errors?.title}<span class="mt-1 text-sm text-red-500">{errors.title}</span>{/if}
				</div>
			</div>

			<div>
				<label for="url" class="block text-sm font-medium {theme.text} ">URL:</label>
				<input
					type="url"
					id="url"
					name="url"
					bind:value={formData.url}
					class:border-red-500={errors?.url}
					class="mt-1 block w-full rounded-md border border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
				/>
				{#if errors?.url}<span class="mt-1 text-sm text-red-500">{errors.url}</span>{/if}
			</div>

			<div class="grid grid-cols-2 gap-4">
				<div class="min-h-full">
					<label for="description" class="block text-sm font-medium {theme.text}"
						>Description:</label
					>
					<textarea
						id="description"
						name="description"
						bind:value={formData.description}
						rows="5"
						class:border-red-500={errors?.description}
						class="mt-1 block w-full rounded-md border border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
					></textarea>
					{#if errors?.description}<span class="mt-1 text-sm text-red-500"
							>{errors.description}</span
						>{/if}
				</div>
				<div class="min-h-full">
					<div>
						<label for="difficulty" class="block text-sm font-medium {theme.text}"
							>Difficulty:</label
						>
						<Dropdown
							id="difficulty"
							items={Object.entries(Difficulty).map(([key, value]) => ({
								name: key,
								value: value
							}))}
							selected={formData.difficulty}
						/>
					</div>
					<div>
						<label for="topics" class="block text-sm font-medium {theme.text} ">Topics:</label>
						<input
							type="text"
							id="topics"
							bind:value={formData.topics}
							class="mt-1 block w-full rounded-md border border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
						/>
					</div>
				</div>
			</div>

			<button
				type="submit"
				disabled={loading}
				class="mt-1 inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
			>
				{#if loading}
					Submitting...
				{:else}
					Submit
				{/if}
			</button>
		</form>
	</div>
</div>
