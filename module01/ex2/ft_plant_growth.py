# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/01 12:11:04 by joana             #+#    #+#              #
#    Updated: 2026/02/01 12:47:15 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    '''Represents a plant and all its attributes'''
    
    def __init__(self, name: str, height: int, days: int) -> None:
        '''
        Initiates the attributes of each plant

        Attributes:
            name (str): the common name of the plant
            height (int): the height of the plant in centimeters
            age (int): the age of the plant in days
        '''
        self.name = name
        self.height = height
        self.days = days
        
    def grow(self) -> None:
        '''Grow plant 1cm'''
        self.height += 1

    def age(self) -> None:
        '''Age plant by 1 day'''
        self.days += 1

    def get_info(self) -> None:
        '''Prints the attributes of a plant in the Garden'''
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    day = 1
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.get_info()
        if day < 7:
            rose.grow()
            rose.age()
        day += 1
    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")