# Contributing Guide

This guide is intended to help you get started with contributing to the game mod-loader. If you have any questions, feel free to ask in the [Discord server](https://discord.gg/p7DeW7pSzA).

## Creating a Pull Request

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a new branch for your changes.
4. Make your changes.
5. Commit your changes.
6. Push the changes to your fork.
7. Create a pull request.

## Add mods to the in-game mod gallery

There's now a rest or "marketplace" system integrated directly into balamod via the mod menu. You can add your mods via the [indexes](https://github.com/balamod/mods/blob/main/index.json)
For the moment there's only one because I'm going to try and regulate malicious mods and the like, but there's bound to be many more in the future.
If you want to add your mod to an index, make a pull request to the index and add your mod to the bottom of the `index.json` file.

There are a few rules to follow when adding your mod to the index:
- The id of the mod must be unique and can only contain lowercase letters, underscores and hyphens.
- The version must be a valid semantic version matching the format `x.y.z`.

The format is as follows:

```json
  {
  "url": "https://github.com/you/my_cool_mod",
  "id": "my_cool_mod",
  "name": "My cool mod",
  "description": [
    "A really cool mod"
  ],
  "version": "1.0.0",
  "load_before": [],
  "load_after": [],
  "authors": [
    "You"
  ]
}
```
