import sys
import os
from pathlib import Path

from progature.engine.core.game.handler import GameHandler

def test_game_loader():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    handler = GameHandler(py_game_path)
    handler.game_complete()