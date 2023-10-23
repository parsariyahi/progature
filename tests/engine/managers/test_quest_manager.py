from tests.utils.component import QuestUtil

from progature.engine.structures.pots import QuestPot
from progature.engine.components import Quest
from progature.engine.core.managers import QuestManager


def test_quest_manager_init():
    quests = QuestUtil.create_quest_bulk()
    pot = QuestPot(quests)
    manager = QuestManager(pot)

    assert manager.current_quest() == pot[0]
    assert manager.next_quest() == pot[1]
    assert manager.next_quest() == pot[2]
    assert manager.nth_quest(4) == pot[4]