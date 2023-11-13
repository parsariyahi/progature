from progature.engine.components.chapter import Chapter
from tests.utils.component import LevelUtil

def test_create_chapter():
    levels = LevelUtil.create_level_bulk()
    chapter = Chapter(0, "chapter1", levels=levels)

    # print(chapter.as_dict())

    assert chapter.name == "chapter1"
    assert chapter.levels == levels

def test_create_chapter_with_none_levels():
    chapter = Chapter(0, "chapter1")

    assert chapter.name == "chapter1"
    assert chapter.levels is None