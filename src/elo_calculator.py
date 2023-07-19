from src.player import Player


class EloCalculator:
    def __init__(self, k_factor: float = 32):
        # K_Factor is the maximum amount of rating points a
        # player can gain or lose in a single match
        self.k_factor = k_factor

    def calculate_expected_score(self, player_rating: float, opponent_rating: float):
        # Expected score is the probability of a player winning
        # based on their rating compared to their opponent's rating
        expected_score = 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))
        return expected_score

    def update_ratings(self, player: Player, opponent: Player, player_won: bool):
        player_expected_score = self.calculate_expected_score(
            player.rating, opponent.rating
        )
        opponent_expected_score = self.calculate_expected_score(
            opponent.rating, player.rating
        )

        if player_won:
            player_result = 1
            opponent_result = 0
        else:
            player_result = 0
            opponent_result = 1

        # Calculate rating change using k-factor
        player_rating_change = self.k_factor * (player_result - player_expected_score)
        opponent_rating_change = self.k_factor * (
            opponent_result - opponent_expected_score
        )

        player.update_rating(player.rating + player_rating_change)
        opponent.update_rating(opponent.rating + opponent_rating_change)
