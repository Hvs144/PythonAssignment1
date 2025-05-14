amt = int(input("Enter amount: "))
bal = int(input("Enter balance: "))
if amt <= bal and amt % 100 == 0:
    print("Withdrawal allowed")
else:
    print("Invalid withdrawal")
