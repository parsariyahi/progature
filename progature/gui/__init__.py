from pathlib import Path
import PySimpleGUI as pg

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.managers import GameManager
from progature.engine.structures.pots import ChapterPot, LevelPot, QuestPot
from progature.engine.components import Game

def init_layout():
    layout = []

    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path)
    manager = GameManager(game)

    chapter_list = manager.chapters()    


    list_box = pg.Listbox(chapter_list.items, size=(100, 10), font=('Arial Bold', 14), expand_y=True, enable_events=True, key="_CHAPTERS_")
    layout.append([list_box])
    return layout

def game_window(game: Game) -> pg.Window:
    layout = []
    manager = GameManager(game)

    layout.append(
        [pg.Text(f"Game name: {manager.game_name()}")])

    layout.append(
        [pg.Text(f"Game skill: {manager.game_skill()}")])

    layout.append(
        [pg.Button("Chapters", enable_events=True, key="_CHAPTER_LIST_")])

    layout.append(
        [pg.Button("Close", enable_events=True, key="_CLOSE_")])


    window = pg.Window("Game", layout=layout, size=(500, 500), resizable=True, finalize=True) 
    return window

def chapter_window(chapters: ChapterPot) -> pg.Window:
    layout = []

    layout.append(
        [pg.Listbox(chapters.items, size=(100, 10), font=('Arial Bold', 14), expand_y=True, enable_events=True, key="_CHAPTERS_")])

    layout.append(
        [pg.Button("Close", enable_events=True, key="_CLOSE_"),
        pg.Button("Levels", enable_events=True, key="_LEVELS_LIST_")])

    window = pg.Window("Chpater", layout=layout, size=(500, 500), resizable=True, finalize=True)
    # return window
    while True:
        event, values = window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            window.close()
            break

        if event == "_LEVELS_LIST_":
            chapter = values["_CHAPTERS_"][0]
            if chapter:
                level_window(chapter.levels)
                continue

def level_window(levels: LevelPot) -> pg.Window:
    layout = []

    layout.append(
        [pg.Listbox(levels.items, size=(100, 10), font=('Arial Bold', 14), expand_y=True, enable_events=True, key="_LEVELS_")])

    layout.append(
        [pg.Button("Close", enable_events=True, key="_CLOSE_"),
        pg.Button("Quests", enable_events=True, key="_QUESTS_LIST_")])

    window = pg.Window("Level", layout=layout, size=(500, 500), resizable=True, finalize=True)
    # return window
    while True:
        event, values = window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            window.close()
            break

        if event == "_QUESTS_LIST_":
            level = values["_LEVELS_"][0]
            if level:
                quest_window(level.quests)
                continue

def quest_window(quests: QuestPot) -> pg.Window:
    layout = []

    layout.append(
        [pg.Listbox(quests.items, size=(100, 10), font=('Arial Bold', 14), expand_y=True, enable_events=True, key="_QUESTS_")])

    layout.append(
        [pg.Button("Close", enable_events=True, key="_CLOSE_")])

    window = pg.Window("Quest", layout=layout, size=(500, 500), resizable=True, finalize=True)
    # return window
    while True:
        event, values = window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            window.close()
            break