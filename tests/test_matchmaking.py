import unittest
import mtchmk
from mtchmk.player import Player
from mtchmk.matchmaking import Matchmaking


class TestMatchmaking(unittest.TestCase):
    def setUp(self):
        self.matchmaking = Matchmaking()

    def test_matchmake_close_elo(self):
        player1 = Player("Player 1", "discord1", "character1", "world1", 1300)
        player2 = Player("Player 2", "discord2", "character2", "world2", 1200)
        player3 = Player("Player 3", "discord3", "character3", "world3", 1100)
        players = [player1, player2, player3]

        matches = self.matchmaking.matchmake_close_elo(players, rounds=3)

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].player1.name, player1.name)
        self.assertEqual(matches[0].player2.name, player2.name)


if __name__ == "__main__":
    unittest.main()
