export interface Theme {
	bg: string;
	text: string;
	accent: string;
	name: string;
}

export const themes: { [key: string]: Theme } = {
	default: {
		bg: 'white-400',
		text: 'red',
		accent: 'bg-my-theme-default-accent',
		name: 'Default'
	},
	forest: {
		bg: 'bg-forest-bg',
		text: 'text-forest-text',
		accent: 'text-forest-accent',
		name: 'Forest'
	},
	ocean: {
		bg: 'bg-ocean-bg',
		text: 'text-ocean-text',
		accent: 'text-ocean-accent',
		name: 'Ocean'
	},
	carbon: {
		bg: 'bg-carbon-bg',
		text: 'text-carbon-text',
		accent: 'text-carbon-accent',
		name: 'Carbon'
	}
};
