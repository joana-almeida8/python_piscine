# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/02 12:25:30 by joana             #+#    #+#              #
#    Updated: 2026/02/02 13:59:09 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 265)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    print(rose)
    print(oak)
    print(cactus)
    print(sunflower)
    print(fern)
    print("\nTotal plants created: 5")