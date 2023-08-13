import json

class GameLoader:

    @staticmethod
    def load(file_path) :
        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()
            game = json.loads(content)

            return game