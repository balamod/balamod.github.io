# utils

## GLOBALS

## CLASSES

## VARIABLES

## FUNCTIONS

### `contains(t: table, element: any) -> boolean`

Returns true if `t` contains `element`, based on the `==` operator

<!-- lua: https://github.com/balamod/balamod_lua/blob/main/src/utils.lua#L7 -->

### `filter(t: table, predicate: function(e: any) -> boolean) -> table`

Filters table `t` based on whether `predicate(element)` is true for each element of `t`

### `map(t: table, mapper: function(element: any) -> any) -> table`

Maps each element of table `t` with `mapper`. Returns the new table.

### `reduce(t: table, reducer: function(previous: any, current: any), initial: any) -> any`

Reduces table `t` using the reducer `reducer`. `initial` is `nil` by default.

### `parseVersion(version: string) -> Version`

Parses a semantic version string into its components

### `v2GreaterThanV1(v1: string, v2: string) -> boolean`

Returns true if v2 is after v1, false otherwise. Used to check for updates most notably.

## CLASSES

### `Version`

#### ATTRIBUTES

- major: number
- minor: number
- patch: number
