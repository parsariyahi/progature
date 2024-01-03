"""`Components` module
This module is our components, we have `Game`, `Skill`, `Chapter`, `Level`, `Quest` components. <br>

## Game
games are main compoent of the app, each `Game` has a `Skill` and none or many `Chapter`'s.
you can have custom games, our games stored in `JSON` file formats, the path is `progature/db/games/`. <br>

## Skill
when you play a `Game`, you want to achive a skill in your real life, this component will show what skill you achive. <br>

## Chapter
chapters are a part of `Game` component, each `Skill` you want to achive has some chapters or topics to learn, this component will handle that.
we offer you `Chapter` to put your needed topics, and complete each chatper to achive your `Skill` and finish the `Game`. <br>

## Level
levels are a part of `Chapter` component, each `Chapter` has none or many `Level`'s, when you want to play games you need to complete levels to finish the chapter.
this compoent is some sub topics of a topic.

## Quest
quests are a part of `Level` component, each `Level` has none or many `Quest`'s, when you enter a `Level` you need to do some quests, you need to write a simple project,
or learn how to write a `Hello World`, so these kind of things are `Quest`'s in our app, when you finish all quests of a `Level` you will complete the `Level`.
"""
from .game import Game
from .skill import Skill
from .chapter import Chapter
from .level import Level
from .quest import Quest

__all__ = [
    "Game",
    "Skill",
    "Chapter",
    "Level",
    "Quest",
]
