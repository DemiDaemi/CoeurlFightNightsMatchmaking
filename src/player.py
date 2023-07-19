class Player:
    def __init__(
        self,
        name: str,
        discord_account_id: str,
        ffxiv_character_id: str,
        world: str,
        initial_rating: float = 1000,
    ):
        self.name = name
        self.discord_account = discord_account_id
        self.ffxiv_character = ffxiv_character_id
        self.world = world
        self.rating = initial_rating

    def update_rating(self, new_rating: float):
        self.rating = new_rating

    def __str__(self) -> str:
        return f"Player: {self.name}, World: {self.world}, FFXIV: {self.ffxiv_character}, Rating: {self.rating}"
