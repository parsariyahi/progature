import PySimpleGUI as pg

from progature.gui import init_layout

if __name__ == "__main__":
    layout = init_layout()
    win = pg.Window("Proature", layout)
    while True:
        event, value = win.read()
        if event in {pg.WINDOW_CLOSED}:
            break

        if event == "_CHAPTERS_":
            chapter = value["_CHAPTERS_"][0]
            print(chapter)

    win.close()