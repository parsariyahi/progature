"""
Initiate point of the app is here.
"""
from progature.utils.component import(
    create_game, create_skill,
    create_bulk_chapters,
    create_bulk_levels,
    create_bulk_quest,
)

def create_basic_python_game():
    game_json = {
        "file_path": "python_basic.json",
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

    return game


def create_advanced_python_game():
    game_json = {
        "file_path": "python_advanced.json",
        "name": "python advanced",
        "skill": "python advanced",
        "is_complete": False,
        "chapters": [
            {
                "index": 0,
                "name": "advanced function",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "map function",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "how to use map function",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "use map function in your program",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "zip function",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "what is zip function",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "write simple program with zip function",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 1,
                "name": "itertools",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "itertools lib",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "use itertools",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "what is __iter__ in classes",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "itertools functions",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "count function",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "cycle function",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 2,
                "name": "lambda functions and decorators",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "lambda functions",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "anonymous functions",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "lambda functions VS. regular functions",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "decorators",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "what is wrapper in functions",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "how to call functions in other functions",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 3,
                "name": "threading",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "threads",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "what is main thread",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "different types of threads",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "threads VS. processes",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "multi processing VS. threading",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "is threading really simultaneously",
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

    return game


def create_data_structure_intro_game():
    game_json = {
        "file_path": "data_structure_intro.json",
        "name": "data structure intoduction",
        "skill": "data structure",
        "is_complete": False,
        "chapters": [
            {
                "index": 0,
                "name": "introduction to data structure",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "arrays",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "what are arrays",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "how arrays work",
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
                                "name": "how to use strings",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "strings in low level computing",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 1,
                "name": "linear data structures",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "linked lists",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "linked lists VS. arrays",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "how poiners works in linked lists",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "queues",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "queue example in real life",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "do a simple project with queues",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 2,
                        "name": "stacks",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "stacks VS. queues",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "use stacks in your project",
                                "is_complete": False,
                            },
                        ]
                    },
                ]
            },
            {
                "index": 2,
                "name": "non-linear data structures",
                "is_complete": False,
                "levels": [
                    {
                        "index": 0,
                        "name": "trees",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "dfs and bfs",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "use trees",
                                "is_complete": False,
                            },
                        ]
                    },
                    {
                        "index": 1,
                        "name": "graphs",
                        "is_complete": False,
                        "quests": [
                            {
                                "index": 0,
                                "name": "graph VS. trees",
                                "is_complete": False,
                            },
                            {
                                "index": 1,
                                "name": "create social medai with graphs",
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

    return game
