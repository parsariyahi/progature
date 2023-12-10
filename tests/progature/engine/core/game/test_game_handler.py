from pathlib import Path

from progature.engine.core.game.handler import GameHandler


def test_game_handler(game):
    py_game_path = Path("progature/db/games") / game.file_name
    handler = GameHandler(py_game_path.absolute())

def test_game_handler_write_on_game(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_game("skill", "basic python3")

def test_game_handler_write_on_chapter(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_chapter("name", "vars", 0)
        handler._write_on_chapter("name", "loooops", 1)

def test_game_handler_write_on_level(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_level("name", "ints", 0, 0)
        handler._write_on_level("name", "for loooops", 1, 1)

def test_game_handler_write_on_quest(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler._write_on_quest("name", "create int obj", 0, 0, 0)
        handler._write_on_quest("is_complete", True, 1, 1, 1)

def test_game_handler_game_complete(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.game_complete()

def test_game_handler_chapter_complete(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.chapter_complete(1)

def test_game_handler_level_complete(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.level_complete(1, 0)

def test_game_handler_quest_complete(game):
    py_game_path = Path("progature/db/games") / game.file_name

    with GameHandler(py_game_path.absolute()) as handler:
        handler.quest_complete(1, 0, 0)