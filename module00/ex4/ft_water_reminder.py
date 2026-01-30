# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 18:27:33 by joana             #+#    #+#              #
#    Updated: 2026/01/30 18:29:43 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    lastWatering = int(input("Days since last watering: "))
    if lastWatering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")