from __future__ import annotations

from progature.engine.components.skill import Skill

class Game:

    def __init__(self, name, skill: Skill) -> None:
        self.name = name
        self.skill = skill