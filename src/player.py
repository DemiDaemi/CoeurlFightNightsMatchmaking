class Player:
    def __init__(
        self, name, discord_account_id, ffxiv_character_id, world, initial_rating=1000
    ):
        self.name = name
        self.discord_account = discord_account_id
        self.ffxiv_character = ffxiv_character_id
        self.world = world
        self.rating = initial_rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def __str__(self):
        return f"Player: {self.name}, World: {self.world}, FFXIV: {self.ffxiv_character}, Rating: {self.rating}"
