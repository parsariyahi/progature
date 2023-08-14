from progature.engine.components.quest import Quest


def test_create_quest():
    quest = Quest("quest1")

    assert quest.name == "quest1"

def test_complete_a_quest():
    #TODO use a create quest util
    quest = Quest("quest1")
    quest.is_complete = True

    assert quest.name == "quest1"
    assert quest.is_complete is True