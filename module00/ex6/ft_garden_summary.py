# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 19:10:11 by joana             #+#    #+#              #
#    Updated: 2026/01/30 19:14:06 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    gardenName = input("Enter garden name: ")
    plantNum = input("Enter number of plants: ")
    print(f"Garden: {gardenName}")
    print(f"Plants: {plantNum}")
    print("Status: Growing well!")