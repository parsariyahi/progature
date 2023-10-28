from pathlib import Path

from progature.engine.core.managers import GameManager
from progature.engine.core.game.loader import GameLoader


def test_game_manager_init():
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path.absolute())
    manager = GameManager(game)

    assert manager.game_name() == game.name
    assert manager.game_skill()  == game.skill
    assert manager.current_chapter() == game.chapters[0]
    assert manager.next_cahpter() == game.chapters[1]
    assert manager.nth_chapter(2) == game.chapters[2]

    levels = manager.get_chapter_levels(1)
    quests = manager.get_level_quests(1, 1)
    print(quests)

    
    