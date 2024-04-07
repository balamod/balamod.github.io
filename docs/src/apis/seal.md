# seal

<!-- toc -->

## GLOBALS

~~~admonish info
This module does not expose any global variables.
~~~

## CLASSES

~~~admonish info
This module does not expose any classes.
~~~

## FUNCTIONS

### seal.registerSeal(args: table)

Takes args:
- mod_id, string: The ID of the mod this seal will be attached to.
- id, string: The name of the seal object with no spaces and no "_seal" at the end. The "_seal" suffix will be added later automatically.
- label, string: The name of the seal as you wish for it to appear in game.
- color, string: The color of the seal's badge and text. Refer to the color list [here](https://balamod.github.io/ui-modding-basics.html).
- description, table: The text description for the object. Check the provided example at the bottom.
- shader, string: The name of the shader to apply to the seal on render. Valid options are:
    - dissolve (the default shader)
    - voucher (like the one Gold seals use)
    - negative
    - holo
    - foil
    - polychrome
    - hologram (works, but has almost no visible effect)
    - vortex (works, and looks hilarious, but probably not a good idea to use)
- timing, string: Denotes the game action where this seal should trigger. Valid options are:
    - onDiscard: triggers when discarding a card.
    - onHold: triggers when holding a card at the end of round.
    - onEval: triggers when playing a card
    - onDollars: triggers only when Gold Seal would otherwise trigger, and must return a number.
    - onRepetition: triggers only when Red Seal would trigger, and must return a table containing:
        - message, a string
        - repetitions, an int
        - "card = self"
- effect, function: A function containing all the conditionals and effects of a particular seal. Examples for a few of the timings are below.

### seal.unregisterSeal(id)

Pass a seal `id`, and it will be removed from the game. Generally, place this in `on_disable`.

### seal.addSealInfotip(set: string, name: string, seal_id: string)

For any consumeables or jokers that might reference a custom seal object, use this function to add in the extra tooltip containing the seal's description.
- set: the name of the set you're using this for, like "Spectral" or "Joker"
- name: the name of the item you're using this with, such as "Deja Vu" or "Certificate"
- seal_id: the id of the seal you want this to refer to. Identical to the `id` attribute from `registerSeal`

## Usage Examples

### Descriptions

`{C:[colorname]}[text]{}` is used for colored text. Colors are available [here](https://balamod.github.io/ui-modding-basics.html).
Line breaks are placed in between text objects.

```lua
description = {"Earn {C:money}$6{} when this", "card is played", "and scores"}
description = {"Creates 2 {C:planet}Planet{} cards", "if this card is {C:attention}held{} in", "hand at end of round", "{C:inactive}(Must have room)"}
description = {"Retrigger this", "card {C:attention}2{} times"}
description = {"Creates 2 {C:tarot}Tarot{} cards", "when {C:attention}discarded.", "{C:inactive}(Must have room)"}
description = {"Creates 2 {C:spectral}Spectral{} cards", "if this card is {C:attention}held{} in", "hand at end of round"}
```

### Effects

```lua
local function sealEffectGold(self) --Uses the onDollars timing.
    local ret = 0
    if self.seal == 'DoubleGold' then
        ret = ret + 6
    end
    return ret
end

local function sealEffectRed(self, context) --Uses the onRepetition timing. Note that "if context.repetition then" is still required.
    if context.repetition then
        if self.seal == 'DoubleRed' then
            return {
                message = localize('k_again_ex'),
                repetitions = 2,
                card = self
            }
        end
    end
end

local function sealEffectPurple(self, context) --Uses the onDiscard timing. Note that "if context.discard then" is still required.
    if context.discard then
        if self.seal == 'DoublePurple' and #G.consumeables.cards + G.GAME.consumeable_buffer <
            G.consumeables.config.card_limit then
            for i = 1, math.min(2, G.consumeables.config.card_limit - #G.consumeables.cards) do
                G.GAME.consumeable_buffer = G.GAME.consumeable_buffer + 1
                if #G.consumeables.cards + G.GAME.consumeable_buffer > G.consumeables.config.card_limit then
                    break
                end
                G.E_MANAGER:add_event(Event({
                    trigger = 'before',
                    delay = 0.0,
                    func = (function()
                        local card = create_card('Tarot', G.consumeables, nil, nil, nil, nil, nil, 'pplsl')
                        card:add_to_deck()
                        G.consumeables:emplace(card)
                        G.GAME.consumeable_buffer = 0
                        return true
                    end)
                }))
            end
            card_eval_status_text(self, 'extra', nil, nil, nil, {
                message = "+2 Tarot",
                colour = G.C.PURPLE
            })
        end
    end
end

local function sealEffectBlue(self, context) --Uses the onHold timing.
    local ret = {}
    if self.seal == 'DoubleBlue' and #G.consumeables.cards + G.GAME.consumeable_buffer <
        G.consumeables.config.card_limit then
        local card_type = 'Planet'
        for i = 1, math.min(2, G.consumeables.config.card_limit - #G.consumeables.cards) do
            G.GAME.consumeable_buffer = G.GAME.consumeable_buffer + 1
            if #G.consumeables.cards + G.GAME.consumeable_buffer > G.consumeables.config.card_limit then
                break
            end
            G.E_MANAGER:add_event(Event({
                trigger = 'before',
                delay = 0.0,
                func = (function()
                    local card = create_card(card_type, G.consumeables, nil, nil, nil, nil, nil, 'blusl')
                    card:add_to_deck()
                    G.consumeables:emplace(card)
                    G.GAME.consumeable_buffer = 0
                    return true
                end)
            }))
        end
        card_eval_status_text(self, 'extra', nil, nil, nil, {
            message = "+2 Planet",
            colour = G.C.SECONDARY_SET.Planet
        })
        ret.effect = true
    end
end
```
