from progature.engine.components.level import Level
from tests.utils.component import QuestUtil


def test_create_level():
    quests = QuestUtil.create_quest_bulk()

    level = Level("level1", quests=quests)

    assert level.name == "level1"
    assert level.quests == quests