def ft_plant_age():
    ageCheck = int(input("Enter plant age in days: "))
    if ageCheck <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
