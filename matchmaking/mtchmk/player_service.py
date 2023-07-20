import logging
import uuid
from matchmaking.mtchmk.player import Player, Verification
from matchmaking.db.dbsession import DBSession

from matchmaking.api.xiv_api import (
    fetch_character_by_id,
    fetch_character_by_name,
    fetch_bio_by_lodestone_id,
)

logging.basicConfig(level=logging.INFO, format="%(message)s", datefmt="%H:%M")


async def add_new_player(
    name: str, discord_account_id: str, ffxiv_character_id: str, world: str
):
    with DBSession() as session:
        new_player = Player(
            name=name,
            discord_account_id=discord_account_id,
            ffxiv_character_id=ffxiv_character_id,
            world=world,
        )
        session.add(new_player)

        try:
            session.commit()
        except Exception as e:
            session.rollback()  # Rollback the changes on error
            logging.exception(f"An error occurred while adding a new player: {e}")
        else:
            logging.info(f"Added new player: {new_player}")


def generate_verification_code():
    # Generate a verification code for the character
    return f"fighter-{uuid.uuid4()}"


def discord_id_registered(discord_account_id):
    with DBSession() as session:
        player = (
            session.query(Player)
            .filter_by(discord_account_id=discord_account_id)
            .first()
        )
        if player != None:
            return True
        else:
            return False


def discord_id_verifying(discord_account_id):
    with DBSession() as session:
        player = (
            session.query(Verification)
            .filter_by(discord_account_id=discord_account_id)
            .first()
        )
        if player != None:
            return True
        else:
            return False


async def obtain_character_id_from_name(surname, lastname, world):
    character = await fetch_character_by_name(surname, lastname, world)
    if character != None:
        try:
            character_id = character["Results"][0]["ID"]
            return character_id
        except IndexError:
            return None
    else:
        return None


async def start_verification(character_id, discord_account_id=None):
    # Start the verification process for the character
    character = await fetch_character_by_id(character_id)
    if character != None:
        verif_code = generate_verification_code()
        with DBSession() as session:
            new_verification = Verification(
                character_id=character_id,
                verification_code=verif_code,
                discord_account_id=discord_account_id,
            )
            session.add(new_verification)

            try:
                session.commit()
            except Exception as e:
                session.rollback()
                logging.exception(
                    f"An error occurred when starting verification process: {e}"
                )
            else:
                logging.info(f"Started verification process for {character_id}")
                logging.info(f"Verification code: {verif_code}")
                return verif_code


async def verify_code_from_discord(discord_account_id):
    # Fetch the character and code from the DB
    with DBSession() as session:
        verification = (
            session.query(Verification)
            .filter_by(discord_account_id=discord_account_id)
            .first()
        )
        if verification != None:
            verif_code = verification.verification_code
            character_id = verification.character_id
            bio = await fetch_bio_by_lodestone_id(character_id)
            if bio != None:
                # Check if the verification code is somewhere in the character bio
                if bio.find(verif_code) != -1:
                    character = await fetch_character_by_id(character_id)
                    await add_new_player(
                        name=character["Character"]["Name"],
                        discord_account_id=discord_account_id,
                        ffxiv_character_id=character_id,
                        world=character["Character"]["Server"],
                    )
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
