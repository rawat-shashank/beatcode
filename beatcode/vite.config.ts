import { defineConfig } from 'vitest/config';
import { sveltekit } from '@sveltejs/kit/vite';

export default defineConfig({
	plugins: [sveltekit()],
	base: '/beatcode/', // MATCH paths.base + trailing slash!

	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});
