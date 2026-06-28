balance = int(input("Enter Balance: "))

withdrawal_times = int(input("Enter how many time do you want to withdrawal: "))

for i in range(1,withdrawal_times+1):
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance and amount%100==0:
        balance = balance-amount
        print("Success")

    else:
        print("Failed")

print("Final Balance amount: ", balance)




# if amount < balance:
#     balance = balance-amount
#     print("Success")
#     print("Balance :",balance)
# else:
#     print("Failed")


