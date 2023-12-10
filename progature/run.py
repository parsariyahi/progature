import os
import sys
from pathlib import Path
import PySimpleGUI as pg

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from progature.engine.core.game.manager import GameManager
from progature.gui import main_window, game_window, chapter_window, level_window, quest_window

if __name__ == "__main__":

    main_window = main_window()

    while True:
        event, values = main_window.read(timeout=10000)

        if event == "_CLOSE_" or event == pg.WIN_CLOSED:
            main_window.close()
            break

        if event == "_GAME_OPEN_":
            if values["_GAMES_"]:
                game = values["_GAMES_"][0]
                if game:
                    manager = GameManager(game.file_name)
                    game_window(manager)
            else:
                pg.popup_error("Please select a chapter")

            continue

    main_window.close()