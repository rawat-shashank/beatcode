<script>
	import { currentTheme } from '$lib/theme/ThemeManager';
	import { themes } from '$lib/theme/themes';
	import '../app.css';
	import Container from '../components/Container.svelte';
	import Header from '../components/Header/Header.svelte';

	$: theme = themes[$currentTheme] || themes.default;
</script>

<main class={theme.bg}>
	<Header />
	<Container>
		<slot />
	</Container>
</main>
