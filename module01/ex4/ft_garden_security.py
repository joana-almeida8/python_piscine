# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/02 12:58:55 by joana             #+#    #+#              #
#    Updated: 2026/02/02 14:32:33 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class SecurePlant:
    '''Represents a single plant in a garden and its attributes'''

    def __init__(self, name: str, height: int, age: int) -> None:
        '''Initializes a new Plant with its attributes'''
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)
    
    def get_height(self) -> int:
        '''Return plant's current height'''
        return self.__height

    def get_age(self) -> int:
        '''Return plant's current age'''
        return self.__age
    
    def set_height(self, height: int) -> None:
        '''Check if new height is negative to prevent data corruption'''
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        '''Check if new age is negative to prevent data corruption'''
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def __str__(self) -> str:
        '''Print a formatted string describing the Plant's current attributes'''
        return f"{self.name} ({self.__height}cm, {self.__age} days)"

if __name__ == "__main__":
    print("=== Garden Security System")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose}")