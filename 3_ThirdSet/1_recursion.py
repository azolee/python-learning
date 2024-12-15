import sys
from Helpers.math import factorials, factorials_iterativ

max_recursion_depth = sys.getrecursionlimit()-2
sys.set_int_max_str_digits(100000000)
while True:
    try:
        user_input = input("Enter a number to calculate it's factorial or type 'exit': ")
        if user_input == "exit":
            break

        number: int = int(user_input)

        if number < 0:
            print("Please enter a positive number.")
        else:
            if number > max_recursion_depth:
                print(f"The factorial of {number} is", factorials_iterativ(number))
            else:
                print(f"The factorial of {number} is", factorials(number))
    except ValueError as e:
        print(f"Please enter a valid number: ", e)
    except RecursionError as e:
        print(f"Please enter a number less than or equal to {max_recursion_depth}.", e)