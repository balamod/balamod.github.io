# Developer Console

Balamod comes with a fully fledged developer console to play with, with some built in commands to help debugging.

## Shortcuts

- `F1` : Restart the game
- `F2` : Toggle the console panel on/off
- `F4` : Toggle debug mode on/off

If the console is opened, you have access to the following shortcuts as well:

**On Mac**

- `Cmd + Shift + C` : Copy all messages into the clipboard
- `Cmd + C` : Copy the currently typed command to the clipboard
- `Cmd + V` : Paste the contents of the clipboard into the command input
- `Escape` : Close the console panel
- `Cmd + Backspace`: Delete the console input line
- `Cmd + right`: Move text to the most recent
- `Cmd + left`: Move text to the most ancient
- `Cmd + up`: Move one page up
- `Cmd + down`: Move one page down
- `up`: Go back one command in the history
- `down`: Go forward one command in the history
- `tab`: Complete the current command
- `Return`: Submit the command to be run

**On Windows / Linux**

- `Ctrl + Shift + C` : Copy all messages into the clipboard
- `Ctrl + C` : Copy the currently typed command to the clipboard
- `Ctrl + V` : Paste the contents of the clipboard into the command input
- `Escape` : Close the console panel
- `Del`: Delete the console input line
- `End`: Move text to the most recent
- `Home`: Move text to the most ancient
- `PageUp`: Move one page up
- `PageDown`: Move one page down
- `up`: Go back one command in the history
- `down`: Go forward one command in the history
- `tab`: Complete the current command
- `Return`: Submit the command to be run

## Built in commands

The balamod dev console comes with a number of built-in commands to help you troubleshoot common issues with your mod, or if you're so inclined, to cheat in the game (if that's your thing)


- `clear`: clears the log output from the console
- `discards <add|remove|set> <amount>`: sets the amount of discards the player has.
- `exit`: exits the console
- `give <item>`: gives an item via its internal ID to the player. Example : `give j_blueprint`
- `hands <add|remove|set> <amount>`: sets the amount of hands the player has.
- `help [command]`: Prints all available commands with their descriptions
- `history`: prints the history of commands
- `installmod <url>`: installs a mod via its URL, URL must point to a valid tarball.
- `luamod <mod_id>`: reloads the specified mod (disables and enables it, performs injections again, and runs its `on_game_load` event)
- `luarun <code>`: runs plain lua code in the context of the game. Must be a one-liner though, multiline input is not supported
- `money <add|remove|set> <amount>`: Sets the amount of money the player has.
- `sandbox`: Loads the sandbox scene which can be used to debug the UI
- `shortcuts`: prints the shortcuts (as seen above) to the console output.

## Logging information to the console

If you're a mod developer, you may want to print informations to the console. To that effect, the console comes with a `logging` API. Log messages will be visible here, and are duplicated in the appropriate, timestamped log file in the `logs/` directory in the balatro save directory.

Logging comes with 6 distinct log levels :

- `TRACE`: for the most verbose messages
- `DEBUG`: for debug messages, verbose but not too spammy either
- `INFO`: the default log level, for informative messages (displayed in blue)
- `WARN`: for warnings (displayed in orange)
- `ERROR`: for errors (displayed in red)
- `PRINT`: for messages you want printed to the console as is, without any extra metadata (such as logger name, timestamp or color)

Use the `--log-level=TRACE` command line argument when starting balatro (with balamod) to change the minimum level a message must be to be displayed in the console. The default log level is `INFO`.
