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


class GardenManager():
    '''Represent the garden(...)'''
    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        '''Initialize plant and its attributes'''
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def add_plants(self) -> None:
        '''Add a plant to the garden'''
        try:
            if self.plant_name is None:
                raise PlantError("Error adding plant: Plant name cannot be empty!")
        except PlantError as error:
            print(error)
            

    def water_plants(self) -> None:
        '''Water a plant'''
    
    def check_plant_health(self) -> None:
        '''Check if plant if healthy'''


def test_garden_management() -> str:
    '''Print expected output and call all needed methods'''
    garden = [("tomato", 5, 8), ("lettuce", 15, 6), (None, 4, 2)]
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    try:
        for plant in garden:
            GardenManager.add_plants(garden[plant])
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    test_garden_management()
