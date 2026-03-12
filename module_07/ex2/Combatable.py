from ex0.Card import Card
from abc import abstractmethod


class Combatable(Card):
    def __init__(self, name, cost, rarity, combat_type,
                 attack_damage, defense_damage):
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.attack_damage = attack_damage
        self.defense_damage = defense_damage

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
