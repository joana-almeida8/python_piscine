class Plant:
    '''Represents a single plant in a garden and its attributes'''
    def __init__(self, name: str, height: int, age: int) -> None:
        '''Initializes a new Plant with its attributes'''
        self.name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        '''Check if height is negative to prevent data corruption'''
        if height < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {self.height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            return self._height

    def set_age(self, age: int) -> None:
        '''Check if new age is negative to prevent data corruption'''
        if age < 0:
            print(f"\nInvalid operation attempted: "
                  f"age {self.age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            return self._age

    def __str__(self, plant_type: str) -> str:
        '''Print a formatted string describing the Plant's
        current attributes'''
        return (f"{self.name} ({plant_type}): "
                f"{self._height}cm, {self._age} days")


class Flower(Plant):
    '''Represents a single Flower and inherits Plant attributes'''

    def __init__(self, name: str, height: int, age: int, colour: str) -> None:
        '''Initializes a new Flower with
        inherited Plant attributes and its own'''
        super().__init__(name, height, age)
        self.__colour = "None"
        self.set_colour(colour)

    def set_colour(self, colour: str) -> None:
        '''Checks if colour exists to prevent data corruption'''
        if colour is not None:
            self.__colour = colour
            return self.__colour
        elif colour is None:
            print(f"Invalid operation attempted: "
                  f"colour {self.__colour} [REJECTED]")

    def bloom(self) -> None:
        '''Flowers bloom beautifully'''
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        '''Print a formatted string describing
        the Flower's current attributes'''
        return f"{super().__str__('Flower')}, {self.__colour} colour"


class Tree(Plant):
    '''Represents a single Tree and inherits Plant attributes'''
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        '''Initializes a new Tree with
        inherited Plant attributes and its own'''
        super().__init__(name, height, age)
        self.__trunk_diameter = 0
        self.set_diameter(trunk_diameter)

    def set_diameter(self, trunk_diameter: int) -> None:
        '''Checks if trunk_diameter is bigger than 0
        to prevent data corruption'''
        if trunk_diameter > 0:
            self.__trunk_diameter = trunk_diameter
            return self.__trunk_diameter
        else:
            print(f"Invalid operation attempted: "
                  f"trunk_diameter {self.trunk_diameter} [REJECTED]")

    def produce_shade(self) -> None:
        '''Checks if shade is bigger than 0 to
        prevent data corruption and prints it'''
        shade = (self._height * self.__trunk_diameter * 3.14) / 1000
        print(f"{self.name} provides {shade:.0f} "
              f"square meters of shade")

    def __str__(self) -> str:
        '''Print a formatted string describing
        the Tree's current attributes'''
        return (f"{super().__str__('Tree')}, "
                f"{self.__trunk_diameter}cm diameter")


class Vegetable(Plant):
    '''Represents a single Vegetable and inherits Plant attributes'''
    def __init__(self, name: str, height: int, age: int,
                 harvest: str, nutritional_value: str) -> None:
        '''Initializes a new Vegetable with
        inherited Plant attributes and its own'''
        super().__init__(name, height, age)
        self.__harvest = "None"
        self.__nutritional_value = "None"
        self.set_harvest(harvest)
        self.set_nutrivalue(nutritional_value)

    def set_harvest(self, harvest: str) -> None:
        '''Checks if colour exists to prevent data corruption'''
        if harvest is not None:
            self.__harvest = harvest
            return self.__harvest
        else:
            print(f"Invalid operation attempted: "
                  f"harvest {harvest} [REJECTED]")

    def set_nutrivalue(self, nutritional_value: int) -> None:
        '''Gets nutritional_value of the vegetable'''
        if nutritional_value is not None:
            self.__nutritional_value = nutritional_value
            return self.__nutritional_value
        else:
            print(f"Invalid operation attempted: "
                  f"nutritional_value {nutritional_value} [REJECTED]")

    def get_nutrivalue(self) -> None:
        '''Get nutritional vale of the vegetable'''
        print(f"{self.name} is rich in {self.__nutritional_value}")

    def __str__(self) -> str:
        '''Print a formatted string describing
        the Vegetable's current attributes'''
        return f"{super().__str__('Vegetable')}, {self.__harvest} harvest"


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 40, 60, "yellow")
    oak = Tree("Oak", 500, 185, 50)
    pine = Tree("Pine", 700, 2000, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 22, 40, "fall", "vitamin A")

    print("=== Garden Plant Types ===\n")
    print(rose)
    rose.bloom()
    print()
    print(sunflower)
    sunflower.bloom()
    print()
    print(oak)
    oak.produce_shade()
    print()
    print(pine)
    pine.produce_shade()
    print()
    print(tomato)
    tomato.get_nutrivalue()
    print()
    print(carrot)
    carrot.get_nutrivalue()
