# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/07 23:40:26 by joana             #+#    #+#              #
#    Updated: 2026/02/08 00:13:29 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenWateringError(Exception):
    '''Represent the garden error of the watering system'''
    
    def __init__(self, message: str) -> None:
        '''Initialize the watering error with a specific message'''
        super().__init__(message)
        self.message = message

def water_plants(plant_list: str) -> None:
    '''Print watering message for every plant on the list'''
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise GardenWateringError(f"Error: Cannot water {plant} "
                                            f"- invalid plant!")
            print(f"Watering {plant}")
    except GardenWateringError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")
    
def test_watering_system() -> None:
    '''Test watering system with good_list and error_list'''
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    good_list = ["toamto", "lettuce", "carrors"]
    water_plants(good_list)
    print("Watering completed sucessfully!")
    print("\nTesting with error...")
    error_list = ["tomato", None]
    water_plants(error_list)
    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()