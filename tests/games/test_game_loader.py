import sys
import os
from pathlib import Path

from progature.games import GameLoader

def test_game_loader():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path.absolute())

    assert game["skill"] == "basic python"
    assert len(game["chapters"]) == 3