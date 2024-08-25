# Mod Loading

Balamod can load mods and apis automatically or manually. When balamod mod-loader is installed, it creates a `mods` folder in the Balatro save directory. It also installs itself there, by putting all of its libraries in the folder as well as by overloading the game's entrypoint to inject itself.

The folder depends on the platform.

- Windows: `C:\Users\<username>\AppData\Roaming\Balatro` aka `%APPDATA%\Balatro`
- macOS: `~/Library/Application Support/Balatro`
- Linux: `~/.local/share/Steam/steamapps/compatdata/2379780/pfx/drive_c/users/steamuser/AppData/Roaming/Balatro`

## Automatic Mod Loading

If a user downloads a mod from the in-game mod gallary, the mod will be automatically loaded by balamod. The mod will be placed in the `mods` folder.

## Manual Mod Loading

If a user downloads a mod from the internet, the mod file should be placed in the `mods` folder. The mod will be loaded by balamod when the game is started.
