# UI Modding Basics

Balatro comes with a built-in UI framework that draws most of the elements of the game. It may seem hard to grasp at first but it's actually quite simple in its structure.

## The `G.FUNCS` and `G.UIDEF` tables

The game uses 2 tables for the UI.

### `G.FUNCS`

It's the table that holds all of the UI callbacks. Basically, whenever you click on a button, its associated to a function defined here. Functions in `G.FUNCS` match the following signature, the `UIElement` class being defined in `engine/ui.lua` :

```lua
function(element: UIElement) -> nil
```

### `G.UIDEF`

It's the table that holds the UI definitions for the game. An UI definition is a function that returns a table that has a very strict structure:

```lua
G.UIDEF.my_ui_definition = function(element)
    return {
        n = G.UIT.ROOT,
        config = {},
        nodes = {}
    }
end
```

Let's break this down:

- `n = G.UIT.ROOT`: n here represents the node "type". There are several node types available in Balatro
  - `T`, which is for text nodes
  - `B`, for boxes (which can be rounded)
  - `C`, for column layouts
  - `R`, for row layouts
  - `O`, for objects (such as cards and such)
  - `ROOT`, for the root node of an UI definition
- `config`: configuration for the node, holds several attributes, each for configuring alignments, or button behavior for instance
- `nodes`: is an array of child nodes

Think of the Balatro UI definition like you would an HTML document. In HTML, you'd write something like this

~~~admonish example collapsed=false title="HTML example"
```html
<div>
  <input type="text"></input>
  <div>
    <span><p>Some Text</p></span>
    <span><p>Other Text</p></span>
  </div>
</div>
```
~~~

Which would roughly be equivalent to

~~~admonish example collapsed=false title="Example HTML equivalent for Balatro UI"
```lua
{
    n = G.UIT.ROOT,
    config = {},
    nodes = {
        {
            n = G.UIT.I,
            config = {},
        },
        {
            n = G.UIT.C,
            config = {},
            nodes = {
                {
                    n = G.UIT.R,
                    config = {},
                    nodes = {
                        {
                            n = G.UIT.T,
                            config = { text = "Some Text" }
                        },
                    },
                },
                {
                    n = G.UIT.R,
                    config = {},
                    nodes = {
                        {
                            n = G.UIT.T,
                            config = { text = "Other Text" }
                        },
                    },
                },
            },
        },
    },
}
```
~~~

## Configuration options for each UI type

### Common config options

### Text options

~~~admonish info
For text UI nodes, the following config table is expected, all values are optional (can be `nil`), unless specified otherwise.
~~~

- `config.text`, must be specified, unless `config.ref_table` and `config.ref_value` are both provided. The text to display. Type: `string`
- `config.colour`, defaults to `G.C.UI.TEXT_LIGHT` (which is white with full opacity, `#FFFFFFFF`)
- `config.scale`, defaults to `1`. Text scaling to apply to the text. Type: `float`
- `config.shadow`, defaults to `false`. Whether to draw a shadow behind the text. Type: `boolean`
- `config.focus_args`
- `config.ref_table`: a reference table, basically, the `text` value will be computed by looking up `config.ref_value` in `config.ref_table`.
- `config.ref_value`: the value to look up into the provided `config.ref_table`
- `config.func`
- `config.id`: An unique ID for the node
- `config.juice`
- `config.outline_colour`: Text outline colour

### Box options

### Column options

### Row options

### Object options

## Premade UI widget factories

The following functions are defined in `functions/UI_definitions.lua`, and use the concepts defined above
to make more complex UI elements.

### `create_slider(args) -> UIElement`

### `create_toggle(args) -> UIElement`

### `create_option_cycle(args) -> UIElement`

### `create_tabs(args) -> UIElement`

### `create_text_input(args) -> UIElement`

### `create_keyboard_input(args) -> UIElement`

## Enumerations

### Colours

Colors are specified in `globals.lua`, you can access them through the `G.C` table.

