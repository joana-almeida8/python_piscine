from ex0.CreatureCard import CreatureCard
from ex3.GameStrategy import GameStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        creatures = [card for card in hand if isinstance(card, CreatureCard)]
        cards_played = [card.name for card in creatures]
        mana_used = sum(card.cost for card in creatures)
        damage_dealt = sum(card.attack for card in creatures)
        return {'cards_played': cards_played, 'mana_used': mana_used,
                'targets_attacked': battlefield, 'damage_dealt': damage_dealt}

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            targets = ["Enemy Player"]
        else:
            targets = list(available_targets)
        return targets
