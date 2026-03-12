from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_damage: int, defense_damage: int, mana_cost: int,
                 spell_damage: int, health: int):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, attack_damage, defense_damage)
        Magical.__init__(self, mana_cost, spell_damage)
        self.health = health

    def play(self, game_estate: dict) -> dict:
        ...

    def attack(self, target) -> dict:
        return {'attacker': {self.name}, 'target': {target.name},
                'damage': {self.attack_damage},
                'combat_type': {self.combat_type}}

    def defend(self, incoming_damage: int) -> dict:
        # random calculation with incoming_damage and defense stats will be 3
        damage_blocked = 3
        alive_stats = "True" if self.health > 0 else "False"
        return {'defender': {self.name}, 'damage_taken': {self.defense_damage},
                'damage_blocked': damage_blocked, 'still_alive': {alive_stats}}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        ...

    def channel_mana(self, amount: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...

    def get_magic_stats(self) -> dict:
        ...
