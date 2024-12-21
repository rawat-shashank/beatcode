<script>
	import '../app.css'; // Import your global styles
	import { base } from '$app/paths';
</script>

<main>
	<nav>
		<a href="{base}/">Home</a>
		<a href="{base}/posts">Posts</a>

	</nav>
	<slot />
</main>

<style>
	nav {
		background-color: #f0f0f0; /* Example background color */
		padding: 10px;
		margin-bottom: 20px;
	}

	nav a {
		margin-right: 10px;
		text-decoration: none;
		color: #333;
	}
	main {
		padding: 10px;
	}
</style>
