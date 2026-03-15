from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self, engine):
        self.valid_creatures = ['dragon', 'goblin']
        self.valid_spells = ['fireball']
        self.valid_artifacts = ['mana_ring']
        self.engine = engine

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            if "Dragon" in name_or_power:
                self.engine.cards_created += 1
                return CreatureCard(name_or_power, 5, "Rare", 7, 5)
            elif "Goblin" in name_or_power:
                self.engine.cards_created += 1
                return CreatureCard(name_or_power, 2, "Regular", 5, 6)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            self.engine.cards_created += 1
            return SpellCard(name_or_power, 3, "Common",
                             "Deal 3 damage to target")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        ...

    def create_themed_deck(self, size: int) -> dict:
        ...

    def get_supported_types(self) -> dict:
        return {'creatures': self.valid_creatures, 'spells': self.valid_spells,
                'artifacts': self.valid_artifacts}
