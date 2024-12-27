<script lang="ts">
	import { setTheme, currentTheme } from '$lib/theme/ThemeManager';
	import { themes } from '$lib/theme/themes';
	let open = false;

	function handleThemeSelect(themeName: string) {
		setTheme(themeName);
	}
</script>

<div class="relative inline-block text-left">
	<div>
		<button
			type="button"
			on:click={() => (open = !open)}
			class="inline-flex w-full justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:bg-gray-700 dark:text-gray-200 dark:hover:bg-gray-600"
			id="menu-button"
			aria-expanded={open}
			aria-haspopup="true"
		>
			{$currentTheme ? themes[$currentTheme].name : 'Select Theme'}
			<svg
				class="-mr-1 ml-2 h-5 w-5"
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 20 20"
				fill="currentColor"
				aria-hidden="true"
			>
				<path
					fill-rule="evenodd"
					d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
					clip-rule="evenodd"
				/>
			</svg>
		</button>
	</div>

	{#if open}
		<div
			class="absolute right-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none dark:bg-gray-800"
			role="menu"
			aria-orientation="vertical"
			aria-labelledby="menu-button"
			tabindex="-1"
		>
			<div class="py-1" role="none">
				{#each Object.entries(themes) as [themeName, themeData]}
					<!-- svelte-ignore a11y_invalid_attribute -->
					<a
						href="#"
						on:click|preventDefault={() => {
							handleThemeSelect(themeName);
							open = false;
						}}
						class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-700"
						role="menuitem"
						tabindex="-1"
						id="menu-item-0"
					>
						{themeData.name}
					</a>
				{/each}
			</div>
		</div>
	{/if}
</div>
