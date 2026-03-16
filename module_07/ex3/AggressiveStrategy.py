import random
from ex3.GameStrategy import GameStrategy
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if len(hand) > 1:
            random.shuffle(hand)
            card1 = hand.pop(0)
            card2 = hand.pop(0)
        cards = [card1, card2]
        cards_played = [card.name for card in cards]
        mana_used = sum(card.cost for card in cards)
        for card in cards:
            if isinstance(card, SpellCard):
                card.attack = card.cost
        damage_dealt = sum(card.attack for card in cards)
        return {'cards_played': cards_played, 'mana_used': mana_used,
                'targets_attacked': battlefield, 'damage_dealt': damage_dealt}

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            targets = ["Enemy Player"]
        else:
            targets = available_targets
        return targets
