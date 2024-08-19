# logging

<!-- toc -->

## GLOBALS

### `LOGGERS`: table

Table mapping a logger's name to its Logger instance

### `START_TIME`: int

Timestamp, in seconds, of the start of the game.

## ENUMS

### `LogLevel`

- TRACE
- DEBUG
- INFO
- WARN
- ERROR
- PRINT

## CLASSES

### `Logger`

#### ATTRIBUTES

- name: string
- log_levels: table[LogLevel, number]
- level: LogLevel
- numeric_level: number
- messages: Message[]

#### METHODS

##### `log(level: LogLevel, ...) -> nil`

Function used internally to log messages with a given log level. Arguments following the level are transformed into strings, then concatenated together with a space separating them. Tables are serialized in a way that makes them compatible with the LUA interpreter. Functions are serialized as the string `"function"`, and `nil` as the string `"nil"`

##### `trace(...) -> nil`

Alias for `Logger:log("TRACE", ...)`

##### `debug(...) -> nil`

Alias for `Logger:log("DEBUG", ...)`

##### `info(...) -> nil`

Alias for `Logger:log("INFO", ...)`

##### `warn(...) -> nil`

Alias for `Logger:log("WARN", ...)`

##### `error(...) -> nil`

Alias for `Logger:log("ERROR", ...)`

##### `print(...) -> nil`

Alias for `Logger:log("PRINT", ...)`

The print log level is special in that it does not format the message as a regular log, and does not serializes the message to the disk. It is to be used to display information to the development console in game.

### `Message`

#### ATTRIBUTES

- level: LogLevel
- level_numeric: number
- text: string
- time: number
- name: string

#### METHODS

##### `formatted(dump: bool) -> string`

Formats the message into a string to dump to the console, or to dump to a file. The format is as follows:

- `[$loggerName] - $messageLevel :: $messageText` if dump == false

- `$messageIsoDate [$loggerName] - $messageLevel :: $messageText` if dump == true

## FUNCTIONS

### `getLogger(name: string) -> Logger`

Gets a logger, and creates one if name does not exist in the `LOGGERS` table

<!-- lua: https://github.com/balamod/balamod_lua/blob/main/src/logging.lua#L78 -->

### `saveLogs() -> nil`

Serializes all logs to the disk.

<!-- lua: https://github.com/balamod/balamod_lua/blob/main/src/logging.lua#L121 -->

### `getAllMessages() -> Message[]`

Returns all logged messages, in order from oldest to newest.

<!-- lua: https://github.com/balamod/balamod_lua/blob/main/src/logging.lua#L88 -->

### `clearLogs() -> nil`

Deletes all log messages.

<!-- lua: https://raw.githubusercontent.com/balamod/balamod/master/src/dependencies/logging.lua#clearLogs -->
