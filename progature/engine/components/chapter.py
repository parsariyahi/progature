from __future__ import annotations
from typing import List

from progature.engine.components.level import Level

class Chapter:

    def __init__(self, name: str, levels: List[Level]):
        self.name = name
        self.levels = levels