from progature.engine.components.quest import Quest
from progature.engine.components.level import Level
from progature.engine.components.chapter import Chapter
from progature.engine.components.skill import Skill

class QuestUtil:

    @staticmethod
    def create_quest():
        return Quest(0, "random quest")

    @staticmethod
    def create_quest_bulk(count: int = 10):
        quests = []
        for counter in range(0, count):
            quests.append(
                Quest(counter, f"quest{str(counter)}")
            )

        return quests


class LevelUtil:

    @staticmethod
    def create_level():
        quests = QuestUtil.create_quest_bulk(count=5)
        return Level(0, "random level", quests=quests)

    @staticmethod
    def create_level_bulk(count: int = 10):
        levels = []
        for counter in range(0, count):
            quests = QuestUtil.create_quest_bulk(5)
            levels.append(
                Level(counter, f"level{str(counter)}", quests=quests)
            )

        return levels


class ChapterUtil:

    @staticmethod
    def create_chapter():
        levels = LevelUtil.create_level_bulk(5)
        return Chapter(0, "random chapter", levels=levels)

    @staticmethod
    def create_chapter_bulk(count: int = 10):
        chapters = []
        for counter in range(0, count):
            levels = LevelUtil.create_level_bulk(5)
            chapters.append(
                Chapter(counter, f"chapter{str(counter)}", levels=levels)
            )

        return chapters


class SkillUtil:

    @staticmethod
    def create_skill():
        return Skill("random chapter")