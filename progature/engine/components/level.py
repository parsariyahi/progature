from __future__ import annotations
from typing import List, Optional, Union

from progature.engine.structures import Pot
from progature.engine.components.quest import Quest

class Level:
    
    def __init__(self, index: int, name: str, quests: Optional[Pot[Quest] | None] = None, is_complete=False) -> None:
        self.index = index
        self.name = name
        self.quests = quests
        self.is_complete = is_complete

    def __str__(self) -> str:
        string = f"{self.index}.{self.name}:{self.is_complete}"
        return string

    def __eq__(self, other) -> bool:
        if isinstance(other, Level):
            return self.name == other.name

        raise TypeError("Type Error Level")

    @property
    def quests(self) -> Union[Pot[Quest], None]:
        return self._quests

    @quests.setter
    def quests(self, quests: Optional[Pot[Quest] | None]) -> None:
        self._quests = quests