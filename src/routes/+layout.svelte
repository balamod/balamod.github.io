<script lang="ts">
	import TopAppBar, { Section, Row } from '@smui/top-app-bar';
	import Button, { Label } from '@smui/button';
  import IconButton from '@smui/icon-button';
	import { faGithub } from '@fortawesome/free-brands-svg-icons';
	import Fa from 'svelte-fa';
  import Drawer, {
    AppContent,
    Content,
    Scrim,
  } from '@smui/drawer';
  import { page } from '$app/stores';
  import List, { Item, Text, Separator } from '@smui/list';

  export let open = false;
  export let activePageUrl = '/docs/user-guide/installation';
  export let documentationPages = [
    {
      title: 'User Guide',
      url: '/docs/user-guide',
      indent: 0,
    },
    {
      title: 'Installation',
      url: '/docs/user-guide/installation',
      indent: 1,
    },
    {
      title: 'Installing mods',
      url: '/docs/user-guide/install-mods',
      indent: 1,
    },
    {
      title: 'Installing mods with the marketplace',
      url: '/docs/user-guide/install-mods/marketplace',
      indent: 2,
    },
    {
      title: 'Installing mods manually',
      url: '/docs/user-guide/install-mods/manual',
      indent: 2,
    },
    {
      separator: true,
    },
    {
      title: 'Modding Guide',
      url: '/docs/modding-guide',
      indent: 0,
    },
    {
      title: 'Getting Started',
      url: '/docs/modding-guide/getting-started',
      indent: 1,
    },
    {
      title: 'Decompiling',
      url: '/docs/modding-guide/decompiling',
      indent: 1,
    },
    {
      title: 'Code injection',
      url: '/docs/modding-guide/code-injection',
      indent: 1,
    },
    {
      title: 'Modding APIs',
      url: '/docs/modding-guide/apis',
      indent: 1,
    },
    {
      title: 'Mod manifests and dependencies',
      url: '/docs/modding-guide/mod-manifests',
      indent: 1,
    },
    {
      title: 'Publishing mods to the marketplace',
      url: '/docs/modding-guide/publishing',
      indent: 1,
    },
    {
      separator: true,
    },
    {
      title: 'Contributing',
      url: '/docs/contributing',
      indent: 0,
    },
    {
      title: 'Reverse engineering findings',
      url: '/docs/contributing/balatro',
      indent: 1,
    },
    {
      title: 'Inner workings of the UI code',
      url: '/docs/contributing/ui-code',
      indent: 1,
    },
    {
      title: 'Contributing to balamod\'s injector',
      url: '/docs/contributing/injector',
      indent: 1,
    },
    {
      title: 'Adding and maintaining balamod APIs',
      url: '/docs/contributing/apis',
      indent: 1,
    },
  ];
</script>

<div class="flexy">
	<div class="top-app-bar-container flexor">
		<TopAppBar variant="static" dense={true} color="primary">
			<Row>
        <Section>
          {#if $page.url.pathname.startsWith('/docs')}
            <IconButton on:click={() => (open = !open)} class="material-icons">menu</IconButton>
          {:else}
            <div style="width:48px;"></div> <!-- Spacer -->
          {/if}
					<Button href="/"><Label>Home</Label></Button>
					<Button href={activePageUrl}><Label>Documentation</Label></Button>
					<Button href="/mods"><Label>Mods</Label></Button>
				</Section>
				<Section align="end">
					<Button href="https://github.com/UwUDev/balamod" target="_blank">
						<Fa icon={faGithub} scale={1.5} />
					</Button>
				</Section>
			</Row>
		</TopAppBar>
		<div class="flexor-content">
      {#if $page.url.pathname.startsWith('/docs')}
        <div class="drawer-container">
          <Drawer variant="modal" fixed={false} bind:open>
            <Content>
              <List>
                {#each documentationPages as page}
                  {#if 'separator' in page}
                    <Separator />
                  {:else}
                    <Item
                      href={page.url}
                      activated={page.url === activePageUrl}
                      style={page.indent
                        ? 'margin-left: ' + page.indent * 25 + 'px;'
                        : ''}
                    >
                      <Text>{page.title}</Text>
                    </Item>
                  {/if}
                {/each}
              </List>
            </Content>
          </Drawer>
          <Scrim fixed={false} />
          <AppContent class="app-content">
            <main class="main-content">
              <slot />
            </main>
          </AppContent>
        </div>
      {:else}
			  <slot />
      {/if}
		</div>
	</div>
</div>

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

  .drawer-container {
    position: relative;
    display: flex;
    height: 100%;
    width: 100%;
    border: 1px solid
      var(--mdc-theme-text-hint-on-background, rgba(0, 0, 0, 0.1));
    overflow: hidden;
    z-index: 0;
  }

  * :global(.app-content) {
    flex: auto;
    overflow: auto;
    position: relative;
    flex-grow: 1;
  }

  .main-content {
    overflow: auto;
    padding: 16px;
    height: 100%;
    box-sizing: border-box;
  }
</style>
