from pathlib import Path

from progature.engine.core.game.loader import GameLoader

def test_game_loader(game):
    py_game_path = Path("progature/db/games") / game.file_name
    game_loaded = GameLoader.load(py_game_path.absolute())

    print(game_loaded, game_loaded.is_complete)