from progature.engine.structures import Pot

class ChapterManager:

    def __init__(self, chapter_pot: Pot):
        self.chapter_pot = chapter_pot
        self.current_chapter_index = 0

    def current_chapter(self) :
        return self.chapter_pot[self.current_chapter_index]

    def next_cahpter(self):
        self.current_chapter_index += 1
        return self.current_chapter()

    def nth_chapter(self, index):
        return self.chapter_pot[index]