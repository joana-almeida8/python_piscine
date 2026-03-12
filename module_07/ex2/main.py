from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    print("\nDataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    ec_arcane_warrior = EliteCard("Arcane Warrior", 11, "Elite", 5, 7, 4, 3, 9)
    cc_enemy = CreatureCard("Enemy", 6, "Rare", 6, 6)
    Deck().add_card(ec_arcane_warrior)
    Deck().add_card(cc_enemy)

    print("\nCombat phase:")
    attack_res = ec_arcane_warrior.attack(cc_enemy)
    print(f"Attack result: {attack_res}")
    defend_res = ec_arcane_warrior.defend(cc_enemy)

    print("\nMagic phase:")
    cast_spell = ec_arcane_warrior.cast_spell("Fireball", ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {cast_spell}")
    print(f"Mana channel: {ec_arcane_warrior.get_magic_stats()}")

    print("Multiple interface implementation successful!")
