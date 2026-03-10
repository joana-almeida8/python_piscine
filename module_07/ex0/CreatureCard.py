from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity:
                 str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = self.type
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def play(self, game_state: dict) -> dict:
        game_state = {'card_played': 'Fire Dragon', 'mana_used': 5,
                      'effect': 'Creature summoned to battlefield'}
        return game_state
    
    def attack_target(self, target: 'CreatureCard') -> dict:
        attack_info = {'attacker': self.name, 'target': target.name,
                      'damage_dealt': self.attack}
        if target.health <= self.attack:
            attack_info['combat_resolved'] = True
        else:
            attack_info['combat_resolved'] = False
        return attack_info
