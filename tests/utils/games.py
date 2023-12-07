import os
from pathlib import Path
import json

from progature.utils.component import(
    create_game, create_skill,
    create_bulk_chapters,
    create_bulk_levels,
    create_bulk_quest,
)

def create_test_game():
    game_json = {
        "file_path": "test_game.json",
        "name": "python basic",
        "skill": "python basic",
        "is_complete": False,
        "chapters": [
            {
                "index": 0,
                "name": "variables",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "integers",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "create integers",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "print some integers",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "strings",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "create strings",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "print strings",
                                "is_complete": False,
                            },
                            {
                                "index": 2,
                                "name": "write a program that prints your name",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 2,
                        "name": "list and tupes",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "create list and tuples",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "lists VS. tuples",
                                "is_complete": False,
                            },
                            {
                                "index": 2,
                                "name": "store names in a list and tuples and work with them",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 1,
                "name": "operations",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "addition",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "add two integers",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "concat two strings",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "subtraction",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "subtrac integers",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "use subtraction on strings",
                                "is_complete": False,
                            },
                            {
                                "index": 2,
                                "name": "write basic calculator",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 2,
                        "name": "multiplication and division",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "multiply on integers",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "division in python",
                                "is_complete": False,
                            },
                            {
                                "index": 2,
                                "name": "use math built-in library",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 2,
                "name": "loops",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "for loops",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "loop on lists",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "loop on tuples",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "while loop",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "create command line interface",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "use while loop like other languages loops",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 3,
                "name": "functions",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "args and params",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "args VS. params",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "type hintings",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "returns and yields",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "returns VS. yields",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "when to use which",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 4,
                "name": "classes",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "OOP",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "basic concepts of OOP",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "dunder methods like __init__",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "inheritance",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "multi inheritance",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "super() function in classes",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
        ]
    }
    skill = create_skill(game_json["skill"])
    game = create_game(game_json["file_path"],
                       game_json["name"],
                       skill,)
    game.chapters = create_bulk_chapters(chapters=game_json["chapters"])
    for chapter in game.chapters:
        chapter.levels = create_bulk_levels(game_json["chapters"][chapter.index]["levels"])
        for level in chapter.levels:
            level.quests = create_bulk_quest(game_json["chapters"][chapter.index]["levels"][level.index]["quests"])

    path = Path("progature/db/games/") / game.file_path
    with open(path, "w") as file:
        json.dump(game.as_dict(), file, indent=4)


def cleanup_test_game():
    file_name = "test_game.json"
    file_path = Path("progature/db/games/") / file_name

    if os.path.isfile(file_path):
        os.remove(file_path)