from pathlib import Path

from progature.engine.core.game.loader import GameLoader
from progature.engine.components import Game
from progature.engine.structures import Pot
from progature.settings.config import GAME_DIR_PATH


def load_all_games() -> Pot[Game]:
    path = Path(GAME_DIR_PATH).glob("*.json")
    game_files = [file for file in path if file.is_file()]
    game_lsit = []

    for game_file in game_files:
        game_lsit.append(
            GameLoader.load(game_file.absolute())
        )

    return Pot(game_lsit)