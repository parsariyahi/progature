from pathlib import Path
import json

from progature.engine.core.game.handler import GameHandler
from progature.engine.core.game.loader import GameLoader

def test_game_handler():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    handler = GameHandler(game)

def test_game_handler_write_on_game():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler._write_on_game("skill", "basic python3")

def test_game_handler_write_on_chapter():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler._write_on_chapter("name", "vars", 0)
        handler._write_on_chapter("name", "loooops", 1)

def test_game_handler_write_on_level():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler._write_on_level("name", "ints", 0, 0)
        handler._write_on_level("name", "for loooops", 1, 1)

def test_game_handler_write_on_quest():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler._write_on_quest("name", "create int obj", 0, 0, 0)
        handler._write_on_quest("is_complete", True, 1, 1, 1)

def test_game_handler_game_complete():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler.game_complete()

def test_game_handler_chapter_complete():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler.chapter_complete(1)

def test_game_handler_level_complete():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler.level_complete(1, 0)

def test_game_handler_quest_complete():
    game_name = "test_game.json"
    py_game_path = Path("progature/games") / game_name

    with open(py_game_path.absolute(), "r") as file:
        game_json = json.load(file)

    game = GameLoader.load(py_game_path)
    with GameHandler(game) as handler:
        handler.quest_complete(1, 0, 0)