import sys
import os
from pathlib import Path

from progature.engine.core.games.loader import GameLoader

def test_game_loader():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path.absolute())

    print(game, game.is_complete)