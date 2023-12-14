from progature.utils.loader import load_all_games

def test_load_all_games(game):
    games_pot = load_all_games()

    assert len(games_pot) == 1
    for g in games_pot:
        assert g == game