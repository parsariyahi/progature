from progature.utils.component import (
    create_bulk_chapters,
    create_bulk_levels,
    create_bulk_quest,
    create_skill,
    create_game,
)
from tests.utils.component import (
    QuestUtil,
    LevelUtil,
    ChapterUtil,
    SkillUtil,
)


def test_create_bulk_quests(test_game_json):
    quest_pot = create_bulk_quest(test_game_json["chapters"][0]["levels"][0]["quests"])

    for quest in quest_pot:
        assert quest.name == test_game_json["chapters"][0]["levels"][0]["quests"][quest.index]["name"]

def test_create_bulk_levels(test_game_json):
    level_pot = create_bulk_levels(test_game_json["chapters"][0]["levels"])

    for level in level_pot:
        assert level.index == test_game_json["chapters"][0]["levels"][level.index]["index"]
        assert level.name == test_game_json["chapters"][0]["levels"][level.index]["name"]
        assert level.is_complete == test_game_json["chapters"][0]["levels"][level.index]["is_complete"]

def test_create_bulk_chapters(test_game_json):
    chapter_pot = create_bulk_chapters(test_game_json["chapters"])

    for chapter in chapter_pot:
        assert chapter.index == test_game_json["chapters"][chapter.index]["index"]
        assert chapter.name == test_game_json["chapters"][chapter.index]["name"]
        assert chapter.is_complete == test_game_json["chapters"][chapter.index]["is_complete"]

def test_create_skill(test_game_json):
    skill = create_skill(test_game_json["skill"])

    assert skill.name == test_game_json["skill"]

def test_create_game(test_game_json):
    game_skill = SkillUtil.create_skill()
    chapters = ChapterUtil.create_chapter_bulk(10)

    game = create_game(test_game_json["file_name"], test_game_json["name"], game_skill, chapters)

    assert game.name == test_game_json["name"]
    assert game.file_name == test_game_json["file_name"]
    assert game.skill == game_skill
    assert game.chapters == chapters

def test_create_full_game_with_component_utils(test_game_json):
    skill = create_skill(test_game_json["skill"])
    game = create_game(test_game_json["file_name"],
                       name=test_game_json["name"],
                       skill=skill)

    chapters_json = test_game_json["chapters"]
    chapters = create_bulk_chapters(chapters_json)
    game.chapters = chapters
    for chapter in game.chapters:
        chapter_json = test_game_json["chapters"][chapter.index]
        chapter_levels_json = chapter_json["levels"]
        chapter.levels = create_bulk_levels(chapter_levels_json)

    for chapter in game.chapters:
        for level in chapter.levels:
            level_json = test_game_json["chapters"][chapter.index]["levels"][level.index]
            level_quests_json = level_json["quests"]
            level.quests = create_bulk_quest(level_quests_json)


    assert game.as_dict() == test_game_json

    for chapter in game.chapters:
        assert chapter.index == test_game_json["chapters"][chapter.index]["index"]
        assert chapter.name == test_game_json["chapters"][chapter.index]["name"]
        assert chapter.is_complete == test_game_json["chapters"][chapter.index]["is_complete"]

        for level in chapter.levels:
            assert level.index == test_game_json["chapters"][chapter.index]["levels"][level.index]["index"]
            assert level.name == test_game_json["chapters"][chapter.index]["levels"][level.index]["name"]
            assert level.is_complete == test_game_json["chapters"][chapter.index]["levels"][level.index]["is_complete"]

            for quest in level.quests:
                assert quest.index == test_game_json["chapters"][chapter.index]["levels"][level.index]["quests"][quest.index]["index"]
                assert quest.name == test_game_json["chapters"][chapter.index]["levels"][level.index]["quests"][quest.index]["name"]
                assert quest.is_complete == test_game_json["chapters"][chapter.index]["levels"][level.index]["quests"][quest.index]["is_complete"]