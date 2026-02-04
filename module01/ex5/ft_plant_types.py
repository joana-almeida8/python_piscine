# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/02 14:22:53 by joana             #+#    #+#              #
#    Updated: 2026/02/03 14:53:17 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    '''Represents a single plant in a garden and its attributes'''
    
    def __init__(self, name: str, height: int, age: int) -> None:
        '''Initializes a new Plant with its attributes'''
        self.name = name
        self.__height = 0
        self.__age = 0
        self.get_height(height)
        self.get_age(age)

    def get_height(self, height: int) -> None:
        '''Check if height is negative to prevent data corruption'''
        if height < 0:
            print(f"\nInvalid operation attempted: height {self.height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            return self.__height
    
    def get_age(self, age: int) -> None:
        '''Check if new age is negative to prevent data corruption'''
        if age < 0:
            print(f"\nInvalid operation attempted: age {self.age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            return self.__age

    def __str__(self, plant_type: str) -> str:
        '''Print a formatted string describing the Plant's current attributes'''
        return f"{self.name} ({plant_type}): {self.__height}cm, {self.__age} days"

class Flower(Plant):
    '''Represents a single Flower and inherits Plant attributes'''
    
    def __init__(self, name: str, height: int, age: int, colour: str) -> None:
        '''Initializes a new Flower with inherited Plant attributes and its own'''
        super().__init__(name, height, age)
        self.__colour = "none"
        self.get_colour(colour)
    
    def get_colour(self, colour: str) -> None:
        '''Checks if colour exists to prevent data corruption'''
        if colour is not None:
            self.__colour = colour
            return self.__colour
        elif colour is None:
            print(f"Invalid operation attempted: colour {self.__colour} [REJECTED]")

    def bloom(self) -> None:
        '''Flowers bloom beautifully'''
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        '''Print a formatted string describing the Flower's current attributes'''
        return f"{super().__str__("Flower")}, {self.__colour} colour"
    
class Tree(Plant):
    '''Represents a single Tree and inherits Plant attributes'''
    
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int, shade: int) -> None:
        '''Initializes a new Tree with inherited Plant attributes and its own'''
        super().__init__(name, height, age)
        self.__trunk_diameter = 0
        self.get_diameter(trunk_diameter)
        self.__shade = 0
        self.produce_shade(shade)

    def get_diameter(self, trunk_diameter: int) -> None:
        '''Checks if trunk_diameter is bigger than 0 to prevent data corruption'''
        if trunk_diameter > 0:
            self.__trunk_diameter = trunk_diameter
            return self.__trunk_diameter
        else:
            print(f"Invalid operation attempted: trunk_diameter {self.trunk_diameter} [REJECTED]")

    def produce_shade(self, shade: int) -> None:
        '''Checks if shade is bigger than 0 to prevent data corruption and prints it'''
        if shade > 0:
            self.__shade = shade
            return self.__shade
        else:
            print(f"Invalid operation attempted: shade {self.shade} [REJECTED]")

    def get_shade(self) -> None:
        '''Get current shade of the tree'''
        print(f"{self.name} provides {self.__shade} square meters of shade")

    def __str__(self) -> str:
        '''Print a formatted string describing the Tree's current attributes'''
        return f"{super().__str__("Tree")}, {self.__trunk_diameter} square meters of shade"

class Vegetable(Plant):
    '''Represents a single Vegetable and inherits Plant attributes'''
    
    def __init__(self, name: str, height: int, age: int, harvest: str, nutritional_value: str) -> None:
        '''Initializes a new Vegetable with inherited Plant attributes and its own'''
        super().__init__(name, height, age)
        self.__harvest = "none"
        self.get_harvest(harvest)
        self.__nutritional_value = "none"
        self.check_nutrivalue(nutritional_value)

    def get_harvest(self, harvest: str) -> None:
        '''Checks if colour exists to prevent data corruption'''
        if harvest is not None:
            self.__harvest = harvest
            return self.__harvest
        else:
            print(f"Invalid operation attempted: harvest {harvest} [REJECTED]")
    
    def check_nutrivalue(self, nutritional_value: int) -> None:
        '''Gets nutritional_value of the vegetable'''
        if nutritional_value is not None:
            self.__nutritional_value = nutritional_value
            return self.__nutritional_value
        else:
            print(f"Invalid operation attempted: nutritional_value {nutritional_value} [REJECTED]")

    def get_nutrivalue(self) -> None:
        '''Get nutritional vale of the vegetable'''
        print(f"{self.name} is rich in {self.__nutritional_value}")
    
    def __str__(self) -> str:
        '''Print a formatted string describing the Vegetable's current attributes'''
        return f"{super().__str__("Vegetable")}, {self.__harvest} harvest"

if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 40, 60, "yellow")
    oak = Tree("Oak", 500, 185, 50, 78)
    pine = Tree("Pine", 700, 2000, 40, 56)
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
    oak.get_shade()
    print()
    print(pine)
    pine.get_shade()
    print()
    print(tomato)
    tomato.get_nutrivalue()
    print()
    print(carrot)
    carrot.get_nutrivalue()