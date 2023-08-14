from progature.engine.components import Game
from tests.utils.component import SkillUtil

def test_create_game():
    skill = SkillUtil.create_skill()

    game = Game("game1", skill=skill)

    assert game.name == "game1"
    assert game.skill == skill

def test_create_game_with_none_skill():
    game = Game("game1")

    assert game.name == "game1"
    assert game.skill is None