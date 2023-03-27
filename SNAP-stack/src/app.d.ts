// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
// and what to do when importing types
declare namespace App {
	// interface Locals {}
	// interface PageData {}
	// interface Error {}
	// interface Platform {}
}

interface PromptSnippetInput {
	title: string
	platform: string
	prompt: string
}

interface PromptSnippet {
	title: string
	platform: string
	prompt: string
	favorite: boolean
}
