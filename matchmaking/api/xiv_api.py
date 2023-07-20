import asyncio
import logging

import pyxivapi
from pyxivapi.models import Filter, Sort
from matchmaking.api.config import XIV_API_KEY

client = pyxivapi.XIVAPIClient(api_key=XIV_API_KEY)


async def fetch_character_by_id(lodestone_id: int):
    character = await client.character_by_id(lodestone_id=lodestone_id)
    # Check if bio contains

    await client.session.close()
    return character


async def fetch_character_by_name(forename: str, surname: str, world: str):
    character = await client.character_search(
        forename=forename, surname=surname, world=world
    )
    await client.session.close()
    return character


async def fetch_bio_by_lodestone_id(lodestone_id: int):
    bio = await client.character_by_id(lodestone_id=lodestone_id)["Character"]["Bio"]
    await client.session.close()
    return bio


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s", datefmt="%H:%M")
    loop = asyncio.get_event_loop()
    character = loop.run_until_complete(fetch_character_by_name("Demi", "Daemi", "asd"))
    print(character)
