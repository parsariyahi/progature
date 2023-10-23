from progature.engine.structures.pots import LevelPot

class LevelManager:

    def __init__(self, level_pot: LevelPot):
        self.level_pot = level_pot
        self.current_level_index = 0

    def current_level(self) :
        return self.level_pot[self.current_level_index]

    def next_level(self):
        self.current_level_index += 1
        return self.current_level()

    def nth_level(self, index):
        return self.level_pot[index]