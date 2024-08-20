# localizations

<!-- toc -->

## GLOBALS

### `VERSION`: string

String representing the version of the module

## FUNCTIONS

### `getModLocale(mod: Mod, locale: string) -> table | nil`

Gets the locale file for a mod given a locale string. Returns a table with the
loaded json table.

<!-- lua: https://github.com/balamod/balamod_lua/blob/main/src/localization.lua#L11 -->

### `inject() -> nil`

Injects the localization files for all loaded and enabled mods into the games `G.localization` table.

<!-- lua: https://github.com/balamod/balamod_lua/blob/main/src/localization.lua#L37 -->
