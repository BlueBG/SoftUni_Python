from typing import List

from project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if self.name == player.guild:
            return f"Player {player.name} is already in guild"
        elif self.name != player.guild and self.name != "Unaffiliated":
            return f"Player {player.name} is already in another guild"

        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"




player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
# print(guild.guild_info())