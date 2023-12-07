from pathlib import Path
import json

from progature.engine.core.game.handler import GameHandler
from progature.engine.core.game.loader import GameLoader
from tests.utils.games import (
    create_test_game,
    cleanup_test_game,
)

def test_game_handler():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name
    handler = GameHandler(py_game_path.absolute())
    cleanup_test_game()

def test_game_handler_write_on_game():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_game("skill", "basic python3")
    cleanup_test_game()

def test_game_handler_write_on_chapter():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_chapter("name", "vars", 0)
        handler._write_on_chapter("name", "loooops", 1)
    cleanup_test_game()

def test_game_handler_write_on_level():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_level("name", "ints", 0, 0)
        handler._write_on_level("name", "for loooops", 1, 1)
    cleanup_test_game()

def test_game_handler_write_on_quest():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_quest("name", "create int obj", 0, 0, 0)
        handler._write_on_quest("is_complete", True, 1, 1, 1)
    cleanup_test_game()

def test_game_handler_game_complete():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.game_complete()
    cleanup_test_game()

def test_game_handler_chapter_complete():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.chapter_complete(1)
    cleanup_test_game()

def test_game_handler_level_complete():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.level_complete(1, 0)
    cleanup_test_game()

def test_game_handler_quest_complete():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.quest_complete(1, 0, 0)
    cleanup_test_game()