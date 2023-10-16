from __future__ import annotations
from typing import Optional, Union, List

from progature.engine.components.skill import Skill
from progature.engine.component.chapter import Chapter

class Game:

    def __init__(self, name, skill: Optional[Skill | None] = None, chapters: Optional[List[Chapter] | None] = None, is_complete=False) -> None:
        self.name = name
        self.skill = skill
        self.chapters = chapters
        self.is_complete = is_complete
    
    @property
    def skill(self) -> Union[Skill, None]:
        return self._skill

    @skill.setter
    def skill(self, skill: Optional[Skill | None]):
        self._skill = skill

    @property
    def chapters(self) -> Union[Skill, None]:
        return self._chapters

    @chapters.setter
    def chapters(self, chapters: Optional[List[Chapter] | None]):
        self._chapters = chapters