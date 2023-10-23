from tests.utils.component import LevelUtil

from progature.engine.structures.pots import LevelPot
from progature.engine.components import Level
from progature.engine.core.managers import LevelManager


def test_level_manager_init():
    levels = LevelUtil.create_level_bulk()
    pot = LevelPot(levels)
    manager = LevelManager(pot)

    assert manager.current_level() == pot[0]
    assert manager.next_level() == pot[1]
    assert manager.next_level() == pot[2]
    assert manager.nth_level(4) == pot[4]