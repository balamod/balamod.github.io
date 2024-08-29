# joker

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

### joker.add(args:table) -> table, table

Adds a joker to the game.

Takes args:
- mod_id, string: The ID of the mod this joker will be attached to.
- id, string: The internal name (ID) of the joker. Joker IDs commonly begin with `j_` (i.e `j_joker`, `j_my_custom_joker`)
- name, string: The displayed name of the joker. This is the name that users will see.
- calculate_joker_effect, function: The function that gets called when any joker-calculating scenario happens. Refer below for more information.
- cost, int: The price of the joker when it appears in the shop
- config, table: A table that contains data about the joker. Some values in config get saved in `card.ability`. Refer below for more information.
- desc, table: The description of the joker. Refer below for more information.
- rarity, int or string: The rarity of the joker. 1 = Common, 2 = Uncommon, 3 = Rare, 4 = Legendary. Custom rarities can be added, refer below for more information
- blueprint_compat, boolean: Determines whether blueprint and brainstorm will show this as incompatible or not. ***This is only visual!***
- no_pool_flag, string: If this string exists as a key in `G.GAME.pool_flags`, then this card will no longer appear.
- yes_pool_flag, string: This card will only appear if this string exists as a key in `G.GAME.pool_flags`
- alerted, boolean: **Strongly suggest leaving this as `nil` or `true`** Whether the joker will have the red notification on it or not. False = has the notification, True = does not have the notification.
- loc_vars, function: A function that returns a table of variables that are displayed in the description. Refer to the description information section for help.
- unlock_condition_desc, table: The description of the joker while it is locked. Formatted the same as a standard description.
- calculate_dollar_bonus_effect, function: A function that gets called after a blind is defeated, when calculating money earned. Returns an `int`, representing the money this card grants. Refer below for more information.
- add_to_deck_effect, function: A function that gets called when this joker is added to your deck through any method. Refer below for more information
- remove_from_deck_effect, function: A function that gets called when this joker is removed from your deck through any method. Refer below for more information.
- extra: A variable that gets saved to `card.config.center.balamod.extra`. 
~~~admonish warning
The following are experimental and may be buggy.
~~~
- unlocked, boolean: Whether the joker starts locked or unlocked in a new profile. 
- discovered, boolean: Whether the joker starts discovered or undiscovered in a new profile.
- effect, string: A description of the effect. This feature may do nothing and is safe to ignore.
- eternal_compat, boolean: Whether the eternal modifier can appear on this joker or not
- perishable_compat, boolean: Whether the perishable modifier can appear on this joker or not
- unlock_condition, table: A table that describes how to unlock this joker. Refer below for more information.
- enhancement_gate, string: The ID of the card modifier this joker needs to appear. 
- tooltip, table: Tooltips that get displayed alongside the description. **Refer below for formatting**



### joker.remove(id: string) -> nil

Removes a *modded* joker from the game. Requires `id`, the one passed as `args.id` in `joker.add`

## Extra Information

### Example
The following example adds a joker card that is functionally "Joker" from vanilla Balatro, but named "Jimbo, but modded"
```lua
joker.add{
  id = "j_joker_name_moddername", -- Recommended to add your name or a unique ID to the ID to prevent issues from same IDs.
  name = "Jimbo, but modded", -- The display name
  desc = {
    "{C:mult}+#1#{} Mult" -- Refer below for description formatting
  },
  cost = 2, -- Costs $2
  rarity = 1, -- Common joker
  config = {extra = {mult = 4}}, -- Refer below for information on config
  loc_vars = function(card) 
    return {card.ability.extra.mult} -- #1# -> card.ability.extra.mult -> 4
  end,
  calculate_joker_effect = function(card, context) -- Refer below for detailed information on contexts
    if card.config.center.id == "j_joker_modded" and context.joker_main then -- Check if we're calculating this card, and if it's the joker scoring context
      return {
        message = localize{type='variable', key='a_mult', vars={card.ability.extra.mult}} -- "+4 Mult" quip
        mult_mod = card.ability.extra.mult -- +4 mult
      }
    end
  end,
}
```

### Effect functions

