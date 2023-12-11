import json
from pathlib import Path

from progature.engine.structures import Pot
from progature.engine.components import Game, Skill, Chapter, Level, Quest
from progature.settings.config import GAME_DIR_PATH


class GameLoader:
    @staticmethod
    def load(file_name: str) -> Game:
        """Game loader that loads games inside app,
        This class is an interface between app and json files to be loaded.

        Parameters
        ----------
        file_name: str
            Path of the game we want to work with.

        Returns
        -------
        Game
            Instance of the game's file Game.
        """
        # path = Path(GAME_DIR_PATH) / file_name
        with open(file_name, "r", encoding="utf8") as file:
            content = file.read()
            game_json = json.loads(content)
            chapters_json = game_json["chapters"]

            chapters = []
            levels = []
            quests = []

            for chapter in chapters_json:
                ch = Chapter(
                    chapter["index"],
                    chapter["name"],
                    is_complete=chapter["is_complete"],
                )
                levels_json = chapter["levels"]

                for level in levels_json:
                    lv = Level(
                        level["index"], level["name"], is_complete=level["is_complete"]
                    )
                    quests_json = level["quests"]

                    for quest in quests_json:
                        quests.append(
                            Quest(
                                quest["index"],
                                quest["name"],
                                is_complete=quest["is_complete"],
                            )
                        )

                    lv.quests = Pot(quests)
                    quests = []

                    levels.append(lv)

                ch.levels = Pot(levels)
                levels = []

                chapters.append(ch)

            skill = Skill(game_json["skill"])
            game = Game(
                file_name,
                game_json["name"],
                skill,
                is_complete=game_json["is_complete"],
            )
            game.chapters = Pot(chapters)

            return game
