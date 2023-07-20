from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    player1_score = Column(Integer)
    player2_score = Column(Integer)
    rounds = Column(Integer)
    match_winner_id = Column(Integer)
    timestamp = Column(DateTime)

    def __repr__(self) -> str:
        return f"{self.player1_id} vs {self.player2_id}: ({self.player1_score} - {self.player2_score})"

    def set_results(self, round_winner_id: int):
        if round_winner_id == self.player1_id:
            self.player1_score += 1
        elif round_winner_id == self.player2_id:
            self.player2_score += 1
        else:
            raise ValueError("Winner must be one of the players in the match")

        if self.player1_score > self.rounds / 2 or self.player2_score > self.rounds / 2:
            self.match_winner_id = (
                self.player1_id
                if self.player1_score > self.player2_score
                else self.player2_id
            )
