# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 09:31:51 by joana             #+#    #+#              #
#    Updated: 2026/02/06 23:16:35 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    '''Represent the custom exception errors'''
    
    def __init__(self, message: str) -> None:
        '''Initialize the garden error with a specific message'''
        super().__init__(message)
        self.message = message

class PlantError(GardenError):
    '''Represent the plant error which inherits from GardenError'''
    pass

class WaterError(GardenError):
    '''Represent the water error which inherits from GardenError'''
    pass

def plant_error_test() -> None:
    '''Test the PlantError exception and return error message'''
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        return f"Caught PlantError: {error}"

def water_error_test() -> None:
    '''Test the WaterError exception and return error message'''
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        return f"Caught WatterError: {error}"

def garden_errors_test() -> None:
    '''Test all garden errors and print each error message'''
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print (f"Caught a garden error: {error}")

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print (f"Caught a garden error: {error}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    print(plant_error_test())
    print("\nTesting WaterError...")
    print(water_error_test())
    print("\nTesting catching all garden errors...")
    garden_errors_test()
    print("\nAll custom error types work correctly!")