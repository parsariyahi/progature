from __future__ import annotations
from typing import List, Optional, Union

from progature.engine.components.level import Level

class Chapter:

    def __init__(self, name: str, levels: Optional[List[Level] | None] = None, is_complete=False):
        self.name = name
        self.levels = levels
        self.is_complete = is_complete

    @property 
    def levels(self) -> Union[List[Level], None]:
        return self._levels

    @levels.setter
    def levels(self, levels: Optional[List[Level] | None]):
        self._levels = levels