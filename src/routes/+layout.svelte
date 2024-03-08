<script lang="ts">
  import TopAppBar, { Section, Row } from '@smui/top-app-bar';
  import Button, { Label } from '@smui/button';
  import { faGithub } from '@fortawesome/free-brands-svg-icons';
  import Fa from 'svelte-fa';
</script>

<body>
  <div class="flexy">
    <div class="top-app-bar-container flexor">
      <TopAppBar variant="static" dense={true} color="primary">
        <Row>
          <Section>
            <Button href="/balamod.github.io"><Label>Home</Label></Button>
            <Button href="/balamod.github.io/docs"><Label>Documentation</Label></Button>
            <Button href="/balamod.github.io/mods"><Label>Mods</Label></Button>
          </Section>
          <Section align="end">
            <Button href="https://github.com/UwUDev/balamod" target="_blank">
              <Fa icon={faGithub} scale={1.5}/>
            </Button>
          </Section>
        </Row>
      </TopAppBar>
      <div class="flexor-content">
        <slot></slot>
      </div>
    </div>
  </div>
</body>

<style>
  .top-app-bar-container {
    width: 100vw;
    height: calc(100vh - 20px);
    border: 1px solid var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
    margin: 0 18px 18px 0;
    background-color: var(--mdc-theme-background, #fff);

    overflow: auto;
    display: inline-block;
  }

  @media (max-width: 480px) {
    .top-app-bar-container {
      margin-right: 0;
    }
  }

  .flexy {
    display: flex;
    flex-wrap: wrap;
    overflow-y: hidden;
  }

  .flexor {
    display: inline-flex;
    flex-direction: column;
  }

  .flexor-content {
    flex-basis: 0;
    height: 0;
    flex-grow: 1;
    overflow: auto;
  }
</style>
