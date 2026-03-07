import alchemy.elements


def healing_potion() -> str:
    return f"Healing potion brewed with {alchemy.elements.create_fire()} \
and {alchemy.elements.create_water()}"

def strength_potion() -> str:
    return f"Healing potion brewed with {alchemy.elements.create_earth()} \
and {alchemy.elements.create_fire()}"
