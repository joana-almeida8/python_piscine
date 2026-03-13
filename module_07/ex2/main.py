from ex1.Deck import Deck
from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    print("\nDataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    ec_arcane_warrior = EliteCard(name="Arcane Warrior", cost=11,
                                  rarity="Elite", combat_type="melee",
                                  attack_damage=5, defense=3, mana = 4,
                                  mana_cost=4, spell_damage=3, health=9)
    ec_enemy = EliteCard(name="Enemy", cost=6,
                                  rarity="Rare", combat_type="melee",
                                  attack_damage=2, defense=6, mana = 4,
                                  mana_cost=6, spell_damage=6, health=6)
    ec_enemy1 = EliteCard(name="Enemy1", cost=1,
                          rarity="Common", combat_type="melee",
                          attack_damage=5, defense=7, mana = 4,
                          mana_cost=4, spell_damage=3, health=9)
    ec_enemy2 = EliteCard(name="Enemy2", cost=1,
                          rarity="Common", combat_type="melee",
                          attack_damage=5, defense=7, mana = 4,
                          mana_cost=4, spell_damage=3, health=9)
    Deck().add_card(ec_arcane_warrior)
    Deck().add_card(ec_enemy)
    Deck().add_card(ec_enemy1)
    Deck().add_card(ec_enemy2)

    print("\nCombat phase:")
    attack_res = ec_arcane_warrior.attack(ec_enemy)
    print(f"Attack result: {attack_res}")
    defend_res = ec_arcane_warrior.defend(5)
    print(f"Defense result: {defend_res}")

    print("\nMagic phase:")
    cast_spell = ec_arcane_warrior.cast_spell("Fireball", ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {cast_spell}")
    print(f"Mana channel: {ec_arcane_warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
