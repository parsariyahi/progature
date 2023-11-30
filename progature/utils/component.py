from typing import Dict, List, Any

from progature.engine.components import (
    Game, Skill, Chapter,
    Level, Quest)
from progature.engine.structures import Pot


def create_bulk_quest(quests: List[Dict[Any, Any]]) -> Pot[Quest]:
    """Create quests in bulk,
    This function is utility for creating quests,
    Creation in this function is bulk type based on input (List).

    Parameters
    ----------
    quests: list
        List of quests in dict type.

    Returns
    -------
    Pot
        Pot object that contains Quest's.
    """
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
    """Create levels in bulk,
    This function is utility for creating levels,
    Creation in this function is bulk type based on input (List).

    Parameters
    ----------
    levels: list
        List of levels in dict type.

    Returns
    -------
    Pot
        Pot object that contains Level's.
    """
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
    """Create chapters in bulk,
    This function is utility for creating chapters,
    Creation in this function is bulk type based on input (List).

    Parameters
    ----------
    chapters: list
        List of chapters in dict type.

    Returns
    -------
    Pot
        Pot object that contains Chapter's.
    """
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
    """Create skill,
    This function is utility for creating skill,

    Parameters
    ----------
    name: str
        Chapter's name that you want to create.

    Returns
    -------
    Skill
        Skill object that is created.
    """
    return Skill(name=name)


def create_game(file_path: str, name: str, skill: Skill, chapters: Pot[Chapter] | None = None) -> Game:
    """Create Game,
    This function is utility for creating game,

    Parameters
    ----------
    file_path: str
        The file path that you want to game be saved in.

    name: str
        Name of the game you want to create

    skill: Skill
        Skill object that you want to assign to this game.

    chapters: Pot[Chapter], optional
        Chapter's that the game has.

    Returns
    -------
    Game
        Game object that is created.
    """
    game = Game(file_path=file_path,
                name=name,
                skill=skill,
                chapters=chapters,
                is_complete=False)

    return game
