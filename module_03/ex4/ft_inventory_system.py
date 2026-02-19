import sys


def parse_input() -> dict:
    '''Parse input to create the inventory dict'''
    inventory = {}
    for arg in sys.argv[1:]:
        if ":" in arg:
            key, val = arg.split(":", 1)
            inventory[key] = int(val)
    return inventory


def inventory_statistics(inventory: dict) -> str:
    '''Return the most and least abundant item on the inventory'''
    item_keys = list(inventory.keys())
    first_item = item_keys[0]
    most_val = least_val = inventory[first_item]
    most_item = least_item = first_item
    for key, val in inventory.items():
        if val > most_val:
            most_val = val
            most_item = key
        if val < least_val:
            least_val = val
            least_item = key
    units_most = units_least = "units"
    if most_val == 1:
        units_most = "unit"
    if least_val == 1:
        units_least = "unit"
    return (f"Most abundant: {most_item} ({most_val} {units_most})\n"
            f"Least abundant: {least_item} ({least_val} {units_least})")


def item_cats(inventory: dict) -> None:
    '''Print groups of items per quantity in the inventory'''
    abund_items = {}
    mod_items = {}
    scarce_items = {}
    for key, val in inventory.items():
        if val >= 10:
            abund_items[key] = int(val)
        elif val >= 5:
            mod_items[key] = int(val)
        elif val > 0:
            scarce_items[key] = int(val)
    if abund_items:
        print(f"Abundant: {abund_items}")
    if mod_items:
        print(f"Moderate: {mod_items}")
    if scarce_items:
        print(f"Scarce: {scarce_items}")


def restock_needed(inventory: dict) -> None:
    '''Return restock suggestions based on item quantities'''
    restock = []
    for key, val in inventory.items():
        if val == 1:
            restock.append(key)
    if restock:
        return (f"Restock needed: {restock}")
    else:
        return ("No items need to be restocked.")


def dict_properties(inventory: dict) -> None:
    '''Return dictionary/inventory properties'''
    keys = ", ".join(inventory.keys())
    values = ", ".join(str(val) for val in inventory.values())
    return (f"Dictionary keys: {keys}\n"
            f"Dictionary values: {values}\n"
            f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    inventory = parse_input()

    print("=== Inventory System Analysis ===")
    total = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory.keys())}")

    print("\n=== Current Inventory ===")
    for key, val in inventory.items():
        print(f"{key}: {val} units ({((val * 100) / total):.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(f"{inventory_statistics(inventory)}")

    print("\n=== Item Categories ===")
    item_cats(inventory)

    print("\n=== Management Suggestions ===")
    print(restock_needed(inventory))

    print("\n=== Dictionary Properties Demo ===")
    print(dict_properties(inventory))
