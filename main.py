from pathlib import Path
import PySimpleGUI as pg

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.managers import GameManager
from progature.gui import init_layout, game_window, chapter_window, level_window, quest_window

if __name__ == "__main__":
    game_name = "py_game.json"
    py_game_path = Path("progature/games") / game_name
    game = GameLoader.load(py_game_path)
    manager = GameManager(game)

    main_window = game_window(game)

    while True:
        window, event, values = pg.read_all_windows()

        if event == pg.WIN_CLOSED:
            if window.Title == "Game":
                break
            window.close()
            continue

        if event == "_CLOSE_":
            window.close()
            continue

        if event == "_CHAPTER_LIST_":
            chapter_window = chapter_window(manager.chapters())
            continue

        if event == "_CHAPTERS_":
            chapter = values["_CHAPTERS_"][0]
            if chapter:
                level_window = level_window(chapter.levels)

        if event == "_LEVELS_":
            level = values["_LEVELS_"][0]
            if level:
                quest_window = quest_window(level.quests)

    main_window.close()