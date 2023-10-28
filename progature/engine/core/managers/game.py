from typing import Union

from progature.engine.components import (
    Game, Skill, Chapter, Level
)
from progature.engine.structures.pots import (
    ChapterPot,
    LevelPot,
    QuestPot,
)

class GameManager:

    def __init__(self, game: Game):
        self.game = game
        self.current_chapter_index = 0

    def game_name(self) -> str:
        return self.game.name

    def game_skill(self) -> Union[Skill, None]:
        return self.game.skill

    def chapters(self) -> Union[ChapterPot, None]:
        return self.game.chapters

    def current_chapter(self) :
        return self.game.chapters[self.current_chapter_index]

    def next_cahpter(self):
        self.current_chapter_index += 1
        return self.current_chapter()

    def nth_chapter(self, index):
        return self.game.chapters[index]

    def get_chapter_levels(self, chapter_index) -> Union[LevelPot, None]:
        chapter: Chapter =  self.game.chapters[chapter_index]
        return chapter.levels

    def get_level_quests(self, chapter_index, level_index) -> Union[QuestPot, None]:
        level: Level = self.game.chapters[chapter_index].levels[level_index]
        return level.quests