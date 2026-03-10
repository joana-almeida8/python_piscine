from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from random import random


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
        ...

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        for card in self.deck:
            creatures = sum(isinstance(card, CreatureCard))
            for key, value in card():
                
                
        stats = {'total_cards': {len(self.deck)}, 'creatures': 1,
                 'spells': 1, 'artifacts': 1, 'avg_cost': 4.0}
        return stats
