from progature.engine.components import (
    Skill, Chapter, Level, Quest
)


class PythonGame():

    def __init__(self):
        self.skill = Skill("python")
        self.chapters = [
            Chapter("learn basics"),
            Chapter("learn OOP"),
            Chapter("learn web development"),
        ]

        self.levels = {
            "1": [
                Level("one"),
                Level("two"),
                Level("three"),
            ],
            "2": [
                Level("one"),
                Level("two"),
                Level("three"),
                Level("four"),
            ]
        }

        self.quests = {
            "1": [
                Quest("learn variabels"),
                Quest("learn loops"),
            ],
            "2": [
                Quest("learn something"),
            ]
        }