from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    discord_account_id = Column(String)
    ffxiv_character_id = Column(String)
    world = Column(String)
    rating = Column(Float, default=1000.0)

    # matches = relationship("Match", back_populates="players")

    def update_rating(self, new_rating: float):
        self.rating = new_rating

    def __repr__(self) -> str:
        return f"{self.name} - {self.world} ({self.rating})"


class Verification(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True)
    character_id = Column(String)
    verification_code = Column(String)
