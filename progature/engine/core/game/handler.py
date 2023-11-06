from typing import Dict, Any
from pathlib import Path
import json

from progature.engine.components import Game

class GameHandler:

    def __init__(self, game: Game):
        self.game = game
        self.game_json = {}

    def __enter__(self):
        self.game_json = self._load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._write()

    def game_complete(self):
        self._write_on_game("is_complete", True)

    def chapter_complete(self, chapter_index):
        self._write_on_chapter("is_complete", True, chapter_index)

    def level_complete(self, level_index):
        self._write_on_level("is_complete", True, level_index)

    def quest_complete(self, quest_index):
        self._write_on_quest("is_complete", True, quest_index)
    
    def _load(self) -> Dict:
        with open(self.game.file_path, "r+") as file:
            return json.load(file)

    def _write(self):
        with open(self.game.file_path, "w") as file:
            json.dump(self.game_json, file, indent=4)

    def _write_on_game(self, key, value):
       self.game_json[key] = value

    def _write_on_chapter(self, key, value, chapter_index):
        self.game_json["chapters"][chapter_index][key] = value

    def _write_on_level(self, key, value, chapter_index, level_index):
        self.game_json["chapters"][chapter_index]["levels"][level_index][key] = value

    def _write_on_quest(self, key, value, chapter_index, level_index, quest_index):
        self.game_json["chapters"][chapter_index]["levels"][level_index]["quests"][quest_index][key] = value