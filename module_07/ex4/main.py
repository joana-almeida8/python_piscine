from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    tournament = TournamentCard()
    fire_dragon = tournament("Fire Dragon", 5, "Legendary", 5, 2,
                             "dragon_001", 1200)
    ice_wizard = tournament("Ice Wizard", 3, "Rare", 3, 2,
                            "wizard_001", 1150)

    print(f"{platform.register_card(fire_dragon)}")
    print(f"{platform.register_card(ice_wizard)}")

    print("\nCreating tournament match...")
    print(f"Match Result: {platform.create_match("dragon_001", "wizard_001")}")
