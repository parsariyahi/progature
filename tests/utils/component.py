from progature.engine.components.quest import Quest
from progature.engine.components.level import Level

class QuestUtil:

    @staticmethod
    def create_quest():
        return Quest("random quest")

    @staticmethod
    def create_quest_bulk(count: int = 10):
        quests = []
        for counter in range(0, count):
            quests.append(
                Quest(f"quest{str(counter)}")
            )

        return quests


class LevelUtil:

    @staticmethod
    def create_level():
        quests = QuestUtil.create_quest_bulk(count=5)
        return Level("random level", quests=quests)

    @staticmethod
    def create_level_bulk(count: int = 10):
        levels = []
        for counter in range(0, count):
            quests = QuestUtil.create_quest_bulk(5)
            levels.append(
                Level(f"level{str(counter)}", quests=quests)
            )

        return levels