import unittest
from src.player import Player
from src.elo_calculator import EloCalculator


class TestEloCalculator(unittest.TestCase):
    def test_calculate_expected_score(self):
        elo_calculator = EloCalculator()

        expected_score_1 = elo_calculator.calculate_expected_score(1000, 1200)
        expected_score_2 = elo_calculator.calculate_expected_score(1200, 1000)

        self.assertAlmostEqual(expected_score_1 + expected_score_2, 1.0, places=2)
        self.assertGreater(
            expected_score_2, expected_score_1
        )  # Player with higher elo has higher expected chance to win

    def test_update_ratings(self):
        player1 = Player(
            "John", "john#1234", "Character123", "Coeurl", initial_rating=1000
        )
        player2 = Player(
            "Jane", "jane#5678", "Character456", "Coeurl", initial_rating=1200
        )
        elo_calculator = EloCalculator()

        # Player 1 wins, rating should climb
        elo_calculator.update_ratings(player1, player2, True)
        self.assertGreater(player1.rating, 1000)

        # Player 2 lost, rating should drop
        self.assertLess(player2.rating, 1200)


if __name__ == "__main__":
    unittest.main()
