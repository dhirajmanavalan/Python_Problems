balance = 1000

while True:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
        break
    else:
        print("Insufficient Balance")

        '''ATM Withdrawal System'''