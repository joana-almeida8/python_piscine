from ex0.Card import Card
from abc import abstractmethod


class Magical(Card):
    def __init__(self, name, cost, rarity, mana_cost, spell_damage):
        super().__init__(name, cost, rarity)
        self.mana_cost = mana_cost
        self.spell_damage = spell_damage

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        pass
