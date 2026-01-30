# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 18:16:34 by joana             #+#    #+#              #
#    Updated: 2026/01/30 18:28:48 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    ageCheck = int(input("Enter plant age in days: "))
    if ageCheck <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")