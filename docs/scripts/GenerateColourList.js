/**
 * Generates a markdown table of colours from a JSON file.
 * 
 * You can retrieve the relevant json from dev_console's 'colours' command.
 * 
 * @param {string} file The path to the JSON file.
 */

const path = require("node:path");
const file = process.argv[2] ?? `.${path.sep}colours.json`;
const input = require(file);

let output = "| Colour name | Colour (hex) | Colour (tuple) |";
for (let [key, value] of Object.entries(input)) {
	output += `\n| ${key} | ${value[0]} | <span style="background-color:#${value[0]};width:100%;height:2rem;display:block;">${value[1]}<span> |`;
}

console.log(output);