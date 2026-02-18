import sys


def parse_input() -> dict:
    '''Parse input to create the inventory dict'''
    inventory = {}
    for arg in sys.argv[1:]:
        key_val = arg.split(":")
        if key_val == 2:
            key = key_val[0]
            val = int(key_val[1])
            inventory[key] = val
    return inventory


def inventory_statistics(inventory: dict) -> None:
    '''Return the most and least abundant item on the inventory'''
    most_val = None
    most_item = None
    least_val = None
    least_item = None
    for key, val in inventory.items():
        current_val = val[0]
        if most_val is None or current_val > most_val:
            most_val = current_val
            most_item = key
        else:
            least_val = current_val
            least_item = key
    print(f"Most abundant: {most_item} ({most_val} units)\n"
          f"Least abundant: {least_item} ({least_val} units)")


if __name__ == "__main__":
    inventory = parse_input()

    print("=== Inventory System Analysis ===")
    total = sum(val[0] for val in inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory.keys())}")

    print("\n=== Current Inventory ===")
    for key, val in inventory.items():
        print(f"{key}: {val[0]} units ({((val[0] * 100) / total):.1f}%)")

    print("\n=== Inventory Statistics ===")
    inventory_statistics(inventory)

    # print("\n=== Item Categories ===")
    # item_cats()

    # print("\n=== Management Suggestions ===")
    # print(f"Restock needed: {restock()}")

    print("\n=== Dictonary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory: {inventory.get('sword')}")
