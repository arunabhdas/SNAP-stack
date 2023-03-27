<script>
    import { CodeBlock } from "@skeletonlabs/skeleton";
</script>

<div class="card rounded-lg">
    <header class="card-header">
        Title of Prompt
        <div class="float-right">
            <button type="button" class="btn btn-sm variant-filled-secondary rounded-lg">
                Favorite
            </button>
            <button type="button" class="btn btn-sm variant-filled-error rounded-lg"> X </button>
        </div>
    </header>
    <section class="p-4">
        <CodeBlock language={"bash"} code={`<h1>Welcome to SNAP Stack</h1>`}/>
    </section>
</div>
