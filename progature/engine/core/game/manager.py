from typing import Union

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.game.handler import GameHandler
from progature.engine.components import Game, Skill, Chapter, Level, Quest
from progature.engine.structures import Pot


class GameManager:
    """`GameManager` is the main interface between `GUI` and `Python` objects.
    This class works as an `API` for `GUI`.
    `GameManger` uses `GameHandler` and `GameLoader` to work with `JSON` files.

    Attributes
    ----------
    game: Game
        `Game` object that we want to manage.
    _handler: GameHandler
        `GameHandler` object that will handler the `JSON` part of the `Game`.
    """
    def __init__(self, game_path: str) -> None:
        """Game manager that manage games inside app,
        This class is an interface between user and games.

        Parameters
        ----------
        game_path: str
            Path of the game we want to work with.
        """
        self.game = GameLoader.load(game_path)
        self._handler = GameHandler(game_path)
        self.current_chapter_index = 0

    def game_name(self) -> str:
        """Returns the `name` property of `Game` object.

        Returns
        ------- 
        str
            `name` of the game
        """
        return self.game.name

    def game_skill(self) -> Union[Skill, None]:
        """Returns the `skill` property of `Game` object.

        Returns
        ------- 
        Skill or None
            `skill` of the game
        """
        return self.game.skill

    def game_complete(self) -> None:
        """Wrtie ``True`` on ``is_complete``.
        This method will make the game completed
        """
        with self._handler as h:
            h.game_complete()
            self.game.is_complete = True

    def chapter_complete(self, chapter_index: int) -> None:
        """Write `True` on `is_complete` for `Chapter`,
        This method will run `handler.chapter_complete()`.

        Parameters
        ----------
        chapter_index: int
            Index of the chapter you want to complete.
        """
        with self._handler as h:
            h.chapter_complete(chapter_index)
            self.game.chapters[chapter_index].is_complete = True

    def level_complete(self, chapter_index: int, level_index: int) -> None:
        """Write `True` on `is_complete` for `Level`,
        This method will run `handler.level_complete()`.

        Parameters
        ----------
        chapter_index: int
            Index of the level's chapter you want to complete.
        level_index: int
            Index of the level you want to complete.
        """
        with self._handler as h:
            h.level_complete(chapter_index, level_index)
            self.game.chapters[chapter_index].levels[level_index].is_complete = True

    def quest_complete(self, chapter_index: int, level_index: int, quest_index: int) -> None:
        """Write `True` on `is_complete` for `Quest`,
        This method will run `handler.quest_complete()`.

        Parameters
        ----------
        chapter_index: int
            Index of the quest's level's chapter you want to complete.
        level_index: int
            Index of the quest's level you want to complete.
        quest_index: int
            Index of the quest you want to complete.
        """
        with self._handler as h:
            h.quest_complete(chapter_index, level_index, quest_index)
            self.game.chapters[chapter_index].levels[level_index].quests[
                quest_index
            ].is_complete = True

    def chapters(self) -> Union[Pot[Chapter], None]:
        """Returns the `chapters` property of `Game` object.

        Returns
        -------
        Pot[Chapter] or None
            `chapters` of the game.
        """
        return self.game.chapters

    def current_chapter(self):
        return self.game.chapters[self.current_chapter_index]

    def next_cahpter(self):
        self.current_chapter_index += 1
        return self.current_chapter()

    def nth_chapter(self, index):
        return self.game.chapters[index]

    def get_chapter_levels(self, chapter_index) -> Union[Pot[Level], None]:
        chapter: Chapter = self.game.chapters[chapter_index]
        return chapter.levels

    def get_level_quests(self, chapter_index, level_index) -> Union[Pot[Quest], None]:
        level: Level = self.game.chapters[chapter_index].levels[level_index]
        return level.quests
