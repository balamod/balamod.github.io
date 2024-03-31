# assets

<!-- toc -->

## GLOBALS

~~~admonish info
This module does not expose any global variables
~~~

## CLASSES

~~~admonish info
This module does not expose any classes
~~~

## FUNCTIONS

### `assets.getAtli(modId: string, textureScaling: int) -> table`

This function gets the atli (plural of atlas) required to inject into `G.ASSET_ATLAS` and `G.ANIMATION_ATLAS`

Atli are loaded from images placed in the `mods/${modId}/assets/textures/${textureScaling}x/` folder. Each image in that folder will be its own atlas, with the atlas key being `${modId}_${fileName}` (without the extension)

Each file should contain a single image, whether it's a joker, a tarot card, or other asset. Each asset should be named according to its center ID. Asset type is determined by the prefix of the file, here is a list of the supported prefixes:

- b: Card back (deck)
- v: Voucher
- j: Joker
- e: Edition
- c: Consumable
- p: Booster
- m: Enhancer
- t: Tag
- card: Card (Playing card)
- chip: Chip
- blind: Blind
- sticker: Sticker

For now, only assets of type `Blind` are animated, with 21 frames of animation.
