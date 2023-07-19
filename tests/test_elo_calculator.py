import unittest
from src.player import Player
from src.elo_calculator import EloCalculator


class TestEloCalculator(unittest.TestCase):
    def test_calculate_expected_score(self):
        elo_calculator = EloCalculator()

        expected_score_1 = elo_calculator.calculate_expected_score(1000, 1200)
        expected_score_2 = elo_calculator.calculate_expected_score(1200, 1000)

        # Sum of two scores should be 1
        self.assertAlmostEqual(expected_score_1 + expected_score_2, 1.0, places=2)

        # Player with higher elo has higher expected chance to win
        self.assertGreater(expected_score_2, expected_score_1)

    def test_update_ratings(self):
        player1 = Player(
            "John", "john#1234", "Character123", "Coeurl", initial_rating=1000
        )
        player2 = Player(
            "Jane", "jane#5678", "Character456", "Coeurl", initial_rating=1200
        )
        elo_calculator = EloCalculator()

        # Player 1 wins, rating should climb
        elo_calculator.update_ratings(player1, player2)
        self.assertGreater(player1.rating, 1000)

        # Player 2 lost, rating should drop
        self.assertLess(player2.rating, 1200)

        print(f"Player 1 rating: {player1.rating}")
        print(f"Player 2 rating: {player2.rating}")


if __name__ == "__main__":
    unittest.main()
