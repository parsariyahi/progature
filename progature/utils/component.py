from typing import List

from progature.engine.components import (
    Game, Skill, Chapter,
    Level, Quest)
from progature.engine.structures import Pot


def create_bulk_quest(quest_names: List[str]) -> Pot[Quest]:
    quest_list = []
    for quest_index, quest_name in enumerate(quest_names):
        quest_list.append(
            Quest(index=quest_index, name=quest_name, is_complete=False)
        )
    
    return Pot(quest_list)


def create_bulk_levels(level_names: List[str], level_quests: List[Pot[Quest]] | None = None) -> Pot[Level]:
    level_list = []
    for level_index, level_name in enumerate(level_names):
        level = Level(index=level_index, name=level_name)
        if level_quests:
            level.quests = level_quests[level_index]
        level_list.append(level)

    return Pot(level_list)


def create_bulk_chapters(chapter_names: List[str], chapter_levels: List[Pot[Level]] | None = None) -> Pot[Chapter]:
    chapter_list = []
    for chapter_index, chapter_name in enumerate(chapter_names):
        chapter = Chapter(index=chapter_index, name=chapter_name)
        if chapter_levels:
            chapter.levels = chapter_levels[chapter_index]
        chapter_list.append(chapter)

    return Pot(chapter_list)


def create_skill(name: str) -> Skill: 
    return Skill(name=name)


def create_game(file_path: str, name: str, skill: Skill, chapters: Pot[Chapter] | None = None) -> Game:
    game = Game(file_path=file_path,
                name=name,
                skill=skill,
                chapters=chapters,
                is_complete=False)

    return game
