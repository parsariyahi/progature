from tests.utils.component import (
    ChapterUtil,
    LevelUtil,
    QuestUtil
)
from progature.engine.structures import Pot


def test_loop_through_pot():
    pot = Pot([1, 2, 3, 4])
    number = 1

    for item in pot:
        assert item == number
        number += 1

def test_get_item_from_pot():
    pot = Pot([1, 2, 3, 4])
    number = 2
    index = 1

    assert pot[index] == number

def test_pot_with_chapter():
    chapters = ChapterUtil.create_chapter_bulk()

    pot = Pot(chapters)

def test_pot_with_level():
    levels = LevelUtil.create_level_bulk()

    pot = Pot(levels)

def test_pot_with_quest():
    quests = QuestUtil.create_quest_bulk()

    pot = Pot(quests)