from typing import List
from player import Player
from match import Match


class Matchmaking:
    def matchmake_close_elo(self, players: List[Player], rounds: int) -> List[Match]:
        # Pair players with closest Elo ratings

        sorted_players = sorted(
            players, key=lambda p: p.rating
        )  # Sort players by rating

        matches = []
        while len(sorted_players) >= 2:
            player1 = sorted_players.pop()
            player2 = sorted_players.pop()
            match = Match(player1, player2, rounds)
            matches.append(match)

        return matches
