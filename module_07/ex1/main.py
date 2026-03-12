from .Deck import Deck
from .Deck import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck = Deck()
    cc_fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    sc_lightning_bolt = SpellCard("Lightning Bolt", 3, "Common",
                                  "Deal 3 damage to target")
    ac_mana_crystal = ArtifactCard("Mana Crystal", 2, "Rare", 5,
                                   "Permanent: +1 mana per turn")
    deck.add_card(cc_fire_dragon)
    deck.add_card(sc_lightning_bolt)
    deck.add_card(ac_mana_crystal)
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    deck.shuffle()
    card = deck.draw_card()
    print(f"\nDrew: {card.name} ({card.type})")
    print(f"Play result: {card.play({})}")

    deck.shuffle()
    card = deck.draw_card()
    print(f"\nDrew: {card.name} ({card.type})")
    print(f"Play result: {card.play({})}")

    deck.shuffle()
    card = deck.draw_card()
    print(f"\nDrew: {card.name} ({card.type})")
    print(f"Play result: {card.play({})}")

    print("\nPolymorphism in action: "
          "Same interface, different card behaviours!")