| Color Name             | Color (hex) | Color (tuple) |                                        Color                                         |
| :--------------------- | :---------: | :-----------: | :----------------------------------------------------------------------------------: |
| MULT                   |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| CHIPS                  |  `#009DFF`  |      `-`      | <span style="background-color:#009DFF;width:100%;height:2rem;display:block;"></span> |
| MONEY                  |  `#F3B958`  |      `-`      | <span style="background-color:#F3B958;width:100%;height:2rem;display:block;"></span> |
| XMULT                  |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| FILTER                 |  `#FF9A00`  |      `-`      | <span style="background-color:#FF9A00;width:100%;height:2rem;display:block;"></span> |
| BLUE                   |  `#009DFF`  |      `-`      | <span style="background-color:#009DFF;width:100%;height:2rem;display:block;"></span> |
| RED                    |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| GREEN                  |  `#4BC292`  |      `-`      | <span style="background-color:#4BC292;width:100%;height:2rem;display:block;"></span> |
| PALE_GREEN             |  `#56A887`  |      `-`      | <span style="background-color:#56A887;width:100%;height:2rem;display:block;"></span> |
| ORANGE                 |  `#FDA200`  |      `-`      | <span style="background-color:#FDA200;width:100%;height:2rem;display:block;"></span> |
| IMPORTANT              |  `#FF9A00`  |      `-`      | <span style="background-color:#FF9A00;width:100%;height:2rem;display:block;"></span> |
| GOLD                   |  `#EAC058`  |      `-`      | <span style="background-color:#EAC058;width:100%;height:2rem;display:block;"></span> |
| YELLOW                 | `#FFFF00FF` |      `-`      | <span style="background-color:#FFFF00;width:100%;height:2rem;display:block;"></span> |
| CLEAR                  | `#00000000` |      `-`      | <span style="background-color:#000000;width:100%;height:2rem;display:block;"></span> |
| WHITE                  | `#FFFFFFFF` |      `-`      | <span style="background-color:#FFFFFF;width:100%;height:2rem;display:block;"></span> |
| PURPLE                 |  `#8867A5`  |      `-`      | <span style="background-color:#8867A5;width:100%;height:2rem;display:block;"></span> |
| BLACK                  |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| L_BLACK                |  `#4F6367`  |      `-`      | <span style="background-color:#4F6367;width:100%;height:2rem;display:block;"></span> |
| GREY                   |  `#5F7377`  |      `-`      | <span style="background-color:#5F7377;width:100%;height:2rem;display:block;"></span> |
| CHANCE                 |  `#4BC292`  |      `-`      | <span style="background-color:#4BC292;width:100%;height:2rem;display:block;"></span> |
| JOKER_GREY             |  `#BFC7D5`  |      `-`      | <span style="background-color:#BFC7D5;width:100%;height:2rem;display:block;"></span> |
| VOUCHER                |  `#CB724C`  |      `-`      | <span style="background-color:#CB724C;width:100%;height:2rem;display:block;"></span> |
| BOOSTER                |  `#646EB7`  |      `-`      | <span style="background-color:#646EB7;width:100%;height:2rem;display:block;"></span> |
| EDITION                | `#FFFFFFFF` |      `-`      | <span style="background-color:#FFFFFF;width:100%;height:2rem;display:block;"></span> |
| DARK_EDITION           | `#000000FF` |      `-`      | <span style="background-color:#000000;width:100%;height:2rem;display:block;"></span> |
| ETERNAL                |  `#C75985`  |      `-`      | <span style="background-color:#C75985;width:100%;height:2rem;display:block;"></span> |
| DYN_UI.MAIN            |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| DYN_UI.DARK            |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| DYN_UI.BOSS_MAIN       |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| DYN_UI.BOSS_DARK       |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| DYN_UI.BOSS_PALE       |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| SO_1.HEARTS            |  `#F03464`  |      `-`      | <span style="background-color:#F03464;width:100%;height:2rem;display:block;"></span> |
| SO_1.DIAMONDS          |  `#F06B3F`  |      `-`      | <span style="background-color:#F06B3F;width:100%;height:2rem;display:block;"></span> |
| SO_1.SPADES            |  `#403995`  |      `-`      | <span style="background-color:#403995;width:100%;height:2rem;display:block;"></span> |
| SO_1.CLUBS             |  `#235955`  |      `-`      | <span style="background-color:#235955;width:100%;height:2rem;display:block;"></span> |
| SO_2.HEARTS            |  `#F83B2F`  |      `-`      | <span style="background-color:#F83B2F;width:100%;height:2rem;display:block;"></span> |
| SO_2.DIAMONDS          |  `#E29000`  |      `-`      | <span style="background-color:#E29000;width:100%;height:2rem;display:block;"></span> |
| SO_2.SPADES            |  `#4F31B9`  |      `-`      | <span style="background-color:#4F31B9;width:100%;height:2rem;display:block;"></span> |
| SO_2.CLUBS             |  `#008EE6`  |      `-`      | <span style="background-color:#008EE6;width:100%;height:2rem;display:block;"></span> |
| SUITS.HEARTS           |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| SUITS.DIAMONDS         |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| SUITS.SPADES           |  `#374649`  |      `-`      | <span style="background-color:#374649;width:100%;height:2rem;display:block;"></span> |
| SUITS.CLUBS            |  `#424E54`  |      `-`      | <span style="background-color:#424E54;width:100%;height:2rem;display:block;"></span> |
| UI.TEXT_LIGHT          | `#FFFFFFFF` |      `-`      | <span style="background-color:#FFFFFF;width:100%;height:2rem;display:block;"></span> |
| UI.TEXT_DARK           |  `#4F6367`  |      `-`      | <span style="background-color:#4F6367;width:100%;height:2rem;display:block;"></span> |
| UI.TEXT_INACTIVE       | `#88888899` |      `-`      | <span style="background-color:#888888;width:100%;height:2rem;display:block;"></span> |
| UI.BACKGROUND_LIGHT    |  `#B8D8D8`  |      `-`      | <span style="background-color:#B8D8D8;width:100%;height:2rem;display:block;"></span> |
| UI.BACKGROUND_WHITE    | `#FFFFFFFF` |      `-`      | <span style="background-color:#FFFFFF;width:100%;height:2rem;display:block;"></span> |
| UI.BACKGROUND_DARK     |  `#7A9E9F`  |      `-`      | <span style="background-color:#7A9E9F;width:100%;height:2rem;display:block;"></span> |
| UI.BACKGROUND_INACTIVE | `#666666FF` |      `-`      | <span style="background-color:#666666;width:100%;height:2rem;display:block;"></span> |
| UI.OUTLINE_LIGHT       |  `#D8D8D8`  |      `-`      | <span style="background-color:#D8D8D8;width:100%;height:2rem;display:block;"></span> |
| UI.TRANSPARENT_LIGHT   | `#EEEEEE22` |      `-`      | <span style="background-color:#EEEEEE;width:100%;height:2rem;display:block;"></span> |
| UI.TRANSPARENT_DARK    | `#22222222` |      `-`      | <span style="background-color:#222222;width:100%;height:2rem;display:block;"></span> |
| UI.HOVER               | `#00000055` |      `-`      | <span style="background-color:#000000;width:100%;height:2rem;display:block;"></span> |
| SET.DEFAULT            |  `#CDD9DC`  |      `-`      | <span style="background-color:#CDD9DC;width:100%;height:2rem;display:block;"></span> |
| SET.ENHANCED           |  `#CDD9DC`  |      `-`      | <span style="background-color:#CDD9DC;width:100%;height:2rem;display:block;"></span> |
| SET.JOKER              |  `#424E54`  |      `-`      | <span style="background-color:#424E54;width:100%;height:2rem;display:block;"></span> |
| SET.TAROT              |  `#424E54`  |      `-`      | <span style="background-color:#424E54;width:100%;height:2rem;display:block;"></span> |
| SET.PLANET             |  `#424E54`  |      `-`      | <span style="background-color:#424E54;width:100%;height:2rem;display:block;"></span> |
| SET.SPECTRAL           |  `#424E54`  |      `-`      | <span style="background-color:#424E54;width:100%;height:2rem;display:block;"></span> |
| SET.VOUCHER            |  `#424E54`  |      `-`      | <span style="background-color:#424E54;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.DEFAULT  | `#9BB6BDFF` |      `-`      | <span style="background-color:#9BB6BD;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.ENHANCED | `#8389DDFF` |      `-`      | <span style="background-color:#8389DD;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.JOKER    |  `#708B91`  |      `-`      | <span style="background-color:#708B91;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.TAROT    |  `#A782D1`  |      `-`      | <span style="background-color:#A782D1;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.PLANET   |  `#13AFCE`  |      `-`      | <span style="background-color:#13AFCE;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.SPECTRAL |  `#4584FA`  |      `-`      | <span style="background-color:#4584FA;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.VOUCHER  |  `#FD682B`  |      `-`      | <span style="background-color:#FD682B;width:100%;height:2rem;display:block;"></span> |
| SECONDARY_SET.EDITION  |  `#4CA893`  |      `-`      | <span style="background-color:#4CA893;width:100%;height:2rem;display:block;"></span> |
| RARITY.1               |  `#009DFF`  |      `-`      | <span style="background-color:#009DFF;width:100%;height:2rem;display:block;"></span> |
| RARITY.2               |  `#4BC292`  |      `-`      | <span style="background-color:#4BC292;width:100%;height:2rem;display:block;"></span> |
| RARITY.3               |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| RARITY.4               |  `#B26CBB`  |      `-`      | <span style="background-color:#B26CBB;width:100%;height:2rem;display:block;"></span> |
| BLIND.SMALL            |  `#50846E`  |      `-`      | <span style="background-color:#50846E;width:100%;height:2rem;display:block;"></span> |
| BLIND.BIG              |  `#50846E`  |      `-`      | <span style="background-color:#50846E;width:100%;height:2rem;display:block;"></span> |
| BLIND.BOSS             |  `#B44430`  |      `-`      | <span style="background-color:#B44430;width:100%;height:2rem;display:block;"></span> |
| BLIND.WON              |  `#4F6367`  |      `-`      | <span style="background-color:#4F6367;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.0          |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.1          |  `#EFEFEF`  |      `-`      | <span style="background-color:#EFEFEF;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.2          |  `#95ACFF`  |      `-`      | <span style="background-color:#95ACFF;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.3          |  `#65EFAF`  |      `-`      | <span style="background-color:#65EFAF;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.4          |  `#FAE37E`  |      `-`      | <span style="background-color:#FAE37E;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.5          |  `#FFC052`  |      `-`      | <span style="background-color:#FFC052;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.6          |  `#F87D75`  |      `-`      | <span style="background-color:#F87D75;width:100%;height:2rem;display:block;"></span> |
| HAND_LEVELS.7          |  `#CAA0EF`  |      `-`      | <span style="background-color:#CAA0EF;width:100%;height:2rem;display:block;"></span> |
| BACKGROUND.L           | `#FFFF00FF` |      `-`      | <span style="background-color:#FFFF00;width:100%;height:2rem;display:block;"></span> |
| BACKGROUND.D           | `#00FFFFFF` |      `-`      | <span style="background-color:#00FFFF;width:100%;height:2rem;display:block;"></span> |
| BACKGROUND.C           |  `#374244`  |      `-`      | <span style="background-color:#374244;width:100%;height:2rem;display:block;"></span> |
| UI_CHIPS               |  `#009DFF`  |      `-`      | <span style="background-color:#009DFF;width:100%;height:2rem;display:block;"></span> |
| UI_MULT                |  `#FE5F55`  |      `-`      | <span style="background-color:#FE5F55;width:100%;height:2rem;display:block;"></span> |
