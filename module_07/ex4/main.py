from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    fire_dragon = TournamentCard(name="Fire Dragon", cost=5,
                                 rarity="Legendary", combat_type="flying",
                                 attack_damage=5, defense=2,
                                 card_id="dragon_001", rating=1200, health=6)
    ice_wizard = TournamentCard(name="Ice Wizard", cost=3, rarity="Rare",
                                combat_type="mage", attack_damage=3, defense=2,
                                card_id="wizard_001", rating=1150, health=10)

    print(f"{platform.register_card(fire_dragon)}")
    print(f"\n{platform.register_card(ice_wizard)}")

    print("\nCreating tournament match...")
    print(f"Match Result: {platform.create_match('dragon_001', 'wizard_001')}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for rank, card in enumerate(leaderboard, 1):
        stats = card.get_tournament_stats()
        print(f"{rank}. {stats['name']} - Rating: "
              f"{stats['rating']} ({stats['score']})")

    print("\nPlatform Report:")
    print(f"{platform.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
