from pathlib import Path
import PySimpleGUI as pg

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.game.manager import GameManager
from progature.utils.loader import load_all_games
from progature.engine.structures import Pot
from progature.engine.components import Game


def main_window() -> pg.Window:
    layout = []
    game_pot = load_all_games()
    games = game_pot.items
    layout.append(
        [
            pg.Listbox(
                games,
                size=(100, 10),
                font=("Arial Bold", 14),
                expand_y=True,
                expand_x=True,
                enable_events=True,
                key="_GAMES_",
            )
        ]
    )

    layout.append(
        [
            pg.Button("Close", enable_events=True, key="_CLOSE_"),
            pg.Button("Open Game", enable_events=True, key="_GAME_OPEN_"),
        ]
    )

    window = pg.Window(
        "Progature", layout=layout, size=(500, 500), resizable=True, finalize=True
    )
    
    return window

def game_window(manager: GameManager) -> pg.Window:
    layout = []

    layout.append([pg.Text(f"Game name: {manager.game_name()}")])

    layout.append([pg.Text(f"Game skill: {manager.game_skill()}")])

    layout.append([pg.Text(f"Game Completion: {manager.game.is_complete}")])

    layout.append(
        [
            pg.Button("Chapters", enable_events=True, key="_CHAPTER_LIST_"),
            pg.Button("Complete", enable_events=True, key="_GAME_COMPLETE_"),
        ]
    )

    layout.append([pg.Button("Close", enable_events=True, key="_CLOSE_")])

    window = pg.Window(
        "Game", layout=layout, size=(500, 500), resizable=True, finalize=True
    )

    while True:
        event, values = window.read(timeout=10000)

        if event == pg.WIN_CLOSED or event == "_CLOSE_":
            window.close()

            break

        if event == "_GAME_COMPLETE_":
            manager.game_complete()

            continue

        if event == "_CHAPTER_LIST_":
            chapter_window(manager)

            continue

def chapter_window(manager: GameManager) -> pg.Window:
    layout = []
    chapters = manager.chapters().items
    layout.append(
        [
            pg.Listbox(
                chapters,
                size=(100, 10),
                font=("Arial Bold", 14),
                expand_y=True,
                expand_x=True,
                enable_events=True,
                key="_CHAPTERS_",
            )
        ]
    )

    layout.append(
        [
            pg.Button("Close", enable_events=True, key="_CLOSE_"),
            pg.Button("Levels", enable_events=True, key="_LEVELS_LIST_"),
            pg.Button("Complete", enable_events=True, key="_CHAPTER_COMPLETE_"),
        ]
    )

    window = pg.Window(
        "Chpater", layout=layout, size=(500, 500), resizable=True, finalize=True
    )
    # return window
    while True:
        event, values = window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            window.close()
            break

        if event == "_LEVELS_LIST_":
            if values["_CHAPTERS_"]:
                chapter = values["_CHAPTERS_"][0]
                if chapter:
                    level_window(manager, chapter.index)
            else:
                pg.popup_error("Please select a chapter")

            continue

        if event == "_CHAPTER_COMPLETE_":
            if values["_CHAPTERS_"]:
                chapter = values["_CHAPTERS_"][0]
                if chapter:
                    manager.chapter_complete(chapter.index)
                    chapters = manager.chapters().items
                    window["_CHAPTERS_"].update(chapters)
            else:
                pg.popup_error("Please select a chapter")

            continue


def level_window(manager: GameManager, chapter_index) -> pg.Window:
    layout = []
    levels = manager.chapters()[chapter_index].levels.items
    layout.append(
        [
            pg.Listbox(
                levels,
                size=(100, 10),
                font=("Arial Bold", 14),
                expand_y=True,
                expand_x=True,
                enable_events=True,
                key="_LEVELS_",
            )
        ]
    )

    layout.append(
        [
            pg.Button("Close", enable_events=True, key="_CLOSE_"),
            pg.Button("Quests", enable_events=True, key="_QUESTS_LIST_"),
            pg.Button("Complete", enable_events=True, key="_LEVEL_COMPLETE_"),
        ]
    )

    window = pg.Window(
        "Level", layout=layout, size=(500, 500), resizable=True, finalize=True
    )
    # return window
    while True:
        event, values = window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            window.close()
            break

        if event == "_QUESTS_LIST_":
            if values["_LEVELS_"]:
                level = values["_LEVELS_"][0]
                if level:
                    quest_window(manager, chapter_index, level.index)
            else:
                pg.popup_error("Please select a level")

            continue

        if event == "_LEVEL_COMPLETE_":
            if values["_LEVELS_"]:
                level = values["_LEVELS_"][0]
                if level:
                    manager.level_complete(chapter_index, level.index)
                    levels = manager.chapters()[chapter_index].levels.items
                    window["_LEVELS_"].update(levels)
            else:
                pg.popup_error("Please select a level")

            continue


def quest_window(manager: GameManager, chapter_index, level_index) -> pg.Window:
    layout = []
    quests = manager.chapters()[chapter_index].levels[level_index].quests.items
    layout.append(
        [
            pg.Listbox(
                quests,
                size=(100, 10),
                font=("Arial Bold", 14),
                expand_y=True,
                expand_x=True,
                enable_events=True,
                key="_QUESTS_",
            )
        ]
    )

    layout.append(
        [
            pg.Button("Close", enable_events=True, key="_CLOSE_"),
            pg.Button("Complete", enable_events=True, key="_QUEST_COMPLETE_"),
        ]
    )

    window = pg.Window(
        "Quest", layout=layout, size=(500, 500), resizable=True, finalize=True
    )
    # return window
    while True:
        event, values = window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            window.close()
            break

        if event == "_QUEST_COMPLETE_":
            if values["_QUESTS_"]:
                quest = values["_QUESTS_"][0]
                if quest:
                    manager.quest_complete(chapter_index, level_index, quest.index)
                    quests = (
                        manager.chapters()[chapter_index].levels[level_index].quests.items
                    )
                    window["_QUESTS_"].update(quests)
            else:
                pg.popup_error("Please select a quest")

            continue