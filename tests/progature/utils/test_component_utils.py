from progature.utils.component import (
    create_bulk_chapters,
    create_bulk_levels,
    create_bulk_quest,
    create_skill,
    create_game,
)
from progature.engine.structures import Pot

from tests.utils.component import (
    QuestUtil,
    LevelUtil,
    ChapterUtil,
    SkillUtil,
)


def test_create_bulk_quests():
    quests = [
        {
            "index": 0,
            "name": "my first hello world",
            "is_complete": False,
        },
        {
            "index": 1,
            "name": "print function",
            "is_complete": False,
        },
    ]

    quest_pot = create_bulk_quest(quests)

    for quest in quest_pot:
        assert quest.name == quests[quest.index]["name"]

def test_create_bulk_levels():
    levels = [
        {
            "index": 0,
            "name": "how to work with strings",
            "is_complete": False,
        },
        {
            "index": 1,
            "name": "if statements",
            "is_complete": False,
        },
    ]

    level_pot = create_bulk_levels(levels)

    for level in level_pot:
        assert level.index == levels[level.index]["index"]
        assert level.name == levels[level.index]["name"]
        assert level.is_complete == levels[level.index]["is_complete"]

def test_create_bulk_chapters():
    chapters = [
        {
            "index": 0,
            "name": "functional programming",
            "is_complete": False,
        },
        {
            "index": 1,
            "name": "OOP",
            "is_complete": False,
        },
    ]

    chapter_pot = create_bulk_chapters(chapters)

    for chapter in chapter_pot:
        assert chapter.index == chapters[chapter.index]["index"]
        assert chapter.name == chapters[chapter.index]["name"]
        assert chapter.is_complete == chapters[chapter.index]["is_complete"]

def test_create_skill():
    skill_name = "python programming"

    skill = create_skill(skill_name)

    assert skill.name == skill_name

def test_create_game():
    game_name = "python basic game"
    game_file_name = "python_basic_game.json"
    game_skill = SkillUtil.create_skill()

    chapters = ChapterUtil.create_chapter_bulk(10)

    game = create_game(game_file_name, game_name, game_skill, chapters)


    assert game.name == game_name
    assert game.file_name == game_file_name
    assert game.skill == game_skill
    assert game.chapters == chapters

def test_create_full_game_with_component_utils():
    final_game = {
        "file_name": "python_basic.json",
        "name": "basic python",
        "skill": "python programming language",
        "is_complete": False,
        "chapters": [
            {
                "index": 0,
                "name": "vars",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "integers",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "sum of ints",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "compare two ints",
                                "is_complete": False,
                            }
                        ]
                    },
                    {
                        "index": 1,
                        "name": "strings",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "sum of strings",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "compare two strings",
                                "is_complete": False,
                            }
                        ]
                    },
                ]
            },
            {
                "index": 1,
                "name": "loops",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "while loop",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "loop on lists",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "infinite loop",
                                "is_complete": False,
                            }
                        ]
                    },
                    {
                        "index": 1,
                        "name": "for loops",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "loop on a list",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "loop on other iterables",
                                "is_complete": False,
                            }
                        ]
                    },
                ]
            }
        ]
    }
    
    skill = create_skill(final_game["skill"])
    game = create_game("python_basic.json",
                       name=final_game["name"],
                       skill=skill)

    chapters_json = final_game["chapters"]
    # chapters_names = [chapter["name"] for chapter in chapters_json]    
    chapters = create_bulk_chapters(chapters_json)
    game.chapters = chapters
    for chapter in game.chapters:
        chapter_json = final_game["chapters"][chapter.index]
        chapter_levels_json = chapter_json["levels"]
        chapter.levels = create_bulk_levels(chapter_levels_json)

    for chapter in game.chapters:
        for level in chapter.levels:
            level_json = final_game["chapters"][chapter.index]["levels"][level.index]
            level_quests_json = level_json["quests"]
            level.quests = create_bulk_quest(level_quests_json)


    assert game.as_dict() == final_game

    for chapter in game.chapters:
        assert chapter.index == final_game["chapters"][chapter.index]["index"]
        assert chapter.name == final_game["chapters"][chapter.index]["name"]
        assert chapter.is_complete == final_game["chapters"][chapter.index]["is_complete"]

        for level in chapter.levels:
            assert level.index == final_game["chapters"][chapter.index]["levels"][level.index]["index"]
            assert level.name == final_game["chapters"][chapter.index]["levels"][level.index]["name"]
            assert level.is_complete == final_game["chapters"][chapter.index]["levels"][level.index]["is_complete"]

            for quest in level.quests:
                assert quest.index == final_game["chapters"][chapter.index]["levels"][level.index]["quests"][quest.index]["index"]
                assert quest.name == final_game["chapters"][chapter.index]["levels"][level.index]["quests"][quest.index]["name"]
                assert quest.is_complete == final_game["chapters"][chapter.index]["levels"][level.index]["quests"][quest.index]["is_complete"]