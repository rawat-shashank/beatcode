<script lang="ts">
	import { currentTheme } from '$lib/theme/ThemeManager';
	import { themes } from '$lib/theme/themes';

	$: theme = themes[$currentTheme] || themes.default;
</script>

<h1 class={theme.text}>Welcome to My Blog</h1>
