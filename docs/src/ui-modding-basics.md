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

Colors are specified in `globals.lua`, you can access them through the `G.C` table. e.g. `G.C.VOUCHER` or `G.C.SUITS.Diamonds`

| Colour name | Colour (hex) | Colour (tuple) |
| VOUCHER | cb724cff | <span style="background-color:#cb724cff;width:100%;height:2rem;display:block;">0.79607843137255,0.44705882352941,0.29803921568627,1<span> |
| GOLD | eac058ff | <span style="background-color:#eac058ff;width:100%;height:2rem;display:block;">0.91764705882353,0.75294117647059,0.34509803921569,1<span> |
| SUITS.Spades | 403995ff | <span style="background-color:#403995ff;width:100%;height:2rem;display:block;">0.25098039215686,0.22352941176471,0.5843137254902,1<span> |
| SUITS.Hearts | f03464ff | <span style="background-color:#f03464ff;width:100%;height:2rem;display:block;">0.94117647058824,0.20392156862745,0.3921568627451,1<span> |
| SUITS.Diamonds | f06b3fff | <span style="background-color:#f06b3fff;width:100%;height:2rem;display:block;">0.94117647058824,0.41960784313725,0.24705882352941,1<span> |
| SUITS.Clubs | 235955ff | <span style="background-color:#235955ff;width:100%;height:2rem;display:block;">0.13725490196078,0.34901960784314,0.33333333333333,1<span> |
| BLUE | 09dffff | <span style="background-color:#09dffff;width:100%;height:2rem;display:block;">0,0.6156862745098,1,1<span> |
| SECONDARY_SET.Edition | 4ca893ff | <span style="background-color:#4ca893ff;width:100%;height:2rem;display:block;">0.29803921568627,0.65882352941176,0.57647058823529,1<span> |
| SECONDARY_SET.Tarot | a782d1ff | <span style="background-color:#a782d1ff;width:100%;height:2rem;display:block;">0.65490196078431,0.50980392156863,0.81960784313725,1<span> |
| SECONDARY_SET.Voucher | fd682bff | <span style="background-color:#fd682bff;width:100%;height:2rem;display:block;">0.9921568627451,0.4078431372549,0.16862745098039,1<span> |
| SECONDARY_SET.Planet | 13afceff | <span style="background-color:#13afceff;width:100%;height:2rem;display:block;">0.074509803921569,0.68627450980392,0.8078431372549,1<span> |
| SECONDARY_SET.Enhanced | 8389ddff | <span style="background-color:#8389ddff;width:100%;height:2rem;display:block;">0.51372549019608,0.53725490196078,0.86666666666667,1<span> |
| SECONDARY_SET.Joker | 708b91ff | <span style="background-color:#708b91ff;width:100%;height:2rem;display:block;">0.43921568627451,0.54509803921569,0.56862745098039,1<span> |
| SECONDARY_SET.Spectral | 4584faff | <span style="background-color:#4584faff;width:100%;height:2rem;display:block;">0.27058823529412,0.51764705882353,0.98039215686275,1<span> |
| SECONDARY_SET.Default | 9bb6bdff | <span style="background-color:#9bb6bdff;width:100%;height:2rem;display:block;">0.6078431372549,0.71372549019608,0.74117647058824,1<span> |
| RENTAL | b18f43ff | <span style="background-color:#b18f43ff;width:100%;height:2rem;display:block;">0.69411764705882,0.56078431372549,0.26274509803922,1<span> |
| CHANCE | 4bc292ff | <span style="background-color:#4bc292ff;width:100%;height:2rem;display:block;">0.29411764705882,0.76078431372549,0.57254901960784,1<span> |
| SET.Tarot | 424e54ff | <span style="background-color:#424e54ff;width:100%;height:2rem;display:block;">0.25882352941176,0.30588235294118,0.32941176470588,1<span> |
| SET.Voucher | 424e54ff | <span style="background-color:#424e54ff;width:100%;height:2rem;display:block;">0.25882352941176,0.30588235294118,0.32941176470588,1<span> |
| SET.Planet | 424e54ff | <span style="background-color:#424e54ff;width:100%;height:2rem;display:block;">0.25882352941176,0.30588235294118,0.32941176470588,1<span> |
| SET.Enhanced | cdd9dcff | <span style="background-color:#cdd9dcff;width:100%;height:2rem;display:block;">0.80392156862745,0.85098039215686,0.86274509803922,1<span> |
| SET.Joker | 424e54ff | <span style="background-color:#424e54ff;width:100%;height:2rem;display:block;">0.25882352941176,0.30588235294118,0.32941176470588,1<span> |
| SET.Spectral | 424e54ff | <span style="background-color:#424e54ff;width:100%;height:2rem;display:block;">0.25882352941176,0.30588235294118,0.32941176470588,1<span> |
| SET.Default | cdd9dcff | <span style="background-color:#cdd9dcff;width:100%;height:2rem;display:block;">0.80392156862745,0.85098039215686,0.86274509803922,1<span> |
| MULT | fe5f55ff | <span style="background-color:#fe5f55ff;width:100%;height:2rem;display:block;">0.99607843137255,0.37254901960784,0.33333333333333,1<span> |
| PALE_GREEN | 56a887ff | <span style="background-color:#56a887ff;width:100%;height:2rem;display:block;">0.33725490196078,0.65882352941176,0.52941176470588,1<span> |
| GREY | 5f7377ff | <span style="background-color:#5f7377ff;width:100%;height:2rem;display:block;">0.37254901960784,0.45098039215686,0.46666666666667,1<span> |
| L_BLACK | 4f6367ff | <span style="background-color:#4f6367ff;width:100%;height:2rem;display:block;">0.30980392156863,0.38823529411765,0.40392156862745,1<span> |
| SO_1.Spades | 403995ff | <span style="background-color:#403995ff;width:100%;height:2rem;display:block;">0.25098039215686,0.22352941176471,0.5843137254902,1<span> |
| SO_1.Hearts | f03464ff | <span style="background-color:#f03464ff;width:100%;height:2rem;display:block;">0.94117647058824,0.20392156862745,0.3921568627451,1<span> |
| SO_1.Diamonds | f06b3fff | <span style="background-color:#f06b3fff;width:100%;height:2rem;display:block;">0.94117647058824,0.41960784313725,0.24705882352941,1<span> |
| SO_1.Clubs | 235955ff | <span style="background-color:#235955ff;width:100%;height:2rem;display:block;">0.13725490196078,0.34901960784314,0.33333333333333,1<span> |
| CLEAR | 0000 | <span style="background-color:#0000;width:100%;height:2rem;display:block;">0,0,0,0<span> |
| EDITION | e6d8ecff | <span style="background-color:#e6d8ecff;width:100%;height:2rem;display:block;">0.90291040727138,0.84691730420935,0.92533973171087,1<span> |
| ORANGE | fda20ff | <span style="background-color:#fda20ff;width:100%;height:2rem;display:block;">0.9921568627451,0.63529411764706,0,1<span> |
| MONEY | f3b958ff | <span style="background-color:#f3b958ff;width:100%;height:2rem;display:block;">0.95294117647059,0.72549019607843,0.34509803921569,1<span> |
| SO_2.Spades | 4f31b9ff | <span style="background-color:#4f31b9ff;width:100%;height:2rem;display:block;">0.30980392156863,0.1921568627451,0.72549019607843,1<span> |
| SO_2.Hearts | f83b2fff | <span style="background-color:#f83b2fff;width:100%;height:2rem;display:block;">0.97254901960784,0.23137254901961,0.1843137254902,1<span> |
| SO_2.Diamonds | e2900ff | <span style="background-color:#e2900ff;width:100%;height:2rem;display:block;">0.88627450980392,0.56470588235294,0,1<span> |
| SO_2.Clubs | 08ee6ff | <span style="background-color:#08ee6ff;width:100%;height:2rem;display:block;">0,0.55686274509804,0.90196078431373,1<span> |
| IMPORTANT | ff9a0ff | <span style="background-color:#ff9a0ff;width:100%;height:2rem;display:block;">1,0.60392156862745,0,1<span> |
| ETERNAL | c75985ff | <span style="background-color:#c75985ff;width:100%;height:2rem;display:block;">0.78039215686275,0.34901960784314,0.52156862745098,1<span> |
| BOOSTER | 646eb7ff | <span style="background-color:#646eb7ff;width:100%;height:2rem;display:block;">0.3921568627451,0.43137254901961,0.71764705882353,1<span> |
| YELLOW | ffff0ff | <span style="background-color:#ffff0ff;width:100%;height:2rem;display:block;">1,1,0,1<span> |
| XMULT | fe5f55ff | <span style="background-color:#fe5f55ff;width:100%;height:2rem;display:block;">0.99607843137255,0.37254901960784,0.33333333333333,1<span> |
| PURPLE | 8867a5ff | <span style="background-color:#8867a5ff;width:100%;height:2rem;display:block;">0.53333333333333,0.40392156862745,0.64705882352941,1<span> |
| RARITY.1 | 09dffff | <span style="background-color:#09dffff;width:100%;height:2rem;display:block;">0,0.6156862745098,1,1<span> |
| RARITY.2 | 4bc292ff | <span style="background-color:#4bc292ff;width:100%;height:2rem;display:block;">0.29411764705882,0.76078431372549,0.57254901960784,1<span> |
| RARITY.3 | fe5f55ff | <span style="background-color:#fe5f55ff;width:100%;height:2rem;display:block;">0.99607843137255,0.37254901960784,0.33333333333333,1<span> |
| RARITY.4 | b26cbbff | <span style="background-color:#b26cbbff;width:100%;height:2rem;display:block;">0.69803921568627,0.42352941176471,0.73333333333333,1<span> |
| RED | fe5f55ff | <span style="background-color:#fe5f55ff;width:100%;height:2rem;display:block;">0.99607843137255,0.37254901960784,0.33333333333333,1<span> |
| WHITE | ffffffff | <span style="background-color:#ffffffff;width:100%;height:2rem;display:block;">1,1,1,1<span> |
| UI_MULT | fe5f55ff | <span style="background-color:#fe5f55ff;width:100%;height:2rem;display:block;">0.99607843137255,0.37254901960784,0.33333333333333,1<span> |
| GREEN | 4bc292ff | <span style="background-color:#4bc292ff;width:100%;height:2rem;display:block;">0.29411764705882,0.76078431372549,0.57254901960784,1<span> |
| UI_CHIPS | 09dffff | <span style="background-color:#09dffff;width:100%;height:2rem;display:block;">0,0.6156862745098,1,1<span> |
| PERISHABLE | 4f5da1ff | <span style="background-color:#4f5da1ff;width:100%;height:2rem;display:block;">0.30980392156863,0.36470588235294,0.63137254901961,1<span> |
| HAND_LEVELS.0 | fe5f55ff | <span style="background-color:#fe5f55ff;width:100%;height:2rem;display:block;">0.99607843137255,0.37254901960784,0.33333333333333,1<span> |
| HAND_LEVELS.1 | efefefff | <span style="background-color:#efefefff;width:100%;height:2rem;display:block;">0.93725490196078,0.93725490196078,0.93725490196078,1<span> |
| HAND_LEVELS.2 | 95acffff | <span style="background-color:#95acffff;width:100%;height:2rem;display:block;">0.5843137254902,0.67450980392157,1,1<span> |
| HAND_LEVELS.3 | 65efafff | <span style="background-color:#65efafff;width:100%;height:2rem;display:block;">0.39607843137255,0.93725490196078,0.68627450980392,1<span> |
| HAND_LEVELS.4 | fae37eff | <span style="background-color:#fae37eff;width:100%;height:2rem;display:block;">0.98039215686275,0.89019607843137,0.49411764705882,1<span> |
| HAND_LEVELS.5 | ffc052ff | <span style="background-color:#ffc052ff;width:100%;height:2rem;display:block;">1,0.75294117647059,0.32156862745098,1<span> |
| HAND_LEVELS.6 | f87d75ff | <span style="background-color:#f87d75ff;width:100%;height:2rem;display:block;">0.97254901960784,0.49019607843137,0.45882352941176,1<span> |
| HAND_LEVELS.7 | caa0efff | <span style="background-color:#caa0efff;width:100%;height:2rem;display:block;">0.7921568627451,0.62745098039216,0.93725490196078,1<span> |
| BLIND.Small | 50846eff | <span style="background-color:#50846eff;width:100%;height:2rem;display:block;">0.31372549019608,0.51764705882353,0.43137254901961,1<span> |
| BLIND.won | 4f6367ff | <span style="background-color:#4f6367ff;width:100%;height:2rem;display:block;">0.30980392156863,0.38823529411765,0.40392156862745,1<span> |
| BLIND.Boss | b44430ff | <span style="background-color:#b44430ff;width:100%;height:2rem;display:block;">0.70588235294118,0.26666666666667,0.18823529411765,1<span> |
| BLIND.Big | 50846eff | <span style="background-color:#50846eff;width:100%;height:2rem;display:block;">0.31372549019608,0.51764705882353,0.43137254901961,1<span> |
| JOKER_GREY | bfc7d5ff | <span style="background-color:#bfc7d5ff;width:100%;height:2rem;display:block;">0.74901960784314,0.78039215686275,0.83529411764706,1<span> |
| DARK_EDITION | 9a9acbff | <span style="background-color:#9a9acbff;width:100%;height:2rem;display:block;">0.6025223751273,0.6025223751273,0.7974776248727,1<span> |
| UI.BACKGROUND_WHITE | ffffffff | <span style="background-color:#ffffffff;width:100%;height:2rem;display:block;">1,1,1,1<span> |
| UI.TEXT_DARK | 4f6367ff | <span style="background-color:#4f6367ff;width:100%;height:2rem;display:block;">0.30980392156863,0.38823529411765,0.40392156862745,1<span> |
| UI.TEXT_LIGHT | ffffffff | <span style="background-color:#ffffffff;width:100%;height:2rem;display:block;">1,1,1,1<span> |
| UI.TEXT_INACTIVE | 88888899 | <span style="background-color:#88888899;width:100%;height:2rem;display:block;">0.53333333333333,0.53333333333333,0.53333333333333,0.6<span> |
| UI.OUTLINE_LIGHT | d8d8d8ff | <span style="background-color:#d8d8d8ff;width:100%;height:2rem;display:block;">0.84705882352941,0.84705882352941,0.84705882352941,1<span> |
| UI.HOVER | 00055 | <span style="background-color:#00055;width:100%;height:2rem;display:block;">0,0,0,0.33333333333333<span> |
| UI.OUTLINE_DARK | 7a9e9fff | <span style="background-color:#7a9e9fff;width:100%;height:2rem;display:block;">0.47843137254902,0.61960784313725,0.62352941176471,1<span> |
| UI.TRANSPARENT_LIGHT | eeeeee22 | <span style="background-color:#eeeeee22;width:100%;height:2rem;display:block;">0.93333333333333,0.93333333333333,0.93333333333333,0.13333333333333<span> |
| UI.TRANSPARENT_DARK | 22222222 | <span style="background-color:#22222222;width:100%;height:2rem;display:block;">0.13333333333333,0.13333333333333,0.13333333333333,0.13333333333333<span> |
| UI.OUTLINE_LIGHT_TRANS | d8d8d866 | <span style="background-color:#d8d8d866;width:100%;height:2rem;display:block;">0.84705882352941,0.84705882352941,0.84705882352941,0.4<span> |
| UI.BACKGROUND_DARK | 7a9e9fff | <span style="background-color:#7a9e9fff;width:100%;height:2rem;display:block;">0.47843137254902,0.61960784313725,0.62352941176471,1<span> |
| UI.BACKGROUND_INACTIVE | 666666ff | <span style="background-color:#666666ff;width:100%;height:2rem;display:block;">0.4,0.4,0.4,1<span> |
| UI.BACKGROUND_LIGHT | b8d8d8ff | <span style="background-color:#b8d8d8ff;width:100%;height:2rem;display:block;">0.72156862745098,0.84705882352941,0.84705882352941,1<span> |
| FILTER | ff9a0ff | <span style="background-color:#ff9a0ff;width:100%;height:2rem;display:block;">1,0.60392156862745,0,1<span> |
| BLACK | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| BACKGROUND.D | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| BACKGROUND.L | ffff0ff | <span style="background-color:#ffff0ff;width:100%;height:2rem;display:block;">1,1,0,1<span> |
| BACKGROUND.C | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| DYN_UI.BOSS_DARK | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| DYN_UI.DARK | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| DYN_UI.MAIN | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| DYN_UI.BOSS_PALE | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| DYN_UI.BOSS_MAIN | 374244ff | <span style="background-color:#374244ff;width:100%;height:2rem;display:block;">0.2156862745098,0.25882352941176,0.26666666666667,1<span> |
| CHIPS | 09dffff | <span style="background-color:#09dffff;width:100%;height:2rem;display:block;">0,0.6156862745098,1,1<span> |