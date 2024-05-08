import base64
import io
import json
import os
from typing import TypedDict
import zipfile

from luaparser import ast, astnodes
import requests


class BalamodVersion(TypedDict):
    latest_tag: str
    latest_url: str
    published_at: str
    release_url_linux: str
    release_name_linux: str
    release_url_windows: str
    release_name_windows: str
    release_url_macos: str
    release_name_macos: str


class Mod(TypedDict):
    id: str
    version: str
    name: str
    description: str
    url: str


class Color(TypedDict):
    name: str
    hex: str
    tuple: tuple[float, float, float, float]


session = requests.session()
session.headers["User-Agent"] = "Balamod Client"
USER = "balamod"
REPO = "balamod"
github_repo_api = f"https://api.github.com/repos/balamod/balamod/releases/latest"
github_gui_repo_api = (
    f"https://api.github.com/repos/balamod/balamod-gui/releases/latest"
)
mods_repo_index_url = (
    f"https://raw.githubusercontent.com/balamod/balamod/master/repos.index"
)
apis_repo_index_url = (
    f"https://raw.githubusercontent.com/balamod/balamod/master/apis.index"
)

config_path = "context.json"


def get_balamod_version(url: str) -> BalamodVersion:
    res = session.get(url).json()
    version = {}

    version["latest_tag"] = res["tag_name"]
    version["latest_url"] = res["html_url"]
    version["published_at"] = res["published_at"]

    linux_assets = next(
        (asset for asset in res["assets"] if "linux" in asset["name"]), None
    )
    version["release_url_linux"] = (
        linux_assets["browser_download_url"] if linux_assets else None
    )
    version["release_name_linux"] = linux_assets["name"] if linux_assets else None

    windows_assets = next(
        (asset for asset in res["assets"] if "windows" in asset["name"]), None
    )
    version["release_url_windows"] = (
        windows_assets["browser_download_url"] if windows_assets else None
    )
    version["release_name_windows"] = windows_assets["name"] if windows_assets else None

    macos_assets = next(
        (
            asset
            for asset in res["assets"]
            if "mac" in asset["name"] or ".pkg" in asset["name"]
        ),
        None,
    )
    version["release_url_macos"] = (
        macos_assets["browser_download_url"] if macos_assets else None
    )
    version["release_name_macos"] = macos_assets["name"] if macos_assets else None
    print("Successfully collected balamod version")
    return version


def parse_mod(mod: str) -> Mod:
    """
    dev_console|0.5.1|Dev Console|An in-game developer console|https://github.com/balamod/mods/tree/main/dev_console|{}
    """
    mod = mod.split("|")
    return {
        "id": mod[0],
        "version": mod[1],
        "name": mod[2],
        "description": mod[3],
        "url": mod[4],
    }


def collect(url: str) -> list[Mod]:
    all_mods = []
    repos = requests.get(url).text
    for repo in repos.split("\n"):
        if not repo:  # Skip if repo is empty
            continue
        mods = requests.get(repo).text
        for mod in mods.split("\n"):
            if not mod:
                continue
            all_mods.append(parse_mod(mod))
    print("Successfully collected community mods")
    return mods


def find_color_node(tree: ast.Node) -> ast.Node:
    return next(
        (
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Assign)
            and isinstance(node.targets[0], ast.Index)
            and node.targets[0].idx.id == "C"
        ),
        None,
    )


def table_to_hex(table: ast.Table) -> str:
    t = [f.value.n for f in table.fields]
    hexparts = [hex(int(p * 255)).replace("0x", "").zfill(2) for p in t]
    return "".join(hexparts)


def lua_table_to_dict(table: ast.Table) -> dict[str, str | dict[str, str]]:
    data = {}
    for field in table.fields:
        key: ast.Name = field.key
        value: ast.Table | ast.Call = field.value
        if isinstance(value, ast.Table):
            if all(
                isinstance(f.key, ast.Number) and isinstance(f.value, ast.Number)
                for f in value.fields
            ):
                data[key.id] = table_to_hex(value)
            else:
                data[key.id] = lua_table_to_dict(value)
        elif isinstance(value, ast.Call):
            arg: ast.String = value.args[0]
            name = key.id if isinstance(key, ast.Name) else key.n
            data[name] = arg.s
        else:
            print("Unknown type", value)
    return data


def flatten_dict(
    data: dict[str, str | dict[str, str]], prefix: str = ""
) -> dict[str, str]:
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result.update(flatten_dict(value, f"{prefix}{key}."))
        else:
            result[f"{prefix}{key}"] = value
    return result


def as_tuple(hex: str) -> tuple[float, float, float, float]:
    if hex.startswith("#"):
        hex = hex[1:]
    if len(hex) == 6:
        hex += "FF"
    return (
        round(int(hex[0:2], 16) / 255, 2),
        round(int(hex[2:4], 16) / 255, 2),
        round(int(hex[4:6], 16) / 255, 2),
        round(int(hex[6:8], 16) / 255, 2),
    )


def parse_balatro_globals(globals_lua: str) -> dict:
    data = base64.b64decode(globals_lua).decode("utf8")
    tree = ast.parse(data)
    color_node: ast.Assign = find_color_node(tree)
    color_table: ast.Table = color_node.values[0]
    raw_colors = lua_table_to_dict(color_table)
    print("Successfully parsed balatro globals")
    return raw_colors


def main():
    raw_colors = parse_balatro_globals(os.getenv("BALATRO_GLOBALS_LUA_BASE64"))
    config_obj = {
        "balamod": get_balamod_version(github_repo_api),
        "balamod_gui": get_balamod_version(github_gui_repo_api),
        "mods": collect(mods_repo_index_url),
        "raw_colors": raw_colors,
        "colors": [
            {"name": key, "hex": value.upper(), "tuple": as_tuple(value)}
            for key, value in flatten_dict(raw_colors).items()
        ],
    }
    print("config_obj", config_obj)

    with open(config_path, "w") as f:
        json.dump(config_obj, f, indent=4)
    return 0


if __name__ == "__main__":
    main()
