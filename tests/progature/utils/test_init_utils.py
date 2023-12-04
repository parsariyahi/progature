from progature.utils.init import (
    create_basic_python_game,
    create_advanced_python_game,
)


def test_basic_python_game():
    game_json = {
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

    game = create_basic_python_game()

    assert game.as_dict() == game_json


def teat_create_advanced_python_game():
    game_json = {
        # "file_path": "python_advanced.json",
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

    game = create_advanced_python_game()

    assert game.as_dict() == game_json