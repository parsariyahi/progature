import sys
import os
from pathlib import Path

from progature.engine.core.games.loader import GameLoader

def test_game_loader():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path.absolute())

    # assert game["skill"] == "basic python"
    # assert len(game["chapters"]) == 3
    print(game, game.is_complete)
    # print(game.skill.chapters)

    for chapter in game.skill.chapters:
        print("chapter: ", chapter.name, chapter.is_complete)
        for level in chapter.levels:
            print("levels :", level.name, level.is_complete)
            for quest in level.quests:
                print("quest: ", quest.name, quest.is_complete)

        print("---------------")