from tests.utils.component import ChapterUtil

from progature.engine.structures import Pot
from progature.engine.components import Chapter
from progature.engine.core.managers import ChapterManager


def test_chapter_manager_init():
    chapters = ChapterUtil.create_chapter_bulk()
    pot = Pot(chapters)
    manager = ChapterManager(pot)

    assert manager.current_chapter() == pot[0]
    assert manager.next_cahpter() == pot[1]
    assert manager.next_cahpter() == pot[2]
    assert manager.nth_chapter(4) == pot[4]