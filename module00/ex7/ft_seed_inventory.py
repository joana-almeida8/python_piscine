# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/30 19:14:57 by joana             #+#    #+#              #
#    Updated: 2026/01/30 19:57:17 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    validUnits = ["packets", "grams", "area"]
    if unit in validUnits:
        if (unit == "packets"):
            print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
        elif unit == "grams":
            print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
        elif unit == "area":
            print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
    