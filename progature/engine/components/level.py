from __future__ import annotations
from typing import List, Optional, Union

from progature.engine.components.quest import Quest

class Level:
    
    def __init__(self, name: str, quests: Optional[List[Quest] | None] = None, is_complete=False) -> None:
        self.name = name
        self.quests = quests
        self.is_complete = is_complete

    @property
    def quests(self) -> Union[List[Quest], None]:
        return self._quests

    @quests.setter
    def quests(self, quests: Optional[List[Quest] | None]) -> None:
        self._quests = quests