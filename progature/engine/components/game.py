from __future__ import annotations
from typing import Optional, Union

from progature.engine.components.skill import Skill

class Game:

    def __init__(self, name, skill: Optional[Skill | None] = None) -> None:
        self.name = name
        self.skill = skill
    
    @property
    def skill(self) -> Union[Skill, None]:
        return self._skill

    @skill.setter
    def skill(self, skill: Optional[Skill | None]):
        self._skill = skill