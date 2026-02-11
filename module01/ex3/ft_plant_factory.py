class Plant:
    '''Represents a single plant in a garden'''
    def __init__(self, name: str, height: int, age: int) -> None:
        '''
        Initializes a new Plant with its the attributes

        Attributes:
            name (str): the common name of the plant
            height (int): the height of the plant in centimeters
            age (int): the age of the plant in days
        '''
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        '''Returns a formatted string describing the plant's current status'''
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    plants = [("Rose", 25, 30), ("Oak", 200, 265),
              ("Cactus", 5, 90), ("Sunflower", 80, 45),
              ("Fern", 15, 120)]
    print("=== Plant Factory Output ===")
    for p in plants:
        print(plants.append(Plant(p)))
    print("\nTotal plants created: 5")
