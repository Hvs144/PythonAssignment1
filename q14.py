n = int(input("Enter number: "))
if n % 3 == 0 and n % 5 == 0:
    print("Divisible by 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")
