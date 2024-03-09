<script lang="ts">
  import Code from '$lib/components/Code.svelte';
</script>
<p>The API of balamod provides a simple way to inject arbitrary code into an existing balatro function</p>

<Code language="lua" lineNumbers>balamod.inject('balatro', 'function', 'function', 'function')</Code>
