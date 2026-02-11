def ft_garden_intro(name: str, height: int, age: int) -> None:
    '''
    Prints the header, a specific plant's attributes,
    and the closing text.

    Attributes:
        name (str): the name of the plant
        height (int): the height of the plant in cm
        age (int): the age of the plant in days
    '''
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    name: str = "Rose"
    height: int = 25
    age: int = 30
    ft_garden_intro(name, height, age)
