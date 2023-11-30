from typing import Dict, List, Any

from progature.engine.components import (
    Game, Skill, Chapter,
    Level, Quest)
from progature.engine.structures import Pot


def create_bulk_quest(quests: List[Dict[Any, Any]]) -> Pot[Quest]:
    quest_list = []
    for quest in quests:
        index = quest.get("index", None)
        name = quest.get("name", None)
        is_complete = quest.get("is_complete", None)
        quest_list.append(
            Quest(index=index,
                  name=name,
                  is_complete=is_complete)
        )
    
    return Pot(quest_list)


def create_bulk_levels(levels: List[Dict[Any, Any]]) -> Pot[Level]:
    level_list = []
    for level in levels:
        index = level.get("index", None)
        name = level.get("name", None)
        is_complete = level.get("is_complete", None)
        level_list.append(
            Level(index=index, 
                  name=name,
                  is_complete=is_complete)
        )

    return Pot(level_list)


def create_bulk_chapters(chapters: List[Dict[Any, Any]]) -> Pot[Chapter]:
    chapter_list = []
    for chapter in chapters:
        index = chapter.get("index", None)
        name = chapter.get("name", None)
        is_complete = chapter.get("is_complete", None)
        chapter_list.append(
            Chapter(index=index,
                    name=name,
                    is_complete=is_complete)
        )

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
