import asyncio
from discord.ext import commands
from matchmaking.mtchmk.player_service import (
    start_verification,
    verify_code_from_discord,
    discord_id_registered,
    discord_id_verifying,
    obtain_character_id_from_name,
)


class Verification(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def register(self, ctx: commands.Context):
        # Discord ID Checks
        discord_id = ctx.message.author.id

        if discord_id_registered(discord_id):
            await ctx.send(
                "A character has already been linked to this discord account. Please contact an admin if you believe this is an error!"
            )
            return

        if discord_id_verifying(discord_id):
            await ctx.send(
                "A verification process is already in progress for this discord account. Please contact an admin if you're having issues!"
            )
            return

        # Command checks
        try:
            surname = ctx.message.content.split(" ")[1]
            lastname = ctx.message.content.split(" ")[2]
            world = ctx.message.content.split(" ")[3]
        except IndexError:
            await ctx.send(
                "Command usage: !register John Finalfantasy Coeurl\n"
                + "Please make sure you include the character's first name, last name, and world."
            )
            return

        # Character checks
        character_id = await obtain_character_id_from_name(surname, lastname, world)
        if character_id == None:
            await ctx.send(
                "Could not find a character with that name on that world.\n"
                + "Command usage: !register John Finalfantasy Coeurl"
            )
            return

        # Start verification process
        verif_code = await start_verification(character_id, discord_id)
        if verif_code != None:
            await ctx.send(
                f"{surname} {lastname} on {world}, \n"
                + f"Please add the following code to your "
                + f"character's profile on the lodestone: \n"
                + f"```{verif_code}```\n"
                + f"Then, please submit `!verify` in this channel when you are done."
            )
        else:
            await ctx.send(
                "An unknown error occurred when starting the verification process."
                + "\nPlease contact an admin, we will be happy to help!"
            )

    @commands.command()
    async def verify(self, ctx: commands.Context):
        discord_id = ctx.message.author.id
        if not discord_id_verifying(discord_id):
            await ctx.send(
                "No verification process for this discord account."
                + "\nPlease register first using `!register Firstname Lastname World`"
            )
            return

        if discord_id_registered(discord_id):
            await ctx.send(
                "A character has already been linked to this discord account.\n"
                + "Please contact an admin if you believe this is an error!"
            )
            return

        if await verify_code_from_discord(discord_id):
            await ctx.send(
                "Verification successful!\n" + "Enjoy your stay at Coeurl Fight Nights!"
            )
        else:
            await ctx.send(
                "Verification failed.\n"
                + "Please make sure you have added the code to your lodestone profile."
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Verification(bot))
