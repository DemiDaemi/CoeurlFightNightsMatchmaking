import unittest
import mtchmk
from mtchmk.player import Player


class TestPlayer(unittest.TestCase):
    def test_create_player(self):
        player = Player(
            "John", "john#1234", "Character123", "Coeurl", initial_rating=1000
        )

        self.assertEqual(player.name, "John")
        self.assertEqual(player.discord_account, "john#1234")
        self.assertEqual(player.ffxiv_character, "Character123")
        self.assertEqual(player.world, "Coeurl")
        self.assertEqual(player.rating, 1000)

    def test_update_rating(self):
        player = Player(
            "John", "john#1234", "Character123", "Coeurl", initial_rating=1000
        )

        player.update_rating(1200)
        self.assertEqual(player.rating, 1200)

        player.update_rating(1100)
        self.assertEqual(player.rating, 1100)


if __name__ == "__main__":
    unittest.main()
