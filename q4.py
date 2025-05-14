n = int(input("Enter number: "))
if n % 2 == 0 and n % 5 == 0:
    print("Even and divisible by 5")
elif n % 2 != 0 and n % 5 == 0:
    print("Odd and divisible by 5")
elif n % 2 == 0:
    print("Even and not divisible by 5")
else:
    print("Odd and not divisible by 5")
