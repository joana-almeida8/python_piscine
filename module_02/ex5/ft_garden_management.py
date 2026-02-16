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


class Plant():
    '''Represent a plant in the garden'''
    def __init__(self, name: str, water: int, sun: int) -> None:
        '''Initialize plant and its attributes'''
        self.name = name
        self.water = water
        self.sunlight = sun


class GardenManager():
    '''Represent the garden manager'''
    def __init__(self) -> None:
        '''Initialize the garden manager'''
        self.garden = []
        self.__water_tank = 2

    def add_plants(self, plant: Plant) -> None:
        '''Add a plant to the garden'''
        try:
            if plant.name is None:
                raise PlantError("Error adding plant: "
                                 "Plant name cannot be empty!")
            else:
                self.garden.append(plant)
                print(f"Added {plant.name} sucessfully")
        except PlantError as error:
            print(error)

    def water_plants(self) -> None:
        '''Water all plants'''
        print("Opening watering system")
        try:
            for plant in self.garden:
                if self.__water_tank <= 0:
                    raise WaterError("Not enough water in the tank")
                else:
                    plant.water += 1
                    self.__water_tank -= 1
                    print(f"Watering {plant.name} - success")
        except WaterError as error:
            print(error)
        print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        '''Raise ValueErrors to check all plants' health'''
        try:
            for plant in self.garden:
                if plant.water > 10:
                    raise ValueError((f"Error checking {plant.name}: "
                                      f"Water level {plant.water} "
                                      f"is too high (max 10)"))
                elif plant.water < 1:
                    raise ValueError((f"Error checking {plant.name}: "
                                      f"Water level {plant.water} "
                                      f"is too low (min 1)"))
                elif plant.sunlight > 12:
                    raise ValueError((f"Error checking {plant.name}: "
                                      f"Sunlight hours {plant.sunlight} "
                                      f"is too high (max 12)"))
                elif plant.sunlight < 2:
                    raise ValueError((f"Error checking {plant.name}: "
                                      f"Sunlight hours {plant.sunlight} "
                                      f"is too low (min 2)"))
                else:
                    print(f"{plant.name}: healthy (water: {plant.water}, "
                          f"sun: {plant.sunlight})")
        except ValueError as error:
            print(error)

    def error_recovery(self) -> None:
        '''Check that water tank is not empty'''
        try:
            if self.__water_tank == 0:
                raise WaterError("Caught GardenError: "
                                 "Not enough water in tank")
        except WaterError as error:
            print(error)
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    '''Print expected output and call all needed methods'''
    raw_garden = [Plant("tomato", 4, 8),
                  Plant("lettuce", 14, 6),
                  Plant(None, 4, 2)]
    manager = GardenManager()
    print("=== Garden Management System ===")

    print("\nAdding plants to garden...")
    for p in raw_garden:
        manager.add_plants(p)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    manager.error_recovery()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
