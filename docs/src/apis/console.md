# console

<!-- toc -->

## GLOBALS

~~~admonish info
This module does not expose any global variables
~~~

## VARIABLES

### `logger: Logger`

Instance of a `logging.Logger` object, dedicated to the console

### `log_level: LogLevel`

The minimum log level for which the console will log messages.

Defaults to `"INFO"`

### `is_open: boolean`

Whether the console is currently open

### `cmd: string`

String representation of the command promt. Always starts with the characters "`> `"

### `line_height: int`

Height of a line in pixels

### `max_lines: int`

Max amount of lines displayable in the console

### `start_line_offset: int`

The integer offset at which to start logging lines

### `history_index: int`

Index of the currently selected history command. Starts at 0 and increments by one on each press of the up arrow, decrements on each press of the down arrow

### `command_history: Array<string>`

Table of commands in the history

### `history_path: string`

Path relative to `BALATRO_SAVE_DIRECTORY` at which to save the history to

### `modifiers: Map<string, boolean>`

Table representing which key modifiers are active at a certain point in time.

Has the following keys :

- `capslock`
- `scrolllock`
- `numlock`
- `shift`
- `ctrl`
- `alt`
- `meta`

Each key should be self explanatory. The `meta` modifier refers to either, depending on the system:

- the windows key
- the apple "command" key

Lock keys (i.e. `scrolllock`, `capslock` and `numlock`) are toggleable. The game has no way to check whether the game was started with the key toggled on/off, and its state will be toggled on release of the corresponding key. This means that the state of these keys is undefined. If the state is true, it means the corresponding key has been pressed during the lifetime of the game, if the state is false it means that the state of the key is the same as the state it was when the game was first started.

### `commands: Map<string, Command>`

Commands registered with `registerCommand` are stored here.

## FUNCTIONS

### `toggle(self) -> nil`

Toggles the console on/off. When the console is toggled on, the `love.textinput` callback gets assigned an anonymous function to capture the text written accurately in the command prompt. The `love.textinput` function is unassigned (set to `nil`) when the console is toggled off.

### `longestCommonPrefix(self, strings: Array<string>) -> string`

Returns the longest common prefix from a set of strings, e.g.

```lua
local prefix = console:longestCommonPrefix({"state", "status", "stars"})
print(prefix)
-- Prints "sta"
```

This function is used internally by the autocompletion engine of the developer console.

### `tryAutocomplete(self) -> string`

Tries to autocomplete a command. For the first part of the command, the command name, the autocompletion is handled by looking at the typed command, and checking which registered commands match the prefix typed.

For subsequent arguments, the `Command.autocomplete(current_arg, previous_args)` function is called with the current partial argument, and all previous arguments, in order from "left to right".

When several matches are found, instead of not completing, the autocomplete engine will return the longest common prefix between all potential command matches.

### `getMessageColor(self, message: Message) -> Tuple<float, float, float>`

Returns a 3-tuple of numbers between 0 and 1 (inclusive) corresponding to the `R`, `G` and `B` color the message should be printed as.


| LogLevel | Color (hex) | Color (tuple)  |                                        Color                                         |
| :------- | :---------: | :------------: | :----------------------------------------------------------------------------------: |
| PRINT    |  `#FFFFFF`  |  `(1, 1, 1)`   | <span style="background-color:#FFFFFF;width:100%;height:2rem;display:block;"></span> |
| INFO     |  `#00E6FF`  | `(0, 0.9, 1)`  | <span style="background-color:#00E6FF;width:100%;height:2rem;display:block;"></span> |
| WARN     |  `#FF8000`  | `(1, 0.5, 0)`  | <span style="background-color:#FF8000;width:100%;height:2rem;display:block;"></span> |
| ERROR    |  `#FF0000`  |  `(1, 0, 0)`   | <span style="background-color:#FF0000;width:100%;height:2rem;display:block;"></span> |
| DEBUG    |  `#2900FF`  | `(0.16, 0, 1)` | <span style="background-color:#2900FF;width:100%;height:2rem;display:block;"></span> |
| TRACE    |  `#FFFFFF`  |  `(1, 1, 1)`   | <span style="background-color:#FFFFFF;width:100%;height:2rem;display:block;"></span> |

