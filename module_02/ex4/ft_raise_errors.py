def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    '''Raise ValueErrors'''
    if plant_name is None:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError((f"Error: Water level {water_level} "
                          f"is too low (min 1)"))
    elif water_level > 10:
        raise ValueError((f"Error: Water level {water_level} "
                          f"is too high (max 10)"))
    elif sunlight_hours < 2:
        raise ValueError((f"Error: Sunlight hours {sunlight_hours} "
                          f"is too low (min 2)"))
    elif sunlight_hours > 12:
        raise ValueError((f"Error: Sunlight hours {sunlight_hours} "
                          f"is too high (max 12)"))
    else:
        print(f"Plant '{plant_name}' is healhy!")


def test_plant_checks() -> None:
    '''Print expected output and call all needed methods'''
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 4, 2)
    except ValueError as error:
        print(error)
    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 4, 2)
    except ValueError as error:
        print(error)
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 2)
    except ValueError as error:
        print(error)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 4, 0)
    except ValueError as error:
        print(error)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
