<div class="accordion-container">
  <Accordion multiple>
    {#each data.repos as repo}
      <Panel>
        <Header>{repo.owner} - {repo.repo}</Header>
        <Content>
          <LayoutGrid>
            {#each repo.mods as mod}
              <Cell>
                <Card padded>
                  <PrimaryAction padded on:click={() => navigate(mod.url)}>
                    <Content>
                      <h4>{mod.name} - {mod.version}</h4>
                      <p>{mod.description}</p>
                    </Content>
                  </PrimaryAction>
                </Card>
              </Cell>
            {/each}
          </LayoutGrid>
        </Content>
      </Panel>
    {/each}
  </Accordion>
</div>

<script lang="ts">
  import Accordion, { Panel, Header, Content } from '@smui-extra/accordion';
  import LayoutGrid, { Cell } from '@smui/layout-grid';
  import Card, { PrimaryAction } from '@smui/card';
  export let data;

  function navigate(url: string) {
    window.open(url, '_blank');
  }
</script>
