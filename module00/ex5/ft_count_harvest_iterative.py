def ft_count_harvest_iterative():
    daysCount = int(input("Days until harvest: "))
    currentDay = 1
    while currentDay <= daysCount:
        print(f"Day {currentDay}")
        currentDay += 1
    print("Harvest time!")
