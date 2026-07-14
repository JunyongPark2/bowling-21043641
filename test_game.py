from game import Game


def roll_many(game, count, pins):
    for _ in range(count):
        game.roll(pins)


def test_gutter_game_scores_zero():
    game = Game()
    roll_many(game, 20, 0)
    assert game.score() == 0


def test_spare_adds_next_roll_as_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)   # spare
    game.roll(3)
    roll_many(game, 17, 0)
    assert game.score() == 16


def test_strike_adds_next_two_rolls_as_bonus():
    game = Game()
    game.roll(10)  # strike
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)
    assert game.score() == 24


def test_perfect_game_scores_300():
    game = Game()
    roll_many(game, 12, 10)
    assert game.score() == 300


def test_tenth_frame_spare_with_fill_ball():
    game = Game()
    roll_many(game, 18, 0)
    game.roll(5)
    game.roll(5)
    game.roll(3)
    assert game.score() == 13


def test_tenth_frame_strike_with_two_fill_balls():
    game = Game()
    roll_many(game, 18, 0)
    game.roll(10)
    game.roll(4)
    game.roll(5)
    assert game.score() == 19
