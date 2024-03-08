import type { Mod, ModsPageData } from '$lib/interfaces.js';

async function getModsInRepo(repoUrl: string): Promise<Mod[]> {
  const rawMods = (await (await fetch(repoUrl)).text()).split('\n');
  return rawMods.filter((line: string) => line.length > 0).map((line: string) => {
    const [slug, version, name, description, url] = line.split('|');
    return {
      slug,
      version,
      name,
      description,
      url,
    };
  });
}

export async function load(): Promise<ModsPageData> {
  const masterRepoUrl = 'https://raw.githubusercontent.com/UwUDev/balamod/master/repos.index';
  const repoUrls = (await (await fetch(masterRepoUrl)).text()).split('\n');
  const repos = await Promise.all(repoUrls.map(async (url: string) => {
    const { pathname } = new URL(url);
    const [owner, repo] = pathname.split('/').splice(1, 3);
    const mods = await getModsInRepo(url);
    return {
      mods,
      repoUrl: url,
      owner,
      repo,
    };
  }));

  return {
    repos,
  };
}
