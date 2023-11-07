from progature.engine.structures import Pot

class QuestManager:

    def __init__(self, quest_pot: Pot):
        self.quest_pot = quest_pot
        self.current_quest_index = 0

    def current_quest(self) :
        return self.quest_pot[self.current_quest_index]

    def next_quest(self):
        self.current_quest_index += 1
        return self.current_quest()

    def nth_quest(self, index):
        return self.quest_pot[index]