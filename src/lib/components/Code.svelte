<script lang="ts">
  import Highlight, { LineNumbers } from "svelte-highlight";
  import typescript from "svelte-highlight/languages/typescript";
  import lua from "svelte-highlight/languages/lua";
  import json from "svelte-highlight/languages/json";
  import rust from "svelte-highlight/languages/rust";
  import plaintext from "svelte-highlight/languages/plaintext";
  import glsl from "svelte-highlight/languages/glsl";
  import github from "svelte-highlight/styles/github";
	import IconButton from "@smui/icon-button/src/IconButton.svelte";

  export let lineNumbers: boolean = false;
  export let language: 'typescript' | 'lua' | 'json' | 'rust' | 'glsl' | 'plaintext' = 'plaintext';
  let code: HTMLSpanElement;

  function getLanguage() {
    switch (language) {
      case 'typescript':
        return typescript;
      case 'lua':
        return lua;
      case 'json':
        return json;
      case 'rust':
        return rust;
      case 'glsl':
        return glsl;
      case 'plaintext':
        return plaintext;
    }
  }

  function capitalize(str: string) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  async function copyCode(code: string) {
    await navigator.clipboard.writeText(code);
  }
</script>

<svelte:head>
  {@html github}
</svelte:head>

<div class="code-container">
  <span class="code-header">
    <pre style="margin-left:1rem; font-size:small;">{capitalize(language)}</pre>
    <IconButton on:click={() => copyCode(code.innerText)} class="material-icons">content_copy</IconButton>
  </span>
  <span style="display: none;" bind:this={code}><slot /></span>
  <Highlight language={getLanguage()} let:highlighted code={code?.innerText ?? ""}>
    {#if lineNumbers}
      <LineNumbers {highlighted}/>
    {/if}
  </Highlight>
</div>

<style>
  .code-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.2rem;
  }

  .code-container {
    border: 1px solid var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
    border-radius: 4px;
    overflow: hidden;
    padding: 2px;
  }
</style>
