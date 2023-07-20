from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from matchmaking.db.models import Base


# Create a new SQLite database
engine = create_engine("sqlite:///ffxiv_pvp.db")

# Create tables for our data models
Base.metadata.create_all(engine)

# Create a sessionmaker bound to the engine
DBSession = sessionmaker(bind=engine)
