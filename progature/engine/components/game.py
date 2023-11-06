from __future__ import annotations
from typing import Optional, Union, List

from progature.engine.structures.pots import ChapterPot
from progature.engine.components.skill import Skill
from progature.engine.components.chapter import Chapter

class Game:

    def __init__(self, file_path, name, skill: Optional[Skill | None] = None, chapters: Optional[ChapterPot[Chapter] | None] = None, is_complete=False) -> None:
        self.file_path = file_path
        self.name = name
        self.skill = skill
        self.chapters = chapters
        self.is_complete = is_complete

    def __str__(self) -> str:
        string = f"{self.name}:{self.is_complete}"
        return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Game):
            return self.name == other.name

        raise TypeError("Type Error Game")
    
    @property
    def skill(self) -> Union[Skill, None]:
        return self._skill

    @skill.setter
    def skill(self, skill: Optional[Skill | None]):
        self._skill = skill

    @property
    def chapters(self) -> Union[ChapterPot[Chapter], None]:
        return self._chapters

    @chapters.setter
    def chapters(self, chapters: Optional[ChapterPot[Chapter] | None]):
        self._chapters = chapters