from progature.engine.components.quest import Quest


def test_create_quest():
    quest = Quest("quest1")

    assert quest.name == "quest1"