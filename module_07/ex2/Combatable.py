from ex0.Card import Card
from abc import abstractmethod


class Combatable(Card):
    def __init__(self, combat_type: str, attack_damage: int,
                 defense: int, **kwargs):
        super().__init__(**kwargs)
        self.combat_type = combat_type
        self.attack_damage = attack_damage
        self.defense = defense

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
