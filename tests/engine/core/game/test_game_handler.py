import sys
import os
from pathlib import Path

from progature.engine.core.game.handler import GameHandler
from progature.engine.core.game.loader import GameLoader

def test_game_loader():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path.absolute())
    handler = GameHandler(game)
    handler.game_complete()