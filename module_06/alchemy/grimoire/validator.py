def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    ings = ingredients.split()
    if ings and all(i in valid_ingredients for i in ings):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
