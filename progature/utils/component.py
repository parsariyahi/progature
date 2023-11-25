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


def create_bulk_levels(level_names: List[str], level_quests: List[Pot[Quest]]) -> Pot[Level]:
    level_list = []
    for level_index, level_name in enumerate(level_names):
        level_list.append(
            Level(index=level_index, name=level_name, quests=level_quests[level_index])
        )

    return Pot(level_list)


def create_bulk_chapters(chapter_names: List[str], chapter_levels: List[Pot[Level]]) -> Pot[Chapter]:
    chapter_list = []
    for chapter_index, chapter_name in enumerate(chapter_names):
        chapter_list.append(
            Chapter(index=chapter_index, name=chapter_name, levels=chapter_levels[chapter_index])
        )

    return Pot(chapter_list)


def create_skill(name: str) -> Skill: 
    return Skill(name=name)


def create_game(file_path: str, name: str, skill: Skill, chapters: Pot[Chapter]) -> Game:
    game = Game(file_path=file_path,
                name=name,
                skill=skill,
                chapters=chapters,
                is_complete=False)

    return game
