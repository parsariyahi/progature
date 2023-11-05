from progature.engine.components.level import Level
from tests.utils.component import QuestUtil


def test_create_level():
    quests = QuestUtil.create_quest_bulk()

    level = Level(0, "level1", quests=quests)

    assert level.name == "level1"
    assert level.quests == quests


def test_create_level_with_none_quests():
    level = Level(0, "level1")

    assert level.name == "level1"
    assert level.quests is None