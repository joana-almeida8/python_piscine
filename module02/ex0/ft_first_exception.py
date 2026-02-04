# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/04 10:32:02 by joana             #+#    #+#              #
#    Updated: 2026/02/04 11:32:08 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_num(temp_str: str) -> bool:
    '''Checks if the input string is a number'''
    try:
        int(temp_str)
        return True
    except ValueError:
        return False

def check_temperature(temp_str: str) -> int:
    '''Passes the value in string-format to int'''

    print(f"Testing temperature: {temp_str}")
    if is_num(temp_str) == True:
        if int(temp_str) < 0:
            print(f"Error: {temp_str} is too cold for plants (min 0ºC)\n")
        elif int(temp_str) > 40:
            print(f"Error: {temp_str} is too hot for plants (max 40ºC)\n")
        else:
            print(f"Temperature {temp_str}ºC is perfect for plants!\n")
    else:
        print(f"Error: {temp_str} is not a valid number\n")
            
if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print(f"All testes completed - program didn't crash!")