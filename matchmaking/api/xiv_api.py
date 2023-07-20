import asyncio
import logging
import requests

import pyxivapi
from pyxivapi.models import Filter, Sort
from matchmaking.api.config import XIV_API_KEY


async def fetch_character_by_id(lodestone_id: int):
    client = pyxivapi.XIVAPIClient(api_key=XIV_API_KEY)
    character = None
    try:
        character = await client.character_by_id(lodestone_id=lodestone_id)
    except Exception as e:
        logging.error(f"An error occurred when fetching character: {e}")
    finally:
        await client.session.close()
        return character


async def fetch_character_by_name(forename: str, surname: str, world: str):
    client = pyxivapi.XIVAPIClient(api_key=XIV_API_KEY)
    character = None
    try:
        character = await client.character_search(
            forename=forename, surname=surname, world=world
        )
    except Exception as e:
        logging.error(f"An error occurred when fetching character: {e}")
    finally:
        await client.session.close()
        return character


async def fetch_bio_by_lodestone_id(lodestone_id: int):
    # client = pyxivapi.XIVAPIClient(api_key=XIV_API_KEY)
    url = f"https://na.finalfantasyxiv.com/lodestone/character/{lodestone_id}/"
    htmltext = requests.get(url).text
    if htmltext.find("character__selfintroduction") == -1:
        return None
    bio = htmltext[
        htmltext.find("character__selfintroduction")
        + 29 : htmltext.find("character__selfintroduction")
        + 1000
    ]
    bio = bio[: bio.find("</div>")]
    return bio
