import json

from progature.engine.components import (
    Game, Skill, Chapter, Level, Quest
)

class GameLoader:

    @staticmethod
    def load(file_path) :
        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()
            game_json = json.loads(content)
            chapters_json = game_json["chapters"]

            chapters = []
            levels = []
            quests = []

            for chapter in chapters_json:
                levels_json = chapter["levels"]
                for level in levels_json:
                    quests_json = level["quests"]
                    for quest in quests_json:
                        quests.append(Quest(quest))
                    levels.append(Level(level["name"], quests))
                chapters.append(Chapter(chapter["name"], levels))

            skill = Skill(game_json["skill"], chapters)

            game = Game(game_json["name"], skill)

            return game