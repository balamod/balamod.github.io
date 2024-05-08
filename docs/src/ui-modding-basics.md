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

<div class="table-wrapper">
<table>
<thead>
<tr>
<th style="text-align: left">Color Name</th>
<th style="text-align: center">Color (hex)</th>
<th style="text-align: center">Color (tuple)</th>
<th style="text-align: center">Color</th>
</tr>
</thead>
<tbody>
{% for color in colors %}
<tr>
<td style="text-align: left"> {{ color.name }} </td>
<td style="text-align: center"> <code class="hljs"> #{{ color.hex }} </code></td>
<td style="text-align: center"> <code class="hljs"> ({{color.tuple[0]}},{{color.tuple[1]}},{{color.tuple[2]}},{{color.tuple[3]}}) </code></td>
<td style="text-align: center"><span style="background-color:#{{color.hex | upper}};width:100%;height:2rem;display:block;"></span></td>
</tr>
{% endfor %}
</tbody>
</table>
</div>
