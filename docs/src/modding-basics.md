# Modding Basics

Balamod mods follow a very specific format,
composed of at least 2 files

```
...
└─mods/
  └─your_mod_id/
    ├─main.lua
    └─manifest.json
```

## `main.lua`

This is the entrypoint of your lua code. `main.lua` should always return. It is where you can add functions, require
APIs, and register [events](./events.md) for your mod. Below is an example empty `main.lua`. You don't need to have all
the hooks, only the ones you need.

```lua
local logging = require("logging")
local logger = logging.getLogger("test_mod")

local function on_enable()
    logger:info("Mod enabled")
end

return {
    on_enable = on_enable
}
```

## `manifest.json`

This JSON document specifies the metadata about your mod, here are the fields

| field               | type     | required | description                                                               |
|:--------------------|:---------|:---------|:--------------------------------------------------------------------------|
| id                  | string   | true     | the mod id for your mod. Must match the name of the folder the mod is in. |
| name                | string   | true     | Display name for your mod, displayed in the mod menu                      |
| version             | string   | true     | Semantic versioning for your mod, used for checking updates for it.       |
| description         | string[] | true     | Description of your mod. Each entry in the array is a line                |
| author              | string   | true     | Author(s) of the mod                                                      |
| load_before         | string[] | true     | List of mod IDs to load before this mod                                   |
| load_after          | string[] | true     | List of mod IDs to load after this mod                                    |
| min_balamod_version | string   | false    | Minimum required version of balamod for this mod to run                   |
| max_balamod_version | string   | false    | Maximum version of balamod for this mod to run                            |
| balalib_version     | string   | false    | Desired version of balalib for this mod to run (Ex: `=1.0.0` or `>1.0.0`) |

Your mod manifest is also describing your mod for submissions to the mod catalog. Mods with invalid manifests will not
load into the game.

## Localization and i18n

Localization discovery is done automatically. Balamod will load all json files within the `localization`
folder of your mod for new strings to translate. The format of a localization string is identical to what
the game internally uses, besides being in `JSON` rather than `LUA` to ease on interoperability (allowing
you to make scripts to generate localizations with an API like `DeepL` for instance)

Here is a mod folder structure that supports the english language:

```
...
└─mods/
  └─your_mod_id/
    ├─localization/
    │ └─en-us.json
    ├─main.lua
    └─manifest.json
```

The following localization file names are available:

- `de.json` : Deutch -- German
- `en-us.json`: English -- English US
- `es_419.json`: Español (México) -- Spanish (Mexican)
- `es_ES.json`: Español (España) -- Spanish (Spain)
- `fr.json`: Français -- French
- `id.json`: Bahasa Indonesia -- Indonesian
- `it.json`: Italiano -- Italian
- `ja.json`: 日本語 -- Japanese
- `ko.json`: 한국어 -- Korean
- `nl.json`: Nederlands -- Dutch
- `pl.json`: Polski -- Polish
- `pt_BR.json`: Português -- Portugese (Brazil)
- `ru.json`: Русский -- Russian
- `zh_CN.json`: 简体中文 -- Chinese (Simplified)
- `zh_TW.json`: 繁體中文 -- Chinese (Traditional)

Localizations are merged in the load order of mods. If you need to overwrite the localization of a mod,
or if you want to change the game's localization, make sure your mod loads **after** the mod you want
to overwrite. Use the `load_after` manifest key to that effect.

See [`utils.mergeTables()`](./apis/utils.md) for more informations.
