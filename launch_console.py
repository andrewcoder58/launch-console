print("Welcome to the Elite 101 Launch Console!")

name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

while True:
    print("\nMenu")
    print("1. About me")
    print("2. My goals")
    print("3. Fun fact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"\nHi, I'm {name}! I'm learning how to code.")
    elif choice == "2":
        print("\nMy goal is to build cool projects!")
    elif choice == "3":
        print("\nFun fact: Python was named after the circus group Monty Python.")
    elif choice == "4":
        print(f"\nGoodbye, {name}! Thanks for stopping by!")
        break
    else:
        print("\nThat's not a valid choice. Please try again.")
