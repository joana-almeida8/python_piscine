import math


def parse(coord: str) -> None:
    '''Parse str to int tuples'''
    try:
        coord_parts = coord.split(",")
        coord_tup = tuple(int(p.strip()) for p in coord_parts)
        print(f'\nParsing coordinates: "{coord}"')
        print(f"Parsed position: {coord_tup}")
        return coord_tup
    except ValueError:
        first_bad = coord.split(",")[0]
        error = f"invalid literal for int() with base 10: '{first_bad}'"
        print(f'\nParsing invalid coordinates: "{coord}"')
        print(f"Error parsing coordinates: {error}")
        print(f'Error details - Type: {type(error).__name__}, '
              f'Args: ("{error}")')


def distance(coord_a: tuple[int], coord_b: tuple[int]) -> float:
    '''Calc distance between two coordenates'''
    x1, y1, z1 = coord_a
    x2, y2, z2 = coord_b
    calc = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return (calc)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    spawn = (0, 0, 0)
    coord1 = (10, 20, 5)
    raw_coord2 = "3,4,0"
    invalid = "abc,def,ghi"

    print(f"Position created: {coord1}")
    print(f"Distance between {spawn} and {coord1}: "
          f"{distance(spawn, coord1):.2f}")

    coord2 = parse(raw_coord2)
    if coord2:
        print(f"Distance between {spawn} and {coord2}: "
              f"{distance(spawn, coord2)}")
    
    parse(invalid)

    if coord2:
        x, y, z = coord2
        print(f"\nUnpacking demonstration:\nPlayer at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
