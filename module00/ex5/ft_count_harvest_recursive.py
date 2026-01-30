# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 18:31:08 by joana             #+#    #+#              #
#    Updated: 2026/01/30 19:09:18 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(currentDay=1, daysCount=-1):
    if (daysCount == -1):
        daysCount = int(input("Days until harvest: "))
    if (currentDay == daysCount):
        print(f"Day {currentDay}")
        print("Harvest time!")
    elif (currentDay < daysCount):
        print(f"Day {currentDay}")
        currentDay += 1
        ft_count_harvest_recursive(currentDay, daysCount)