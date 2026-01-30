# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 18:30:39 by joana             #+#    #+#              #
#    Updated: 2026/01/30 19:09:20 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    daysCount = int(input("Days until harvest: "))
    currentDay = 1
    while currentDay <= daysCount:
        print(f"Day {currentDay}")
        currentDay += 1
    print("Harvest time!")