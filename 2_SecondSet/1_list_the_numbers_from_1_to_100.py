for i in range(1, 101):
    divided_by_3: bool = (i % 3) == 0
    divided_by_5: bool = (i % 5) == 0

    if divided_by_3 and divided_by_5:
        print("FizzBuzz")
    elif divided_by_3:
        print("Fizz")
    elif divided_by_5:
        print("Buzz")
    else:
        print(f"List item {i} of 100")