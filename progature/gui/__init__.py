from pathlib import Path
import PySimpleGUI as pg

from progature.engine.core.game.loader import GameLoader
from progature.engine.core.managers import GameManager

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