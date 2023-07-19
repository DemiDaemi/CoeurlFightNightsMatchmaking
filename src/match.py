from datetime import datetime
from src.player import Player


class Match:
    def __init__(self, player1: Player, player2: Player, rounds: int = 3):
        self.player1 = player1
        self.player2 = player2
        self.result = (0, 0)  # (player1 score, player2 score)
        self.rounds = rounds  # "best of X" rounds
        self.match_winner = None  # Player object
        self.timestamp = datetime.now()

    def set_results(self, round_winner: Player):
        if round_winner == self.player1:
            self.result = (self.result[0] + 1, self.result[1])
        elif round_winner == self.player2:
            self.result = (self.result[0], self.result[1] + 1)
        else:
            raise ValueError("Winner must be one of the players in the match")

        if self.result[0] > self.rounds / 2 or self.result[1] > self.rounds / 2:
            self.match_winner = (
                self.player1 if self.result[0] > self.result[1] else self.player2
            )

    def __str__(self) -> str:
        return f"{str(self.player1)} vs {str(self.player2)} - ({self.result[0] - self.result[1]})"
