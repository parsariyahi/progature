from typing import Dict, Any
from pathlib import Path
import json

from progature.engine.components import Game


class GameHandler:
    def __init__(self, game_path: str):
        """Game handler that handles games files,
        This class is an interface between python and json.

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
        self._write_on_game("is_complete", True)

    def chapter_complete(self, chapter_index: int) -> None:
        """Write ``True`` on ``is_complete`` for chapter. 

        Parameters
        ----------
        chapter_index: int
            Index of the chapter you want to complete.
        """
        self._write_on_chapter("is_complete", True, chapter_index)

    def level_complete(self, chapter_index: int, level_index: int) -> None:
        """Write ``True`` on ``is_complete`` for level. 

        Parameters
        ----------
        chapter_index: int
            Index of the level's chapter you want to complete.
        level_index: int
            Index of the level you want to complete.
        """
        self._write_on_level("is_complete", True, chapter_index, level_index)

    def quest_complete(self, chapter_index, level_index, quest_index):
        """Write ``True`` on ``is_complete`` for quest. 

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
