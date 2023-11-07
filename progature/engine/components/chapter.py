from __future__ import annotations
from typing import List, Optional, Union, Dict

from progature.engine.structures import Pot
from progature.engine.components.level import Level

class Chapter:

    def __init__(self, index: int, name: str, levels: Optional[Pot[Level] | None] = None, is_complete=False):
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

    def as_dict(self) -> Dict:
        return {
            "index": self.index,
            "name": self.name,
            "is_complete": self.is_complete,
            "levels": [level.as_dict() for level in self.levels],
        }

    @property 
    def levels(self) -> Union[Pot[Level], None]:
        return self._levels

    @levels.setter
    def levels(self, levels: Optional[Pot[Level] | None]):
        self._levels = levels