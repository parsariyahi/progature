import os
import sys
import json
from pathlib import Path
import pytest
from typing import Dict, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from progature.engine.components import Game
from progature.utils.component import(
    create_game, create_skill,
    create_bulk_chapters,
    create_bulk_levels,
    create_bulk_quest,
)
from progature.settings.config import GAME_DIR_PATH
from progature.settings.games import TEST_GAME_JSON


@pytest.fixture
def test_game() -> Game:
    game_json = TEST_GAME_JSON
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

@pytest.fixture
def test_game_json() -> Dict[Any, Any]:
    return TEST_GAME_JSON

def cleanup_test_game(file_name: str):
    path = Path(GAME_DIR_PATH) / file_name

    if os.path.isfile(path):
        os.remove(path)

@pytest.fixture(scope="session", autouse=True)
def game() -> Game:
    game_json = TEST_GAME_JSON
    skill = create_skill(game_json["skill"])
    test_game = create_game(game_json["file_name"],
                       game_json["name"],
                       skill,)
    test_game.chapters = create_bulk_chapters(chapters=game_json["chapters"])
    for chapter in test_game.chapters:
        chapter.levels = create_bulk_levels(game_json["chapters"][chapter.index]["levels"])
        for level in chapter.levels:
            level.quests = create_bulk_quest(game_json["chapters"][chapter.index]["levels"][level.index]["quests"])

    path = Path(GAME_DIR_PATH) / test_game.file_name
    with open(path, "w") as file:
        json.dump(test_game.as_dict(), file, indent=4)

    yield test_game

    cleanup_test_game(test_game.file_name)