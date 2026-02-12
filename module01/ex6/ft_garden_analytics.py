class Plant:
    '''Represent a Plant and all its attributes'''
    def __init__(self, name: str, height: int) -> None:
        '''Initialize a new Plant with its attributes'''
        self.name = name
        self.__height = 0
        self.set_height(height)
        self.initial_height = self.__height

    def set_height(self, height: int) -> None:
        '''Check if height is negative to prevent data corruption'''
        if height < 0:
            print((f"\nInvalid operation attempted: "
                  f"height {height}cm [REJECTED]"))
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def get_height(self) -> int:
        '''Get public __height in cm'''
        return self.__height

    def get_growth(self) -> int:
        '''Calculate specific plant growth'''
        return self.__height - self.initial_height

    def grow(self, garden_owner: str) -> None:
        '''Increase plant height by 1cm'''
        self.__height += 1
        if garden_owner == "Alice":
            print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        '''Print a formatted string describing
        the Plant's current attributes'''
        return f"{self.name}: {self.__height}cm"


class FloweringPlant(Plant):
    '''Represent a single FloweringPlant and
    inherits Plant attributes'''

    def __init__(self, name: str, height: int, colour: str) -> None:
        '''Initialize a new FloweringPlant with inherited
        Plant attributes and its own'''
        super().__init__(name, height)
        self.__colour = "none"
        self.set_colour(colour)

    def set_colour(self, colour: str) -> None:
        '''Check if colour exists to prevent data corruption'''
        if colour is not None:
            self.__colour = colour
            return self.__colour
        elif colour is None:
            print((f"Invalid operation attempted: "
                   f"colour {self.__colour} [REJECTED]"))

    def __str__(self) -> str:
        '''Print a formatted string describing the
        FloweringPlant's current attributes'''
        return f"{super().__str__()}, {self.__colour} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    '''Represent a single PrizeFlower and inherits FloweringPlant attributes'''
    def __init__(self, name: str, height: int,
                 colour: str, prize: int) -> None:
        '''Initialize a new PrizePlant with inherited FloweringPlant
        attributes and its own'''
        super().__init__(name, height, colour)
        self.__prize = 0
        self.set_prize_points(prize)

    def set_prize_points(self, prize: int) -> None:
        '''Check if prize points are bigger than 0
        to prevent data corruption'''
        if prize > 0:
            self.__prize = prize
            return self.__prize
        else:
            print((f"Invalid operation attempted: "
                   f"prize points {self.prize} [REJECTED]"))

    def get_prize_points(self) -> None:
        '''Get prize points of the plant'''
        return self.__prize

    def __str__(self) -> str:
        '''Print a formatted string describing the
        PrizeFlower's current attributes'''
        return f"{super().__str__()}, Prize points: {self.__prize}"


class GardenManager:
    '''Manage multipe gardens and all their plants'''
    total_gardens = 0

    def __init__(self, owner: str) -> None:
        '''Initialize an owner's garden with no plants'''
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        '''Add a plant to the owner's garden'''
        self.plants.append(plant)
        if self.owner == "Alice":
            print(f"Added {plant.name} to {self.owner}'s garden")

    def validate_heights(self) -> bool:
        '''Check if height is negative to prevent data corruption'''
        index = 0
        while index < len(self.plants):
            current_plant = self.plants[index]
            if current_plant.get_height() >= 0:
                index += 1
            else:
                return False
        return True

    @classmethod
    def create_garden_nextwork(cls, names: list[str]) -> list['GardenManager']:
        '''Factory method to generate a list of GardenManager owners'''
        return [cls(name) for name in names]

    class GardenStats:
        '''Helper class for calculating statistics'''

        def __init__(self, owner: str) -> None:
            '''Initialize garden stats'''
            pass

        def calc_score(plants) -> int:
            '''Return the sum of all plant heights'''
            score = sum(p.get_height() for p in plants)
            for p in plants:
                if isinstance(p, PrizeFlower):
                    score += p.get_prize_points()
            return score

        @staticmethod
        def print_plant_stats(plants) -> None:
            '''Calculate and print counts for regular,
            flowering, and prize plants'''
            regular = sum(1 for p in plants if type(p) is Plant)
            flowering = sum(1 for p in plants if type(p) is FloweringPlant)
            prize_flowers = sum(1 for p in plants if type(p) is PrizeFlower)
            total_growth = sum(p.get_growth() for p in plants)
            print((f"\nPlants added: {len(plants)}, "
                   f"Total growth: {total_growth}cm"))
            print((f"Plant types: {regular} regular, {flowering} flowering, "
                   f"{prize_flowers} prize flowers"))


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    gardens = GardenManager.create_garden_nextwork(["Alice", "Bob"])
    alice_garden = gardens[0]
    bob_garden = gardens[1]

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    bob_garden.add_plant(Plant("Pine Tree", 200))
    bob_garden.add_plant(FloweringPlant("Tulip", 15, "pink"))
    bob_garden.add_plant(FloweringPlant("Dahlia", 20, "black"))

    print(f"\n{alice_garden.owner} is helping all plants grow...")
    for plant in alice_garden.plants:
        plant.grow(alice_garden.owner)

    # print(f"\n{bob_garden.owner} is helping all plants grow...")
    for plant in bob_garden.plants:
        plant.grow("Bob")

    alice_score = GardenManager.GardenStats.calc_score(alice_garden.plants)
    bob_score = GardenManager.GardenStats.calc_score(bob_garden.plants)

    print(f"\n=== {alice_garden.owner}'s Garden Report ===")
    print("Plants in garden:")
    for p in alice_garden.plants:
        print(f"- {p}")

    # print(f"\n=== {bob_garden.owner}'s Garden Report ===")
    # print("Plants in garden:")
    # for p in bob_garden.plants:
    #         print(f"- {p}")

    GardenManager.GardenStats.print_plant_stats(alice_garden.plants)

    print(f"\nHeight validation test: {alice_garden.validate_heights()}")
    print((f"Garden Score = {alice_garden.owner}: {alice_score}, "
           f"{bob_garden.owner}: {bob_score}"))
    print(f"Total gardens managed: {GardenManager.total_gardens}")