### `getFilteredMessages(self) -> Array<Message>`

Returns, amongst all of the log messages, the messages matching a log level greater than, or equal to the console's log level.

### `getMessagesToDisplay(self) -> Array<Message>`

Returns a table with all of the messages currently *on screen*

The array should **always** be of length `console.max_lines`, with a padding of `Message("PRINT", "")` if necessary


### `modifiersListener(self) -> nil`

Listener for changes in modifiers (see [modifiers](#modifiers-mapstring-boolean)). When either the `ctrl` or `meta` modifiers is on, then the textinput callback is temporarily disabled. This is so that typing shortcuts in the console doesn't interfere with text input in the command prompt.

### `typeKey(self, key_name: string) -> nil`

Callback used by the `dev_console` mod when `on_key_pressed` is called. This is the function responsible for handling the following shortcuts:

- `meta + C` or `ctrl + C` : copies the current typed command into the clipboard
- `meta + shift + C` or `ctrl + shift + C`: Copies all formatted logs on screen into the clipboard
- `meta + V` or `ctrl + V`: pastes the contents of the clipboard into the command prompt, concatenating it to the existing prompt.
- `escape`: close the console
- `delete` or `meta + backspace`: clears the command prompt
- `end` or `meta + left`: moves the text to the latest log message printed
- `home` or `meta + right`: moves the text to the first log message
- `pagedown` or `meta + down`: moves the text `console.max_lines` down
- `pageup` or `meta + up`: moves the text `console.max_lines` up
- `up`: navigates up in the history (previous commands)
- `down`: navigates down in the history (towards more recent commands)
- `tab`: tries completing the current command using the autocompletion engine
- `backspace`: delete a character
- `return` or `kp_enter`: submit the command
  - command return value defines whether the command is saved to history or not. A truthy return value (`true`) will add the command to history. Failed commands are not saved.

### `addToHistory(self, command: string) -> nil`

Adds a non empty command to the `self.command_history` array, resets `self.history_index` to 0 and saves the history to a file.

### `registerCommand(self, name: string, callback: function(args: Array<string>)->boolean, short_description: string, autocomplete: function(current_arg: string, previous_args: Array<string>)->Array<string>, usage: string)->nil`

Creates a new `Command` object and saves it to the `self.commands` map.

`name` is the command name. Self-explanatory, it's just what the user will type in the prompt to run your command.

`callback` is the callback. It's a simple lua function that will be called with the rest of the arguments passed in as input when the command is submitted. If the command finished successfully, return `true`, return `false` otherwise. This will control whether the command gets added to the history or not.

~~~admonish warning
If your command contains sensitive information as arguments (passwords, API tokens, etc), then it should never return `true` because the history is saved as plain text.

A bad actor could read the history file and figure out sensitive info from it.
~~~

`short_description` is just a string that will be printed when the built-in `help` command is run.

`autocomplete` is a simple lua function that should return a completion based on the current argument, and maybe the list of previous arguments.
This function should return a table of suggested completions. The function [`console:longestCommonPrefix`](#longestcommonprefixself-strings-arraystring---string) will be then called amongst all those completions to fill in the maximum amount of characters.

`Usage` is just the usage string. The intent is to eventually automate bad usage error messages, but this is unused right now.

### `removeCommand(self, cmd_name: string) -> nil`

Removes a command. Call this function in your `on_disable` hook to make sure that your mod's commands are not included if the mod is disabled

### `wrapText(self, message: string, screenWidth: int) -> Array<string>`

Wraps the text to fit within `screenWidth` pixels.

## CLASSES

### `Command`

#### ATTRIBUTES

- `call`: `function(args) -> boolean`, the callback for the command
- `desc`: `string`, the help text for the command, its description
- `autocomplete`, `function(current_arg, previous_args) -> Array<string>`, the autocomplete for the command
- `usage`: `string`, the usage text for the command
