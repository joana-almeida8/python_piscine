def rare_achiev(alice: set, bob: set, charlie: set) -> set:
    '''Return a set of all the rare achievements among all the players'''
    inter_ab = alice.intersection(bob)
    inter_ac = alice.intersection(charlie)
    inter_bc = bob.intersection(charlie)
    common_achiev = inter_ab.union(inter_ac, inter_bc)
    rare = alice.union(bob, charlie).difference(common_achiev)
    return rare


if __name__ == "__main__":
    players = {
        'alice': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'],
        'bob': ['first_kill', 'level_10', 'boss_slayer', 'collector'],
        'charlie': ['level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist']
               }

    alice = set(players['alice'])
    bob = set(players['bob'])
    charlie = set(players['charlie'])

    print("=== Achievement Tracker System ===\n")
    for player_name, achievements in players.items():
        print(f"Player {player_name} achievements: {achievements}")

    print("\n=== Achievement Analytics ===")
    all_unique = set.union(*(set(achiev) for achiev in players.values()))
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    common = set.intersection(*(set(achiev) for achiev in players.values()))
    print(f"\nCommon to all players: {common}")
    rare = rare_achiev(alice, bob, charlie)
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(alice.intersection(bob))}")
    print(f"Bob unique: {bob.difference(alice.intersection(bob))}")
