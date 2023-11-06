from typing import Union

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.game.handler import GameHandler
from progature.engine.components import (
    Game, Skill, Chapter, Level
)
from progature.engine.structures.pots import (
    ChapterPot,
    LevelPot,
    QuestPot,
)

class GameManager:

    def __init__(self, game_path: str):
        self.game = GameLoader.load(game_path)
        self._handler = GameHandler(self.game)
        self.current_chapter_index = 0

    def game_name(self) -> str:
        return self.game.name

    def game_skill(self) -> Union[Skill, None]:
        return self.game.skill

    def game_complete(self):
        with self._handler as h:
            h.game_complete()
            self.game.is_complete = True

    def chapter_complete(self, chapter_index):
        with self._handler as h:
            h.chapter_complete(chapter_index)
            self.game.chapters[chapter_index].is_compelte = True

    def level_complete(self, chapter_index, level_index):
        with self._handler as h:
            h.level_complete(chapter_index, level_index)
            self.game.chapters[chapter_index].levels[level_index].is_complete = True

    def quest_complete(self, chapter_index, level_index, quest_index):
        with self._handler as h:
            h.quest_complete(chapter_index, level_index, quest_index)
            self.game.chapters[chapter_index].levels[level_index].quests[quest_index].is_complete = True

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