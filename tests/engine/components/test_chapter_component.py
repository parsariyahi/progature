from progature.engine.components.chapter import Chapter
from tests.utils.component import LevelUtil

def test_create_chapter():
    levels = LevelUtil.create_level_bulk()

    chapter = Chapter("chapter1", levels=levels)

    assert chapter.name == "chapter1"
    assert chapter.levels == levels