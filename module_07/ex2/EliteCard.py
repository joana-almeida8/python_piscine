from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Combatable, Magical):
    def __init__(self, health: int, **kwargs):
        super().__init__(**kwargs)
        self.health = health

    def play(self, game_estate: dict) -> dict:
        ...

    def attack(self, target) -> dict:
        return {'attacker': self.name, 'target': target.name,
                'damage': self.attack_damage,
                'combat_type': self.combat_type}

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = self.defense
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        alive_stats = "True" if self.health > 0 else "False"
        return {'defender': self.name, 'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': alive_stats}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {'caster': self.name, 'spell': spell_name,
                'targets': targets, 'mana_used': self.mana_cost}

    def channel_mana(self, amount: int) -> dict:
        total = self.mana + amount
        return {'channeled': amount, 'total_mana': total}

    def get_combat_stats(self) -> dict:
        return {'health': self.health, 'mana': self.mana}

    def get_magic_stats(self) -> dict:
        ...
