pwd = input("Enter password: ")
if len(pwd) >= 8 and '@' in pwd:
    print("Strong password")
else:
    print("Weak password")

