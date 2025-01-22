interface Example {
	input: any;
	output: any;
	explanation?: string;
}

export enum Difficulty {
	Easy,
	Medium,
	Hard
}

export interface Post {
	id: number;
	url: string; // Or URL if your environment supports it (e.g., modern browsers)
	title: string;
	difficulty: Difficulty;
	description: string;
	input_constraints: string[];
	examples: Example[];
}
