from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")
    engine = GameEngine()

    print("\nConfiguring Fantasy Card Game...")
    factory = FantasyCardFactory(engine)
    strategy = AggressiveStrategy()
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    engine.hand = [factory.create_creature("Fire Dragon"),
                   factory.create_creature("Goblin Warrior"),
                   factory.create_spell("Lightning Bolt")]
    hand_formatted = [f"{card.name} ({card.cost})" for card in engine.hand]
    print(f"Hand: {", ".join(hand_formatted)}")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {engine.simulate_turn()}")

    print("\nGame Report:")
    print(f"{engine.get_engine_status()}")

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
