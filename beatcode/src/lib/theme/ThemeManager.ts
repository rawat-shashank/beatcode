import { get, writable } from 'svelte/store';
import { themes, type Theme } from './themes';
import { browser } from '$app/environment';

export const currentTheme = writable((browser && localStorage.getItem('theme')) || 'default');

export function setTheme(themeName: string) {
	if (themes[themeName] && browser) {
		currentTheme.set(themeName);
		currentTheme.subscribe((theme) => {
			if (browser) return (localStorage.theme = theme);
		});
	} else {
		console.error(`Invalid theme: ${themeName}`);
	}
}
