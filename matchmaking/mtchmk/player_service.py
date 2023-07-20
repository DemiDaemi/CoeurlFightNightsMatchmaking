import asyncio
import logging
import uuid
from matchmaking.mtchmk.player import Player, Verification
from matchmaking.db.dbsession import DBSession

from matchmaking.api.xiv_api import (
    fetch_character_by_id,
    fetch_character_by_name,
    fetch_bio_by_lodestone_id,
)


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
            print(f"An error occurred while adding a new player: {e}")
        else:
            print(f"Added new player: {new_player}")


def generate_verification_code():
    # Generate a verification code for the character
    return f"fighter-{uuid.uuid4()}"


async def start_verification(character_id):
    # Start the verification process for the character
    character = await fetch_character_by_id(character_id)
    if character != None:
        verif_code = generate_verification_code()
        with DBSession() as session:
            new_verification = Verification(
                character_id=character_id, verification_code=verif_code
            )
            session.add(new_verification)

            try:
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"An error occurred when starting verification process: {e}")
            else:
                print(f"Started verification process for {character_id}")
                print(f"Verification code: {verif_code}")
                return verif_code


async def verify_code_from_bio(character_id):
    # Fetch the character and code from the DB
    with DBSession() as session:
        verification = (
            session.query(Verification).filter_by(character_id=character_id).first()
        )
        if verification != None:
            verif_code = verification.verification_code
            bio = await fetch_bio_by_lodestone_id(character_id)
            if bio != None:
                # Check if the verification code is somewhere in the character bio
                if bio.find(verif_code) != -1:
                    character = await fetch_character_by_id(character_id)
                    await add_new_player(
                        name=character["Character"]["Name"],
                        discord_account_id=None,
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s", datefmt="%H:%M")
    loop = asyncio.get_event_loop()
    # verif_code = loop.run_until_complete(start_verification(38151114))

    # print(verif_code)
    loop.run_until_complete(verify_code_from_bio(38151114))
    # toon = loop.run_until_complete(fetch_character_by_name("Demi", "Daemi", "Ultros"))
    # print(toon)
    # character = loop.run_until_complete(fetch_character_by_id(38151114))
    # print(character)


# async def verify_character(character_id, verification_code, discord_account_id):
#     api = XIVAPI()
#     char_data = api.get_character_data(character_id)
#     if char_data != None:
#         char_name = char_data["Character"]["Name"]
#         char_world = char_data["Character"]["Server"]

#         with DBSession() as session:
#             # Check if the character is already registered
#             player = (
#                 session.query(Player).filter_by(ffxiv_character_id=character_id).first()
#             )
#             if player != None:
#                 print(f"Character {character_id} is already registered.")
#                 return False

#             # Check if the verification code matches the one in the character data
#             verification = (
#                 session.query(Verification).filter_by(character_id=character_id).first()
#             )
#             if verification != None:
#                 if verification.verification_code == verification_code:
#                     # Verification successful, add the player to the database
#                     add_new_player(
#                         name=char_name,
#                         discord_account_id=discord_account_id,
#                         ffxiv_character_id=character_id,
#                         world=char_world,
#                     )

#                     try:
#                         session.commit()
#                     except Exception as e:
#                         session.rollback()
#                         print(f"An error occurred when verifying character: {e}")
#                     else:
#                         print(f"Verified character {character_id}")
#                         return True
#                 else:
#                     print("Verification code does not match.")
#                     return False
#             else:
#                 print("Verification code not found.")
#                 return False
#     # TODO: Check if the generated verification code matches the one in the character data
