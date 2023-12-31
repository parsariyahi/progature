from __future__ import annotations
from typing import List, Optional, Union, Dict

from progature.engine.structures import Pot
from progature.engine.components.level import Level


__all__ = [
    "Chapter",
]


class Chapter:
    def __init__(
        self,
        index: int,
        name: str,
        levels: Optional[Pot[Level] | None] = None,
        is_complete=False,
    ):
        """Chapter component contains chapter data of each chapter in game,
        This Class is universal interface for Chapter all over the app.
        We just work with this class when we intract with our Chapters.

        Parameters
        ----------
        index: int
            The index of each chapter inside chapter list in "".json"" file
        name : string
            The name of chapter.
        levels : Pot[Level] or None, optional
            levels of each chapter.
        is_complete : bool, optional
            Status of chapter completion
        """
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
            "levels": [level.as_dict() for level in self.levels] if self.levels else [],
        }

    @property
    def levels(self) -> Union[Pot[Level], None]:
        return self._levels

    @levels.setter
    def levels(self, levels: Optional[Pot[Level] | None]):
        self._levels = levels
