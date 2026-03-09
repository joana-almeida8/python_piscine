from .CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"{fire_dragon.get_card_info()}")

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(6)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Regular", 5, 6)
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")
