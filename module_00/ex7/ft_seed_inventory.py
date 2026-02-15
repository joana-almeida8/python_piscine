def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    validUnits = ["packets", "grams", "area"]
    if unit in validUnits:
        if (unit == "packets"):
            print(f"{seed_type.capitalize()} seeds: "
                  f"{quantity} {unit} available")
        elif unit == "grams":
            print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
        elif unit == "area":
            print(f"{seed_type.capitalize()} seeds: "
                  f"covers {quantity} square meters")
    else:
        print("Unknown unit type")
