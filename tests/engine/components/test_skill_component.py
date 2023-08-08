from progature.engine.components.skill import Skill
from tests.utils.component import ChapterUtil

def test_create_skill():
    chapters = ChapterUtil.create_chapter_bulk()

    skill = Skill("skill1", chapters=chapters)

    assert skill.name == "skill1"
    assert skill.chapters == chapters