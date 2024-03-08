import type { HomePageData } from '$lib/interfaces';
import { Octokit } from 'octokit';

export async function load({ params }): Promise<HomePageData> {
  const octokit = new Octokit();
  const { data } = await octokit.request('GET /repos/{owner}/{repo}/releases', {
    owner: 'UwUDev',
    repo: 'balamod',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    },
  });
  const latest = data[0];
  return {
    releaseVersion: latest.tag_name,
    linuxDownloadUrl: latest.assets.find(asset => asset.name.includes('linux'))?.browser_download_url ?? "",
    windowsDownloadUrl: latest.assets.find(asset => asset.name.includes('windows'))?.browser_download_url ?? "",
    macDownloadUrl: latest.assets.find(asset => asset.name.includes('mac'))?.browser_download_url ?? "",
  };
}
