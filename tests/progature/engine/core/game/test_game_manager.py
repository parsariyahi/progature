from pathlib import Path

from progature.engine.core.game.manager import GameManager
from progature.engine.core.game.loader import GameLoader
from tests.utils.games import (
    create_test_game,
    cleanup_test_game,
)


def test_game_manager_init():
    create_test_game()
    game_name = "test_game.json"
    test_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(test_game_path.absolute())
    manager = GameManager(test_game_path)

    assert manager.game_name() == game.name
    assert manager.game_skill() == game.skill
    cleanup_test_game()

def test_game_manager_game_complete():
    create_test_game()
    game_name = "test_game.json"
    test_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(test_game_path.absolute())
    manager = GameManager(test_game_path)

    manager.game_complete()

    assert manager.game["is_compelte"] == True
    cleanup_test_game()

def test_game_manager_game_complete():
    create_test_game()
    game_name = "test_game.json"
    test_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(test_game_path.absolute())
    manager = GameManager(test_game_path)
    manager.game_complete()

    assert manager.game.is_complete == True
    cleanup_test_game()

def test_game_manager_chaper_complete():
    create_test_game()
    game_name = "test_game.json"
    test_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(test_game_path.absolute())
    manager = GameManager(test_game_path)

    chapter_index = 0
    manager.chapter_complete(chapter_index)

    assert manager.game.chapters[chapter_index].is_complete == True
    cleanup_test_game()

def test_game_manager_level_complete():
    create_test_game()
    game_name = "test_game.json"
    test_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(test_game_path.absolute())
    manager = GameManager(test_game_path)

    chapter_index = 0
    level_index = 0
    manager.level_complete(chapter_index, level_index)

    assert manager.game.chapters[chapter_index].levels[level_index].is_complete == True
    cleanup_test_game()

def test_game_manager_quest_complete():
    create_test_game()
    game_name = "test_game.json"
    test_game_path = Path("progature/db/games") / game_name
    game = GameLoader.load(test_game_path.absolute())
    manager = GameManager(test_game_path)

    chapter_index = 0
    level_index = 0
    quest_index = 0
    manager.quest_complete(chapter_index, level_index, quest_index)

    assert manager.game.chapters[chapter_index].levels[level_index].quests[quest_index].is_complete == True
    cleanup_test_game()
