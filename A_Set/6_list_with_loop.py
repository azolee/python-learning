favourite_foods = ['pizza', 'pasta', 'salad', 'sushi', 'ice cream', 'chocolate', 'cake', 'cookies', 'chips', 'popcorn']
favourite_foods.sort()

while True:
    try:
        line_limit = int(input('Enter the number of items per line: '))
        max_number = len(favourite_foods)
        if 0 < line_limit <= max_number:
            break
        else:
            print(f"Please enter a positive number between 1 and {max_number}.")
    except ValueError:
        print('Please enter a number.')

print('\n- My favourite foods are:')
for index, food in enumerate(favourite_foods):
    if index > 0 and index % line_limit == 0 and index != max_number - 1:
        print()
    print(food.capitalize(), end=', ')
print("\n")
