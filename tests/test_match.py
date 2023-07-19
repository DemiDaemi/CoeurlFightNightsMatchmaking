import unittest
import mtchmk
from mtchmk.player import Player
from mtchmk.match import Match


class TestMatch(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "discord1", "character1", "world1", 1000)
        self.player2 = Player("Player 2", "discord2", "character2", "world2", 1200)
        self.match = Match(self.player1, self.player2, 3)

    def test_create_match(self):
        match = Match(self.player1, self.player2, 3)

        self.assertEqual(match.player1, self.player1)
        self.assertEqual(match.player2, self.player2)
        self.assertEqual(match.result, (0, 0))
        self.assertEqual(match.rounds, 3)
        self.assertEqual(match.match_winner, None)

    def test_set_results_1(self):
        # Player 1 wins round 1
        self.match.set_results(self.player1)
        self.assertEqual(self.match.result, (1, 0))
        self.assertEqual(self.match.match_winner, None)
        print(self.match)

        # Player 2 wins round 2
        self.match.set_results(self.player2)
        self.assertEqual(self.match.result, (1, 1))
        self.assertEqual(self.match.match_winner, None)

        # Player 1 wins round 3 (and the set)
        self.match.set_results(self.player1)
        self.assertEqual(self.match.result, (2, 1))
        self.assertEqual(self.match.match_winner, self.player1)


if __name__ == "__main__":
    unittest.main()
