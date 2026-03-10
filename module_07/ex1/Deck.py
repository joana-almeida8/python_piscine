from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import random
from typing import Dict, List


class Deck:
    def __init__(self) -> None:
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            for key, value in card():
                if key['name'] == card_name:
                    self.deck.remove(card)
                    return True
        if not card_name in self.deck:
            return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if not self.deck:
            raise ValueError("The deck is empty.")
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = sum(isinstance(card, CreatureCard) for card in self.deck)
        spells = sum(isinstance(card, SpellCard) for card in self.deck)
        artifacts = sum(isinstance(card, ArtifactCard) for card in self.deck)
        total_cost = sum(card.cost for card in self.deck)
        avg_cost = total_cost / len(self.deck) if len(self.deck) > 0 else 0.0
        stats = {'total_cards': len(self.deck), 'creatures': creatures,
                 'spells': spells, 'artifacts': artifacts,
                 'avg_cost': avg_cost}
        return stats
