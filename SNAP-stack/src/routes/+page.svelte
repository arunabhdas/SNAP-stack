<script lang="ts">
    import PromptSnippetCard from "../PromptSnippetCard.svelte";
	import { promptSnippetStore, addPrompt } from "../PromptSnippetStore";
	import type { PageData } from "./$types";
    export let data: PageData;

    data.prompts
    let formData : PromptSnippetInput = {
        title: "",
	    platform: "midjourney",
	    prompt: ""
    }

    // createPrompt(input: PromptSnippetInput)
    promptSnippetStore.set(data.prompts);

    // SnippetStore -> local writable that allows us to store prompt snippets


    // create / delete prompts

    // favorite prompts

    // +page.ts to initially load in some example prompts (mocking a database request)


</script>

<div class="flex justify-center">
    <div class="grid grid-cols-1 gap-4 min-w-full md:min-w-[750px]">
        <h6 class="text-center py-2">Create an AI prompt</h6>
        <div class="card p-4 w-full text-token space-y-4 rounded-lg">
            <label class="label">
                <span>Prompt Title</span>
                <input class="input rounded-lg" type="text" placeholder="Enter prompt" bind:value={formData.title}/>
            </label>

            <label class="label">
                <span>AI Platform</span>
                <select class="select rounded-lg" bind:value={formData.platform}>
                    <option value="GPT">GPT</option>
                    <option value="Midjourney">Midjourney</option>
                    <option value="Stable Diffusion">Stable Diffusion</option>
                </select>
            </label>

            <label class="label">
                <span>Prompt Snippet</span>
                <textarea class="textarea rounded-lg" rows="4" placeholder="Enter prompt here" bind:value={formData.prompt}></textarea>
            </label>
            <button type="button" class="btn btn-sm variant-filled-primary rounded-lg" on:click={()=> addPrompt(formData)}>Create Prompt</button>
            <div class="text-center py-0">
                <h6>My Prompts</h6>
            </div>
            {#each $promptSnippetStore as prompt, index}
            <PromptSnippetCard promptSnippet={prompt} index={index} />
            {/each}
        </div>
    </div>
</div>
