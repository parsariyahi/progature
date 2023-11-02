from pathlib import Path
import json


class GameHandler:

    def __init__(self, game_path):
        self.path = game_path

    def game_complete(self):
        self._write("is_complete", True)

    def _write(self, key, value):
        if not self.path:
            return 

        with open(self.path, "r+") as file:
            game_json = json.load(file)

            game_json = self._write_on_game(game_json, key, value)

            file.seek(0)
            json.dump(game_json, file, indent=4)
            file.truncate()

        return game_json

    def _write_on_game(self, game, key, value):
       game[key] = value
       return game

    @classmethod
    def _write_on_chapter(cls):
        pass

    @classmethod
    def _write_on_level(cls):
        pass

    @classmethod
    def _write_on_quest(cls):
        pass
