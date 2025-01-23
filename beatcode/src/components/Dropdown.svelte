<script lang="ts">
	import { browser } from '$app/environment';

	export let id: string = '';
	export let items: { name: string; value: any }[] = [];
	export let selected: any = null;
	export let label: string = 'Select an option';
	export let onSelect: (value: any) => void = () => {}; // Callback function

	let isOpen = false;
	let dropdownContainer: any;

	const toggleDropdown = () => {
		isOpen = !isOpen;
	};

	const selectItem = (item: any) => {
		selected = item.value;
		isOpen = false;
		onSelect(item.value); // Call the callback function
	};

	$: if (isOpen && browser) {
		document.addEventListener('click', handleClickOutside, { once: true });
	} else if (!isOpen && browser) {
		document.removeEventListener('click', handleClickOutside);
	}

	const handleClickOutside = (event: Event) => {
		if (!dropdownContainer.contains(event.target as HTMLElement)) {
			isOpen = false;
		}
	};
</script>

<div {id} class="relative inline-block w-full text-left" bind:this={dropdownContainer}>
	<div>
		<button
			type="button"
			on:click={toggleDropdown}
			class="inline-flex w-full justify-center border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm focus:outline-none"
			id="menu-button"
			aria-expanded={isOpen}
			aria-haspopup="true"
		>
			{selected ? items.find((i) => i.value === selected)?.name : label}
			<svg
				class="-mr-1 ml-2 h-5 w-5"
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 20 20"
				fill="currentColor"
				aria-hidden="true"
				class:rotate-180={isOpen}
				class:transition-transform={true}
			>
				<path
					fill-rule="evenodd"
					d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
					clip-rule="evenodd"
				/>
			</svg>
		</button>
	</div>

	{#if isOpen}
		<div
			class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none dark:bg-gray-800"
			role="menu"
			aria-orientation="vertical"
			aria-labelledby="menu-button"
			tabindex="-1"
		>
			<div class="py-1" role="none">
				{#each items as item}
					<!-- svelte-ignore a11y_invalid_attribute -->
					<a
						href="#"
						on:click|preventDefault={() => selectItem(item)}
						class="block cursor-pointer px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-700"
						role="menuitem"
						tabindex="-1"
					>
						{item.name}
					</a>
				{/each}
			</div>
		</div>
	{/if}
</div>
