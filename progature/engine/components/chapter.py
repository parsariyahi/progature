from __future__ import annotations
from typing import List, Optional, Union

from progature.engine.structures.pots import LevelPot
from progature.engine.components.level import Level

class Chapter:

    def __init__(self, index: int, name: str, levels: Optional[LevelPot[Level] | None] = None, is_complete=False):
        self.index = index
        self.name = name
        self.levels = levels
        self.is_complete = is_complete

    def __str__(self) -> str:
        string = f"{self.index}.{self.name}:{self.is_complete}"
        return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Chapter):
            return self.name == other.name

        raise TypeError("Type Error Chapter")

    @property 
    def levels(self) -> Union[LevelPot[Level], None]:
        return self._levels

    @levels.setter
    def levels(self, levels: Optional[LevelPot[Level] | None]):
        self._levels = levels