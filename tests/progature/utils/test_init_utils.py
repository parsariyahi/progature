import os
from pathlib import Path

from progature.utils.init import (
    create_basic_python_game,
    create_advanced_python_game,
    create_data_structure_intro_game,
    create_all_games,
)
from progature.settings.games import (
    PYTHON_BASIC_GAME_JSON,
    PYTHON_ADVANCED_GAME_JSON,
    DATA_STRUCTURE_INTRO_GAME_JSON
)


def test_basic_python_game():
    game = create_basic_python_game()

    assert game.as_dict() == PYTHON_BASIC_GAME_JSON


def teat_create_advanced_python_game():
    game = create_advanced_python_game()

    assert game.as_dict() == PYTHON_ADVANCED_GAME_JSON


def teat_create_data_structure_intro_game():
    game = create_data_structure_intro_game()

    assert game.as_dict() == DATA_STRUCTURE_INTRO_GAME_JSON


def test_create_all_games():
    games = [
        create_basic_python_game(),
        create_advanced_python_game(),
        create_data_structure_intro_game(),
    ]

    create_all_games()

    for game in games:
        path = Path("progature/db/games/") / game.file_name
        assert os.path.isfile(path) == True