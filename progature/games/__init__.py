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
                ch = Chapter(chapter["name"])
                levels_json = chapter["levels"]

                for level in levels_json:
                    lv = Level(level["name"])
                    quests_json = level["quests"]

                    for quest in quests_json:
                        quests.append(Quest(quest))

                    lv.quests = quests
                    quests = []

                    levels.append(lv)

                ch.levels = levels
                levels = []

                chapters.append(ch)

            skill = Skill(game_json["skill"], chapters)

            game = Game(game_json["name"], skill)

            return game