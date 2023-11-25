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
    quest_names = [
        "my first hello world",
        "print function",
    ]

    quest_pot = create_bulk_quest(quest_names)

    for quest_index, quest in enumerate(quest_pot):
        assert quest.name == quest_names[quest_index]

def test_create_bulk_levels():
    level_names = [
        "how to work with strings",
        "if statements"
    ]

    quests = [
        Pot(QuestUtil.create_quest_bulk(10)),
        Pot(QuestUtil.create_quest_bulk(5)),
    ]


    level_pot = create_bulk_levels(level_names, quests)

    for level_index, level in enumerate(level_pot):
        assert level.quests == quests[level_index]

def test_create_bulk_chapters():
    chapter_names = [
        "functional programming",
        "OOP",
    ]

    levels = [
        Pot(LevelUtil.create_level_bulk(5)),
        Pot(LevelUtil.create_level_bulk(10)),
    ]

    chapter_pot = create_bulk_chapters(chapter_names, levels)

    for chapter_index, chapter in enumerate(chapter_pot):
        assert chapter.levels == levels[chapter_index]

def test_create_skill():
    skill_name = "python programming"

    skill = create_skill(skill_name)

    assert skill.name == skill_name

def test_create_game():
    game_name = "python basic game"
    game_file_path = "db/python_basic_game.json"
    game_skill = SkillUtil.create_skill()

    chapters = ChapterUtil.create_chapter_bulk(10)

    game = create_game(game_file_path, game_name, game_skill, chapters)


    assert game.name == game_name
    assert game.file_path == game_file_path
    assert game.skill == game_skill
    assert game.chapters == chapters

def test_create_full_game_with_component_utils():
    final_game = {
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
    
    # skill = create_skill(final_game["skill"])
    # chapters = create_bulk_chapters()
    # game = create_game("db/python_basic.json",
    #                    name=final_game["name"],
    #                    skill=skill,
    #                    chapters=chapters)