These functions are called during various events in the game. The most commonly called one is `calculate_joker_effect`, under a large breadth of `context`'s. The following is a list of contexts that call `calculate_joker_effect`. Contrary to the name, `calculate_joker_effect` is not only called on jokers, but also consumables in `context.joker_main`. When writing your own `calculate_joker_effect`, check for your joker's id, and the context you want it to activate. Example above.
| Key | Description | Info | Vanilla Example
|-|-|-|-|
|`individual`| When calculating an individual playing card, either in hand, or played. | `context.cardarea` == `G.hand` if calculating cards in hand, `G.play` if calculating played cards<br> `context.full_hand` == Table of cards in played hand <br> `context.scoring_hand` == Table of scored cards in played hand <br> `context.scoring_name` == Name of hand type played <br> `context.poker_hands` == All hand types included in played hand <br> `context.other_card` == A playing card. Iterates through the cards in the `cardarea` | too many to list, check `card.lua` in base game source code
|`repetition`| When calculating repetitions. Required to return a table with at least repetitions: `{repetitions:int}` | too many to list, check `state_events.lua` in base game source code. | Sock and Buskin, Hanging Chad, Dusk, Seltzer, Hack, Mime
|`joker_main`| During the joker scoring phase. Also includes consumables. | `context.cardarea` == `G.jokers`<br> `context.full_hand` == Table of cards in played hand <br> `context.scoring_hand` == Table of scored cards in played hand <br> `context.scoring_name` == Name of hand type played <br> `context.poker_hands` == All hand types included in played hand | Observatory
|`discard`| When discarding cards. Called once per discarded card | `context.other_card` == A discarded card. Iterates through discarded cards<br>`context.full_hand` == A table of all discarded cards. | Ramen, Trading Card, Castle, Mail-In Rebate, Hit The Road, Green Joker, Yorick, Faceless Joker
| `blueprint` | Whether the current calculate_joker is being called by a Blueprint or Brainstorm. Add `not context.blueprint` if your card is incompatible with Blueprint or Brainstorm. | |
| `open_booster` | When opening a booster pack. | `context.card` == `card` | Hallucination
| `buying_card` | When buying a **VOUCHER**. | `context.card` == `card` | Unused in vanilla Balatro.
| `selling_self` | When this card is getting sold. | No additional data passed. |Luchador, Diet Cola, Invisible Joker
| `selling_card` | When another card is getting sold. | `context.card` == The card getting sold | Campfire
| `reroll_shop` | When the shop gets rerolled. | No additional data passed. | Flash Card
| `ending_shop` | When exiting the shop. | No additional data passed. | Perkeo
| `skip_blind`| When skipping a blind | No additional data passed. | Throwback
|`skipping_booster`| When skipping a blind | No additional data passed. | Red Card
|`playing_card_added`| When a playing card is added to the deck | `context.cards` == Table of playing cards added to the deck | Hologram
|`first_hand_drawn`| When the first hand is drawn against a Blind. | No additional data passed. | Certificate, DNA, Trading Card, Chicot, Madness, Burglar, Riff-Raff, Cartomancer, Ceremonial Dagger, Marble Joker
|`destroying_card`| After hand is scored. Called multiple times, once per played card. | `context.destroying_card` == A playing card that was scored <br> `context.full_hand` == Table of cards in played hand | Sixth Sense
|`remove_playing_cards`|  When a playing card is destroyed by another card | `context.cardarea` == nil if destroyed by a consumable, `G.jokers` if destroyed by a joker. <br> `context.destroyed` == Table of cards destroyed | Caino, Glass Joker
|`using_consumeable`| When using a consumable | `context.consumeable` == The consumable used | Fortune Teller, Constellation, Glass Joker (When using Hanged Man)
|`debuffed_hand`| When a hand type that is not allowed is played (e.g Playing a 4 card hand against the Psychic). | `context.cardarea` == `G.jokers`<br>`context.full_hand` == Table of cards in played hand<br>`context.scoring_hand` == Table of scored cards in played hand<br>`context.scoring_name` == Name of hand type played<br> `context.poker_hands` == All hand types included in played hand  | Matador
|`pre_discard`| Before a hand is discarded | `context.full_hand` == Table of cards in discarded hand<br>`context.hook` == If the discard was forced by The Hook blind | Burnt Joker
|`end_of_round`| After exiting a blind, by either defeating it, or by game over. When defeating a blind, its called multiple times, once per card in hand. If you want your joker to proc once, after defeating a blind, use `(not context.individual and not context.repetition)` | `context.cardarea` == `G.hand`<br>`context.other_card` == A card in hand. Iterates through the hand per call.<br>`context.individual` == When not calculating repetitions.<br>`context.repetition` == When calculating repetitions of playing cards with end of round effects<br>`context.repetition_only` == Only when checking for red seal<br>`context.card_effects` == When calculating repetitions, the effect that has procced. (i think?) | Campfire, Rocket, Turtle Bean, Invisible Joker, Popcorn, Egg, Gift Card, To Do List, Mr Bones
|`game_over`| If a game over would happen | `context.end_of_round` == true | Mr Bones
|`cards_destroyed`| ***Never called***. Likely an artifact of `remove_playing_cards`. | - | Caino, Glass Joker

