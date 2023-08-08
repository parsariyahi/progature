from __future__ import annotations
from typing import List 

from progature.engine.components.chapter import Chapter

class Skill:

    def __init__(self, name, chapters: List[Chapter] = None):
        self.name = name
        self.chapters = chapters