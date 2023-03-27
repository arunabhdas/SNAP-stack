import { writable, get } from "svelte/store";
// PromptStore

// Prompt Snippet

// Title, Prompt, Language, Favorite
export const promptSnippetStore = writable<PromptSnippet[]>([]);


// addPrompt
export function addPrompt(input: PromptSnippetInput) {
    let prompts = get(promptSnippetStore); // $promptSnippetStore -> listen to changes to the value of promptStore
    promptSnippetStore.update(() => {
        return [{ ...input, favorite: false }, ...prompts]
    });
}

// updatePrompt
export function updatePrompt(inputPrompt: PromptSnippetInput, index: number) {
    let prompts = get(promptSnippetStore);
    return prompts.map((prompt, promptIndex) => {
        if (promptIndex === index) {
            return inputPrompt
        }
        return prompt;
    });
}

// deletePrompt
export function deletePrompt(index: number) {
    let prompts = get(promptSnippetStore);
    prompts.splice(index, 1);
    promptSnippetStore.update(() => {
        return prompts;
    });
}

// toggleFavorite
export function toggleFavorite(index: number) {
    let prompts = get(promptSnippetStore);
    return prompts.map((prompt, promptIndex) => {
        if (promptIndex === index) {
            return { ...prompt, favorite: !prompt.favorite }
        }
        return prompt;
    });
}

