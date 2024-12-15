try:
    limit: int = int(input("Enter a limit number: "))
    for i in range(1, limit+1):
        print(f"List item {i} of {limit}")
except ValueError:
    print("Invalid input. Please enter a number.")