from progature.engine.components import Game
from tests.utils.component import (
    SkillUtil,
    ChapterUtil
)

def test_create_game():
    skill = SkillUtil.create_skill()

    game = Game("path to your game", "game1", skill=skill)

    assert game.name == "game1"
    assert game.skill == skill

def test_create_game_with_none_skill():
    game = Game("path to your game", "game1")

    assert game.name == "game1"
    assert game.skill is None

def test_create_game_with_chapters():
    game = Game("path to your game", "game1")
    chapters = ChapterUtil.create_chapter_bulk()
    game.chapters = chapters

    assert game.name == "game1"
    assert game.chapters == chapters