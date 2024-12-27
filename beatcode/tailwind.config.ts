import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				theme: {
					'ocean-bg': '#e0f2f7'
				},
				forest: {
					bg: '#fdf0d5',
					accent: '#d91c81',
					secondary: '#8e2949',
					text: '#8e2949'
				},
				ocean: {
					bg: '#1e1e2e',
					accent: '#cba6f7',
					secondary: '#7f849c',
					text: '#fff'
				},
				carbon: {
					bg: '#313131',
					accent: '#f66e0d',
					secondary: '#616161',
					text: '#fff'
				}
			}
		}
	},
	plugins: []
} satisfies Config;
