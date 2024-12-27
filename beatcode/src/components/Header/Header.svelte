<script>
	import Logo from '../Logo.svelte';
	import { base } from '$app/paths';
	import { siteMetaData, HEADER_NAV_LINKS } from '$lib';
	import ThemeSwitcher from '../ThemeSwitcher.svelte';
	import { currentTheme } from '$lib/theme/ThemeManager';
	import { themes } from '$lib/theme/themes';

	$: theme = themes[$currentTheme] || themes.default;
</script>

<header>
	<div class="container mx-auto flex flex-col flex-wrap items-center p-5 md:flex-row lg:w-4/6">
		<a href="/" class="title-font mb-4 flex items-center font-medium md:mb-0 {theme.accent}">
			{#if Logo}
				<Logo className="h-14 w-14 {theme.accent}" />
			{/if}
			<span class="ml-3 text-xl {theme.accent}">{siteMetaData.title}</span>
		</a>

		<nav class="flex flex-wrap items-center justify-center text-base md:ml-auto">
			{#each HEADER_NAV_LINKS as link}
				<a
					href={link.href}
					class="mr-5 font-semibold text-indigo-600 hover:text-indigo-800 dark:text-indigo-400 dark:hover:text-indigo-200"
				>
					{link.title}
				</a>
			{/each}
		</nav>
		<ThemeSwitcher />
	</div>
</header>
