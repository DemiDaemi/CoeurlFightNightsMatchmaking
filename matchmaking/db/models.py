from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy.orm as orm

Base = orm.declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discord_account_id = Column(String)
    ffxiv_character_id = Column(String)
    world = Column(String)
    rating = Column(Float)

    matches = relationship("Match", back_populates="players")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey("players.id"))
    player2_id = Column(Integer, ForeignKey("players.id"))
    player1_score = Column(Integer)
    player2_score = Column(Integer)
    rounds = Column(Integer)
    match_winner_id = Column(Integer, ForeignKey("players.id"))
    timestamp = Column(DateTime)

    player1 = relationship("Player", foreign_keys=[player1_id])
    player2 = relationship("Player", foreign_keys=[player2_id])
    match_winner = relationship("Player", foreign_keys=[match_winner_id])


class Verification(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True)
    discord_account_id = Column(String)
    character_id = Column(String)
    verification_code = Column(String)
