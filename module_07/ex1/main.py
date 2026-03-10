from ex0.Card import Card
from .Deck import Deck
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {Deck().get_deck_stats()}")

    print("\nDrawing and playing cards:\n")

    print(f"Drew: {Deck().draw_card()}")
