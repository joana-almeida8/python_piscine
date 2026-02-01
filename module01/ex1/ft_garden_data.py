# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 11:39:46 by joana             #+#    #+#              #
#    Updated: 2026/02/01 12:05:36 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    '''Represents a plant and all its attributes'''
    
    def __init__(self, name: str, height: int, age: int) -> None:
        '''
        Initiates the attributes of each plant

        Attributes:
            name (str): the common name of the plant
            height (int): the height of the plant in centimeters
            age (int): the age of the plant in days
        '''
        self.name = name
        self.height = height
        self.age = age
        
    def __str__(self) -> str:
        '''Prints the attributes of a plant in the Garden'''
        return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(rose)
    print(sunflower)
    print(cactus)