import math


def parse(coord: str) -> None:
    '''Parse str to int tuples'''
    try:
        coord_tup = coord.split(",")
        print(f"Parsing coordinates: {coord}")
        print(f"Parsed position: {coord_tup}")
        if not coord_tup:
            raise ValueError("invalid literal for int() "
                             f"with base 10: '{coord[0]}'")
    except ValueError as error:
        print(f"Parsing invalid coordinates: {coord}")
        print(f"Error parsing coordinates: {error}")
        print(f'Error details - Type: {type(error)}, Args: ("{error}")')


def distance(coord_a: tuple[int], coord_b: tuple[int]) -> float:
    '''Calc distance between two coordenates'''
    x1 = coord_a[0], y1 = coord_a[1], z1 = coord_a[2]
    x2 = coord_b[0], y2 = coord_b[1], z2 = coord_b[2]
    calc = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return calc


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    spawn = (0, 0, 0)
    coord1 = (10, 20, 5)
    raw_coord2 = "3,4,0"
    invalid = "abc,def,ghi"
    coords = (spawn, coord1, raw_coord2, invalid)
    for xyz in coords:
        if not isinstance(xyz, tuple):
            parse(xyz)
        else:
            print(f"Position created: {xyz}")




    # coord2 = raw_coord2.split(",")
    # print(f"Position created: {coord1}")
    # print(f"Distance between {spawn} and {coord1}: {distance(spawn, coord1)}")
    # print(f"\nParsing coordinates: {raw_coord2}")
    # print(f"Parsed position: {coord2}")
    # print(f"Distance between {spawn} and {coord2}: {distance(spawn, coord2)}")
    # print(f"\nParsing invalid coordinates: {invalid}")
    
    # print(f"Error parsing coordinates: invalid literal for ")
