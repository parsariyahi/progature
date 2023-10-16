from tests.utils.component import (
    ChapterUtil,
    LevelUtil,
    QuestUtil
)

from progature.engine.structures.pots import (
    Pot,
    ChapterPot,
    LevelPot,
    QuestPot,
)


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

def test_chapter_pot():
    chapters = ChapterUtil.create_chapter_bulk()

    pot = ChapterPot(chapters)

def test_level_pot():
    levels = LevelUtil.create_level_bulk()

    pot = LevelPot(levels)

def test_quest_pot():
    quests = QuestUtil.create_quest_bulk()

    pot = QuestPot(quests)