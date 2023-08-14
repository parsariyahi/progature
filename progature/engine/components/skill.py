from __future__ import annotations
from typing import List, Optional, Union

from progature.engine.components.chapter import Chapter

class Skill:

    def __init__(self, name, chapters: Optional[List[Chapter] | None] = None) -> None:
        self.name = name
        self.chapters = chapters

    @property
    def chapters(self) -> Union[List[Chapter], None]:
        return self._chapters

    @chapters.setter
    def chapters(self, chapters: Optional[List[Chapter] | None]) -> None:
        self._chapters = chapters