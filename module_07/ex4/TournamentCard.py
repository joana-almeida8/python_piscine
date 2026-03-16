from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Combatable, Rankable):
    def __init__(self, card_id, rating, **kwargs):
        super().__init__(**kwargs)
        self.card_id = card_id
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.record = "0-0"

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack(self, target) -> dict:
        target = target
        damage = self.attack_damage
        return {"damage_dealt": damage}

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.defense
        self.health -= damage_taken
        return {"damage_taken": damage_taken}

    def calculate_rating(self) -> int:
        ...

    def get_tournament_stats(self) -> dict:
        ...

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.record = f"{self.wins}-{self.losses}"

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.record = f"{self.wins}-{self.losses}"

    def get_rank_info(self) -> dict:
        ...
