import json

from progature.engine.structures.pots import (
    ChapterPot,
    LevelPot,
    QuestPot,
)
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
                ch = Chapter(chapter["name"], is_complete=chapter["is_complete"])
                levels_json = chapter["levels"]

                for level in levels_json:
                    lv = Level(level["name"], is_complete=level["is_complete"])
                    quests_json = level["quests"]

                    for quest in quests_json:
                        quests.append(
                            Quest(quest["name"], is_complete=quest["is_complete"])
                        )

                    lv.quests = QuestPot(quests)
                    quests = []

                    levels.append(lv)

                ch.levels = LevelPot(levels)
                levels = []

                chapters.append(ch)

            skill = Skill(game_json["skill"])
            game = Game(game_json["name"], skill, is_complete=game_json["is_complete"])
            game.chapters = ChapterPot(chapters)

            return game