In scoring contexts and some others, you may return a table with the following keys for various effects:
| Key | Effect |
|-|-|
| `message`: string | A little quip with `message` will pop up near `card`. If `card` is not defined, or not required, it will pop up near whatever card is returning this |
| `colour`: table | The colour that `message` will be in. Check `globals.lua` for colours |
| `delay`: float | Delay `message` by this many seconds |
| `extra`: table | Used to return an `Event`, by returning `{func: function}`. Message may be placed inside of `extra`. |
| `remove`: boolean | Whether to destroy hand or not. Exists in `context.discard` (Not really certain on this one) |
| `saved`: boolean | Whether to cancel the upcoming `context.game_over` or not. Exclusive to Mr Bones. (Not really certain on this one) |
| `level_up`: boolean | Whether to level up played hand or not. Used by Space Joker |
| `playing_cards_created`: table | Whether a playing card was created or not. Used by DNA |
| `Xmult_mod`: int | Multiplies current Mult by `Xmult_mod` |
| `mult_mod`: int | Adds `mult_mod` to current Mult |
| `chip_mod`: int | Adds `chip_mod` to current Chips |
| `x_mult`: int | Used in `context.individual`. Current card gives an additional `x_mult` XMult |
| `chips`: int | Used in `context.individual`. Current card gives an additional `chips` Chips |
| `mult`: int | Used in `context.individual`. Current card gives an additional `mult` Mult |
| `dollars`: int | Used in `context.individual`. Current card gives $`dollars` |
| `h_mult`: int | Used in `context.individual` and `context.cardarea == G.hand`. Current card gives `h_mult` Mult |
| `repetitions`: int | Used in `context.repetition`. Current card repeats `repetitions` times |

`calculate_dollar_bonus_effect` does not have any contexts. It will always be called after a blind is defeated. The following is an example `calculate_dollar_bonus_effect` function. It gives $10 after any blind is defeated.
```lua
calculate_dollar_bonus_effect = function(card)
    if card.config.center.id == "j_dollar_bonus_joker" then
        return 10
    end
end
```

`add_to_deck_effect` and `remove_from_deck_effect` only have 1 'context',  passed as "from_debuff". It is determined by whether the effect is being added/removed by debuffing a joker or by actually adding/removing the joker from the deck. The following is an example that gives $3 when its added to the deck, and $1 when it is debuffed, and $2 when it is no longer debuffed.
```lua
add_to_deck_effect = function(card, from_debuff)
  if card.config.center.id == "j_add_remove_joker" then
    if from_debuff then
      ease_dollars(2)
    else 
      ease_dollars(3)
    end
  end
end,
remove_from_deck_effect = function(card, from_debuff)
  if card.config.center.id == "j_add_remove_joker" and from_debuff then
    ease_dollars(1)
  end
end
```
### Config

`args.config` is partially saved into `card.ability`. Strongly suggest not using anything but `extra` for more control over your card, but its up to you. The following are keys that get saved and their effects.
| Key | Effect |
|-|-|
| `mult`: int | Additive Mult bonus |
| `Xmult`: float | Multiplicative Mult bonus |
| `type`: string | A hand type to check for |
| `t_mult`: int | Additive Mult bonus when `type` is played |
| `t_chips`: int | Additive Chips bonus when `type is played |
| `h_size`: int | Bonus to hand size (Can be negative) |
| `d_size`: int | Bonus to discard count |
| `extra`: table | Everything that gets passed into `config.extra` gets saved in `card.ability.extra`. |

### Description Formatting

The following is describes features you can use in your card description. For a full list of colours, go [here](https://balamod.github.io/ui-modding-basics.html).
```lua
desc = {
  "This is the first line of text",
  "This is the second line of text",
  "{C:red}Red{} is {C:red}red{}",
  "{S:2.0}This{} is twice as large",
  "#1# is the first variable in the table returned by loc_vars",
  "{C:green}#2#{} is the second variable in the table returned by loc_vars", 
},
loc_vars = function(card)
  return {"This", "Green"}
end
```

### Custom Rarities

~~~admonish warn
This feature is experimental. You will encounter various bugs while using this.
~~~
You can add custom rarities by having the following code in your `on_enable` function, before you add your cards with this rarity. ***Cards of these rarities WILL NOT naturally show up in the game***. Replace `{customrarity}` with a name or number of your choice. Replace `{hexcode}` with a hexcode of a colour of your choice.
```lua
  -- where your cards of this rarity will be saved
  G.P_JOKER_RARITY_POOLS["{customrarity}"] = {} 

  -- to display the rarity badge
  local to_replace = [[localize%('k_legendary'%)]]
  local replacement = [[localize%('k_legendary'%), {customrarity}="Custom Rarity"]]
  local file_name = "functions/UI_definitions.lua"
  local fun_name = "G.UIDEF.card_h_popup"
  inject(file_name, fun_name, to_replace, replacement) 

  -- colour of the rarity badge
  G.C.RARITY["{customrarity}"] = HEX("{hexcode}") 
