username = "admin"
password = "1234"

attempts = 3

while attempts > 0:
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print(f"Invalid! Attempts left: {attempts}")

if attempts == 0:
    print("Account Locked")

    # 🚀 1. Login Authentication System