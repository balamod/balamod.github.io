export interface HomePageData {
  releaseVersion: string;
  linuxDownloadUrl: string;
  windowsDownloadUrl: string;
  macDownloadUrl: string;
}

export interface Mod {
  slug: string;
  version: string;
  name: string;
  description: string;
  url: string;
}

export interface ModRepository {
  mods: Mod[];
  repoUrl: string;
  owner: string;
  repo: string;
}

export interface ModsPageData {
  repos: ModRepository[];
}