```

### Unlock Conditions

~~~admonish warn
This feature is experimental.
Known issue: Restarting the game will re-lock modded jokers that were unlocked
~~~

All the `"strings"` are unlock 'types', the sub-points are what goes along with the unlock type.

Example: `{unlock_condition = {type = 'modify_jokers', extra = {polychrome = true, count = 2}}}`
- `"modify_jokers"`: add enhancements to jokers (Bootstraps)
    - `extra`:
        - `polychrome`: bool: check for polychrome modifiers
        - `count`: int: number of modifiers to look for
- `"c_cards_sold"`: sell centers (Burnt Joker)
    - `extra`: int: number of centers sold
- `"discover_amount"`: discover cards in the following collections (Astronomer, Cartomancer)
    - `planet_count`: how many planets
    - `tarot_count`: how many tarots
- `"modify_deck"`: modify playing cards (Driver's License, Glass Joker, Onyx Agate, Arrowhead, Bloodstone, Rough Gem, Smeared Joker)
    - `extra`:
        - `count`: int: how many modified playing cards
        - `tally`: str: 'total', all modification types
        - `enhancement`: str: 'Glass Card' 'Wild Card', type of modification
        - `e_key`: str: 'm_glass' 'm_wild', the P_CENTER key of the modification
        - `suit`: str: Suit of cards in the deck
- `"play_all_hearts"`: play all heart cards in your deck in 1 round (Shoot the Moon)
- `"money"`:  have a certain amount of money (Sateillite)
    - `extra`: int: amount of money
- `"discard_custom"`: discard a certain hand type (unsure how to define) (Brainstorm, Hit the Road)
- `"win_custom"`: win while doing a certain thing (unsure how to define) (Invisible Joker, Blueprint)
- `"chip_score"`: play a hand that gives a certain amount of chips (Stuntman, The Idol, Oops! All 6s)
    - `chips`: int: the amount of chips to have to unlock
- `"win_no_hand"`: win without playing a certain hand type (The Duo, The Trio, The Family, The Order, The Tribe)
    - `extra`: str: define the hand type that was not played: 'Pair', 'Three of a Kind', 'Four of a Kind', 'Straight', 'Flush'
- `"hand_contents"`: play a certain hand (Seeing Double, Golden Ticket)
    - `extra`: str: the hand: 'four 7 of Clubs' 'Gold'(5 gold cards)
- `"win`": win within a certain number of rounds (Merry Andy, Wee Joker)
    - `n_rounds`: int: the amount of rounds to win before
- `"ante_up"`: reach a certain ante (Flower Pot, Showman)
    - `ante`: int: the ante to reach
- `"round_win"`: win in 1 round with no discards(Matador)
    - `extra`: 'High Card', adds condition of certain hand type (Hanging Chad)
    - `extra`: int: win in 1 round this many times (this might allow discards) (Troubadour)
- `"continue_game"`: Continue a saved run from the main menu (Throwback)
- `"double_gold"`: Have a gold seal on a gold card (Certificate)
- `"c_jokers_sold"`: Sell jokers (Swashbuckler)
    - `extra`: int: how many jokers
- `"c_face_cards_played"`: play face cards (Sock and Buskin)
    - `extra`: int: how many face cards
- `"c_hands_played"`: play hands (Acrobat)
    - `extra`: int: how many hands
- `"c_losses"`: lose runs (Mr. Bones)
    - `extra`: int: how many runs


### Tooltips
~~~admonish warn
This feature is experimental.
~~~

Tooltips currently do not support loc_vars. Tooltips are formatted as follows.
```lua
tooltip = {
  {
    name = "Name of the first tooltip",
    text = {
      "First line of the first tooltip",
      "Second line of the first tooltip",
    }
  },
  {
    name = "Name of the second tooltip",
    text = {
      "First line of the second tooltip",
    }
  },
},
```

### Common Mistakes

If your joker crashes the game with an error saying `'for' limit must be a number` in `state_events.lua`, make sure you filter out `context.repetition`

If you change values in `card.config.center.config`, it may affect all instances of the card, rather than just the instance you're accessing it through. Use `card.ability` to only edit `card`.