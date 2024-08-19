# Mod Format

Balamod mods follow a very specific format,
composed of at least 2 files

## `main.lua`

This is the entrypoint of your lua code. `main.lua` should always return. It is where you can add functions, require APIs, and register hooks for your mod. Below is an example empty `main.lua`. You don't need to have all the hooks, only the ones you need.

The `menu()` function is called when the mod menu is opened, it will add a "menu" button if you returned it in the table near the "enable/disable" button that calls the function.

```lua
local logging = require("logging")
local logger = logging.getLogger("test_mod")

local function on_enable()
end

local function on_disable()
end

local function menu()
end

local function on_game_load(args)
end

local function on_game_quit()
end

local function on_key_pressed(key)
end

local function on_key_released(key)
end

local function on_mouse_pressed(button, x, y, touch)
end

local function on_mouse_released(button, x, y)
end

local function on_mousewheel(x, y)
end

local function on_pre_render()
end

local function on_post_render()
end

local function on_error(message)
end

local function on_pre_update(dt)
end

local function on_post_update(dt)
end

return {
    on_enable = on_enable,
    on_disable = on_disable,
    menu = menu,
    on_game_load = on_game_load,
    on_game_quit = on_game_quit,
    on_key_pressed = on_key_pressed,
    on_key_released = on_key_released,
    on_mouse_pressed = on_mouse_pressed,
    on_mouse_released = on_mouse_released,
    on_mousewheel = on_mousewheel,
    on_pre_render = on_pre_render,
    on_post_render = on_post_render,
    on_error = on_error,
    on_pre_update = on_pre_update,
    on_post_update = on_post_update,
}
```


## `manifest.json`

This JSON document specifies the metadata about your mod, here are the fields

| field               | type     | required | description                                                              |
|:--------------------| :------- | :------- | :----------------------------------------------------------------------- |
| id                  | string   | true     | the mod id for your mod. Must match the name of the folder the mod is in. |
| name                | string   | true     | Display name for your mod, displayed in the mod menu                     |
| version             | string   | true     | Semantic versioning for your mod, used for checking updates for it.      |
| description         | string[] | true     | Description of your mod. Each entry in the array is a line               |
| author              | string   | true     | Author(s) of the mod                                                     |
| load_before         | string[] | true     | List of mod IDs to load before this mod                                  |
| load_after          | string[] | true     | List of mod IDs to load after this mod                                   |
| min_balamod_version | string   | false    | Minimum required version of balamod for this mod to run                  |
| max_balamod_version | string   | false    | Maximum version of balamod for this mod to run                           |
| balalib_version     | string   | false    | Desired version of balalib for this mod to run (Ex: `=1.0.0` or `>1.0.0`)|


Your mod manifest is also describing your mod for submissions to the mod catalog. Mods with invalid manifests will not load into the game.
