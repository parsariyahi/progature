from __future__ import annotations
from typing import List

from progature.engine.components.quest import Quest

class Level:
    
    def __init__(self, name: str, quests: List[Quest] = None) -> str:
        self.name = name
        self.quests = quests