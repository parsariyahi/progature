from progature.engine.components.skill import Skill
from tests.utils.component import ChapterUtil

def test_create_skill():
    skill = Skill("skill1")

    assert skill.name == "skill1"