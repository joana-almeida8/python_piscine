def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda m: m['power'] > min_power, mages)

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))

def mage_stats(mages: list[dict]) -> dict:
    max_p = max(mages, key=lambda m: m['power'])
    min_p = min(mages, key=lambda m: m['power'])
    avg_p = sum([m['power'] for m in mages]) / len(mages)
    return {'max_power': max_p.get('power'),
            'min_power': min_p.get('power'),
            'avg_power': round(avg_p, 2)}

if __name__ == "__main__":
    artifacts = [
        {'name': "Elder Wand", 'power': 92, 'type': "Deathly Hallow"},
        {'name': "Gryffindor's Sword", 'power': 70, 'type': "Founder's Relic"}
    ]

    mages = [
        {'name': "Grindelwald", 'power': 89, 'element': "water"},
        {'name': "Dumbledore", 'power': 91, 'element': "fire"},
        {'name': "Goyle", 'power': 15, 'element': "water"},
        {'name': "Crabbe", 'power': 16, 'element': "water"}
    ]

    spells = [
        "Stupefy", "Arrestum Momentum", "Wingardium Leviosa", "Alohamora",
        "Expulso", "Serpensontia", "Accio", "Expecto Patronum"
    ]

    print("*** Lumos ***")

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    index = 0
    for a in sorted_artifacts:
        if index < (len(sorted_artifacts) - 1):
            i1 = sorted_artifacts[index]
            i2 = sorted_artifacts[index + 1]
            print(f"{i1['name']} ({i1['power']} power) comes before "
              f"{i2['name']} ({i2['power']} power)")
        index += 1

    print("\nTesting power filter...")
    min_power = 30
    sorted_mages = power_filter(mages, min_power)
    print(f"Mages with over {min_power} power:")
    for mage in sorted_mages:
        print(f"- {mage['name']} ({mage['power']})")

    print("\nTesting spell transformer...")
    trans_spells = spell_transformer(spells)
    print("\n".join(spell for spell in trans_spells))

    print("\nTesting mage statistics...")
    stats = mage_stats(mages)
    print(f"Highest power level: {stats['max_power']}")
    print(f"Lowest power level: {stats['min_power']}")
    print(f"Average power level: {stats['avg_power']}")

    print("\n*** Nox ***")
