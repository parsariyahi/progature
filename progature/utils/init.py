"""
Initiate point of the app is here.
"""
from pathlib import Path
import json

from progature.utils.component import(
    create_game, create_skill,
    create_bulk_chapters,
    create_bulk_levels,
    create_bulk_quest,
)
from progature.settings.config import (
    GAME_DIR_PATH
)
from progature.settings.games import (
    PYTHON_BASIC_GAME_JSON,
    PYTHON_ADVANCED_GAME_JSON,
    DATA_STRUCTURE_INTRO_GAME_JSON
)

def create_basic_python_game():
    game_json = PYTHON_BASIC_GAME_JSON
    skill = create_skill(game_json["skill"])
    game = create_game(game_json["file_name"],
                       game_json["name"],
                       skill,)
    game.chapters = create_bulk_chapters(chapters=game_json["chapters"])
    for chapter in game.chapters:
        chapter.levels = create_bulk_levels(game_json["chapters"][chapter.index]["levels"])
        for level in chapter.levels:
            level.quests = create_bulk_quest(game_json["chapters"][chapter.index]["levels"][level.index]["quests"])

    return game


def create_advanced_python_game():
    game_json = PYTHON_ADVANCED_GAME_JSON
    skill = create_skill(game_json["skill"])
    game = create_game(game_json["file_name"],
                       game_json["name"],
                       skill,)
    game.chapters = create_bulk_chapters(chapters=game_json["chapters"])
    for chapter in game.chapters:
        chapter.levels = create_bulk_levels(game_json["chapters"][chapter.index]["levels"])
        for level in chapter.levels:
            level.quests = create_bulk_quest(game_json["chapters"][chapter.index]["levels"][level.index]["quests"])

    return game


def create_data_structure_intro_game():
    game_json = DATA_STRUCTURE_INTRO_GAME_JSON
    skill = create_skill(game_json["skill"])
    game = create_game(game_json["file_name"],
                       game_json["name"],
                       skill,)
    game.chapters = create_bulk_chapters(chapters=game_json["chapters"])
    for chapter in game.chapters:
        chapter.levels = create_bulk_levels(game_json["chapters"][chapter.index]["levels"])
        for level in chapter.levels:
            level.quests = create_bulk_quest(game_json["chapters"][chapter.index]["levels"][level.index]["quests"])

    return game


def create_all_games():
    games = [
        create_basic_python_game(),
        create_advanced_python_game(),
        create_data_structure_intro_game(),
    ]

    for game in games:
        path = Path(GAME_DIR_PATH) / game.file_name
        with open(path, "w") as file:
            json.dump(game.as_dict(), file, indent=4)