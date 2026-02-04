# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joana <joana@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/04 11:37:08 by joana             #+#    #+#              #
#    Updated: 2026/02/04 17:59:19 by joana            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations(error_type: str) -> str:
    '''Test different error inputs and return the caught exception'''

    plants = {"Flower": ["sunflower" "tulip" "lily"], "Tree": "Oak"}
    if error_type == "value":
        try:
            int("error")
        except ValueError:
            return "Caught ValueError: invalid literal for int()\n"
    
    elif error_type == "zero":
        try:
            42 / 0
        except ZeroDivisionError:
            return "Caught ZeroDivisionError: division by zero\n"

    elif error_type == "file":
        try:
            open('missing.txt')
        except FileNotFoundError:
            return "Caught FileNotFoundError: No such file 'missing.txt'\n"

    elif error_type == "key":
        try:
            plants["rose"]
        except KeyError:
            return "Caught KeyError: 'missing\_plant'\n"

    else:
        try:
            int("error")
            42 / 0
            open('missing.txt')
            plants["rose"]
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            return "Caught an error, but the program continues!\n"

def test_error_types() -> None:
    '''Execute different tests for different error types'''
    print("Testing ValueError...")
    print(garden_operations("value"))
    print("Testing ZeroDivisionError...")
    print(garden_operations("zero"))
    print("Testing FileNotFoundError...")
    print(garden_operations("file"))
    print("Testing KeyError...")
    print(garden_operations("key"))
    print("Testing multiple errors together...")
    print(garden_operations("other"))

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")