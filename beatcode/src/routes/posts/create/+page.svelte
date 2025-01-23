<script lang="ts">
	import { enhance } from '$app/forms';
	import { currentTheme } from '$lib/theme/ThemeManager';
	import { themes } from '$lib/theme/themes';
	import { isValidURL } from '$lib';
	import { Difficulty } from '$lib/types';
	import Dropdown from '$components/Dropdown.svelte';
	import type { SubmitFunction, ActionData } from './$types';

	$: theme = themes[$currentTheme] || themes.default;
	export let form: ActionData;

	interface FormData {
		number: string;
		title: string;
		url: string;
		description: string;
		difficulty: Difficulty;
		input_constraint: string[];
		examples: string[];
		topics: number[];
	}

	let formData: FormData = {
		number: '',
		title: '',
		url: '',
		description: '',
		difficulty: Difficulty.Easy,
		input_constraint: [],
		examples: [],
		topics: []
	};

	let errors: { [key in keyof FormData]?: string } = {};

	function validateField(fieldName: keyof FormData) {
		errors[fieldName] = undefined;

		switch (fieldName) {
			case 'number':
				if (!formData.number.trim()) {
					errors.number = `${fieldName} is required.`;
				} else if (isNaN(Number(formData.number))) {
					errors[fieldName] = `${fieldName} must be a number.`;
				} else if (parseFloat(formData.number) !== Number(formData.number)) {
					errors[fieldName] = `${fieldName} must be a valid number.`;
				} else if (!Number.isInteger(Number(formData.number))) {
					errors[fieldName] = `${fieldName} must be a integer.`;
				}
				break;
			case 'title':
				if (!formData.title.trim()) {
					errors.title = `${fieldName} is required.`;
				} else if (formData.title.length < 3) {
					errors.title = `${fieldName} must be at least 3 characters.`;
				}
				break;
			case 'url':
				if (!formData.url.trim()) {
					errors.url = `${fieldName} is required.`;
				} else if (!isValidURL(formData.url)) {
					errors.url = `Invalid ${fieldName}`;
				}
				break;
			case 'description':
				if (!formData.description.trim()) {
					errors.description = 'Description is required.';
				}
				break;
		}
	}

	function handleDropdownSelect(difficulty: Difficulty) {
		formData.difficulty = difficulty;
	}

	const handleSubmit: SubmitFunction = () => {
		for (const field in formData) {
			validateField(field as keyof FormData);
		}
		return async ({ result, update }) => {
			await update();
			if (result.type === 'success') {
				// Optionally reset the form
			}
			if (result.type === 'error') {
				console.error(result.error.message);
			}
		};
	};

	// function handleSubmit() {
	// 	for (const field in formData) {
	// 		validateField(field as keyof FormData);
	// 	}

	// 	// if (Object.keys(errors).length === 0) {
	// 	// 	formData = { number: '', title: '', url: '', description: '', difficulty: Difficulty.Easy }; // Reset form
	// 	// }

	// 	// handle form submission
	// }
</script>

<form method="POST" action="?/create" use:enhance={handleSubmit}>
	<div class="grid grid-cols-[3fr_9fr] gap-4">
		<div>
			<label for="number" class="block text-sm font-medium {theme.text}">Number:</label>
			<input
				type="text"
				id="number"
				bind:value={formData.number}
				on:blur={() => validateField('number')}
				class="mt-1 block w-full rounded-md border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
			/>
			{#if errors.number}<span class="mt-1 text-sm text-red-500">{errors.number}</span>{/if}
		</div>
		<div>
			<label for="title" class="block text-sm font-medium {theme.text}">Title:</label>
			<input
				type="text"
				id="title"
				bind:value={formData.title}
				on:blur={() => validateField('title')}
				class="mt-1 block w-full rounded-md border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
			/>
			{#if errors.title}<span class="mt-1 text-sm text-red-500">{errors.title}</span>{/if}
		</div>
	</div>

	<div>
		<label for="url" class="block text-sm font-medium {theme.text} ">URL:</label>
		<input
			type="url"
			id="url"
			bind:value={formData.url}
			on:blur={() => validateField('url')}
			class="mt-1 block w-full rounded-md border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
		/>
		{#if errors.url}<span class="mt-1 text-sm text-red-500">{errors.url}</span>{/if}
	</div>

	<div class="grid grid-cols-2 gap-4">
		<div class="min-h-full">
			<label for="description" class="block text-sm font-medium {theme.text}">Description:</label>
			<textarea
				id="description"
				bind:value={formData.description}
				on:blur={() => validateField('description')}
				rows="5"
				class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
			></textarea>
			{#if errors.description}<span class="mt-1 text-sm text-red-500">{errors.description}</span
				>{/if}
		</div>
		<div class="min-h-full">
			<div>
				<label for="difficulty" class="block text-sm font-medium {theme.text}">Difficulty:</label>
				<Dropdown
					id="difficulty"
					items={Object.entries(Difficulty).map(([key, value]) => ({
						name: key,
						value: value
					}))}
					selected={formData.difficulty}
					label="Select a fruit"
					onSelect={handleDropdownSelect}
				/>
			</div>
			<div>
				<label for="topics" class="block text-sm font-medium {theme.text} ">Topics:</label>
				<input
					type="text"
					id="topics"
					bind:value={formData.topics}
					class="mt-1 block w-full rounded-md border-gray-300 p-3 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
				/>
			</div>
		</div>
	</div>

	<button
		type="submit"
		class="inline-flex items-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
	>
		Submit
	</button>
</form>
