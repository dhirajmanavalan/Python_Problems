'''Simple Menu System'''

while True:
    print("1. Say Hello")
    print("2. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Hello User!")
    elif choice == 2:
        print("Exiting...")
        break
    else:
        print("Invalid choice")