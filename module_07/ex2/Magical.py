from ex0.Card import Card
from abc import abstractmethod


class Magical(Card):
    def __init__(self, mana: int, mana_cost: int, spell_damage: int, **kwargs):
        super().__init__(**kwargs)
        self.mana = mana
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
