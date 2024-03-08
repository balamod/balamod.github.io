<h1>Balamod</h1>

<p>A mod loader for Balatro, written in Rust!</p>

<h2>
  Releases
</h2>

<p>Latest balamod release is {data.releaseVersion}</p>

<div class="row">
  <Card padded>
    <PrimaryAction padded on:click={() => download(data.windowsDownloadUrl)}>
      <Content>
        <div class="column">
          <Fa icon={faWindows} scale={5} />
          <h3>Windows</h3>
        </div>
      </Content>
    </PrimaryAction>
  </Card>
  <Card padded>
    <PrimaryAction padded on:click={() => download(data.linuxDownloadUrl)}>
      <Content>
        <div class="column">
          <Fa icon={faLinux} scale={5}/>
          <h3>Linux</h3>
        </div>
      </Content>
    </PrimaryAction>
  </Card>
  <Card padded>
    <PrimaryAction padded on:click={() => download(data.macDownloadUrl)}>
      <Content>
        <div class="column">
          <Fa icon={faApple} scale={5}/>
          <h3>MacOS</h3>
        </div>
      </Content>
    </PrimaryAction>
  </Card>
</div>

<script lang="ts">
  import type { HomePageData } from "$lib/interfaces";
  import Card, { Content, PrimaryAction } from '@smui/card';
  import Fa from 'svelte-fa';
  import { faApple, faWindows, faLinux } from '@fortawesome/free-brands-svg-icons';

  export let data: HomePageData;

  function download(url: string) {
    window.open(url, '_blank');
  }
</script>

<style>
  .row {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
  }

  .column {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
