import { redirect } from '@sveltejs/kit';

export function load() {
  redirect(302, '/docs/user-guide/install-mods/marketplace');
}
