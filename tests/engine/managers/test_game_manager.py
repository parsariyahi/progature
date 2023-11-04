from pathlib import Path

from progature.engine.core.managers import GameManager
from progature.engine.core.game.loader import GameLoader


def test_game_manager_init():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path.absolute())
    manager = GameManager(py_game_path)

    assert manager.game_name() == game.name
    assert manager.game_skill() == game.skill