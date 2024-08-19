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
