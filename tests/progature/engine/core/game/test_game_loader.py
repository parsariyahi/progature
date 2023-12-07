import sys
import os
from pathlib import Path

from progature.engine.core.game.loader import GameLoader
from tests.utils.games import (
    create_test_game,
    cleanup_test_game,
)

def test_game_loader():
    create_test_game()
    game_name = "test_game.json"
    py_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(py_game_path.absolute())

    print(game, game.is_complete)
    cleanup_test_game()