from .player import Player


class EloCalculator:
    def __init__(self, k_factor: float = 32):
        # K_Factor is the maximum amount of rating points a
        # player can gain or lose in a single match
        self.k_factor = k_factor

    def calculate_expected_score(self, w_rating: float, l_rating: float):
        # Expected score is the probability of a player winning
        # based on their rating compared to their opponent's rating
        expected_score = 1 / (1 + 10 ** ((l_rating - w_rating) / 400))
        return expected_score

    def update_ratings(self, w_player: Player, l_player: Player):
        w_score = self.calculate_expected_score(w_player.rating, l_player.rating)
        l_score = self.calculate_expected_score(l_player.rating, w_player.rating)

        # Calculate rating change using k-factor
        w_rating_change = self.k_factor * (1 - w_score)
        l_rating_change = self.k_factor * (0 - l_score)

        w_player.update_rating(w_player.rating + w_rating_change)
        l_player.update_rating(l_player.rating + l_rating_change)
