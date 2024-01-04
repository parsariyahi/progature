from typing import Dict, Any
from pathlib import Path
import json

from progature.engine.components import Game


class GameHandler:
    """This class is used to comunicate with `JSON` files,
    We use `GameHandler` in other part of our apps to change our `JSON` db.
    This class is an `API` between `Python` and `JSON`.

    Attributes
    ----------
    game_path: str
        Path of the `Game`'s `JSON` file.
    game_json: dict
        `dict` representation of the `Game`'s `JSON` file.

    Examples
    --------
    >>> g_h = GameHandler("GAME_PATH")
    >>> with g_h as handler:
    >>>     handler.game_complete()
    """
    def __init__(self, game_path: str):
        """Game handler that handles game's files,
        This class is an interface between `Python` and `JSON`.

        Parameters
        ----------
        game_path: str
            Path of the game we want to work with it's files.
        """
        self.game_path = game_path
        self.game_json = {}

    def __enter__(self):
        self.game_json = self._load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._write()

    def game_complete(self):
        """Write `True` on `is_complete` for `Game` object. 
        This method makes the `Game` and its `JSON` file completed.
        """
        self._write_on_game("is_complete", True)

    def chapter_complete(self, chapter_index: int) -> None:
        """Write `True` on `is_complete` for `Chapter` object. 

        Parameters
        ----------
        chapter_index: int
            Index of the chapter you want to complete.
        """
        self._write_on_chapter("is_complete", True, chapter_index)

    def level_complete(self, chapter_index: int, level_index: int) -> None:
        """Write `True` on `is_complete` for `Level` object. 

        Parameters
        ----------
        chapter_index: int
            Index of the level's chapter you want to complete.
        level_index: int
            Index of the level you want to complete.
        """
        self._write_on_level("is_complete", True, chapter_index, level_index)

    def quest_complete(self, chapter_index: int, level_index: int, quest_index: int):
        """Write `True` on `is_complete` key for `Quest`. 

        Parameters
        ----------
        chapter_index: int
            Index of the quest's level's chapter you want to complete.
        level_index: int
            Index of the quest's level you want to complete.
        quest_index: int
            Index of the quest you want to complete.
        """
        self._write_on_quest(
            "is_complete", True, chapter_index, level_index, quest_index
        )

    def _load(self) -> Dict:
        with open(self.game_path, "r+") as file:
            return json.load(file)

    def _write(self):
        with open(self.game_path, "w") as file:
            json.dump(self.game_json, file, indent=4)

    def _write_on_game(self, key, value):
        self.game_json[key] = value

    def _write_on_chapter(self, key, value, chapter_index):
        self.game_json["chapters"][chapter_index][key] = value

    def _write_on_level(self, key, value, chapter_index, level_index):
        self.game_json["chapters"][chapter_index]\
                      ["levels"][level_index][key] = value

    def _write_on_quest(self, key, value, chapter_index, level_index, quest_index):
        self.game_json["chapters"][chapter_index]\
                      ["levels"][level_index]\
                      ["quests"][quest_index][key] = value
