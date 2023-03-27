<script lang="ts">
    import { CodeBlock } from "@skeletonlabs/skeleton";
    import { deletePrompt, toggleFavorite } from "./PromptSnippetStore";
    export let promptSnippet : PromptSnippet = {
        title: "",
        platform: "",
        prompt: "",
        favorite: false
    }

    export let index: number;
</script>

<div class="card rounded-lg">
    <header class="card-header">
        {promptSnippet.title} - {promptSnippet.platform}
        <div class="float-right">
            <button type="button" class="btn btn-sm variant-filled-secondary rounded-lg" on:click={() => toggleFavorite(index)}>
                { promptSnippet.favorite ? "Unfavorite" : "Favorite" }
            </button>
            <button type="button" class="btn btn-sm variant-filled-error rounded-lg" on:click={() => deletePrompt(index)}> X </button>
        </div>
    </header>
    <section class="p-4">
        <CodeBlock language="text" platform={promptSnippet.platform} code={promptSnippet.prompt}/>
    </section>
</div>
