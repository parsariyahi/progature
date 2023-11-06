from pathlib import Path
import PySimpleGUI as pg

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.game.handler import GameHandler
from progature.engine.core.managers import GameManager
from progature.gui import init_layout, game_window, chapter_window, level_window, quest_window

if __name__ == "__main__":
    game_name = "test_game.json"
    test_game_path = Path("progature/games") / game_name
    manager = GameManager(test_game_path.absolute())

    maanger, main_window = game_window(manager)

    while True:
        event, values = main_window.read(timeout=10000)

        if event == pg.WIN_CLOSED or event == "_CLOSE_":
            break

        if event == "_GAME_COMPLETE_":
            manager.game_complete()

        if event == "_CHAPTER_LIST_":
            chapter_window(manager)
            continue

    main_window.close()