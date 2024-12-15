while True:
    user_input = input("Kerem adjon meg egy szamot: ")
    if user_input == "exit":
        break
    try:
        num: int = int(user_input)

        if num % 2 == 0:
            print("Ez a szam paros!")
        else:
            print("Ez a szam paratlan!")
    except ValueError:
        print("Ez nem egy szam!")
