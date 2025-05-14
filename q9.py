user = input("Enter username: ")
role = input("Enter role: ")
if user in ['john', 'amy', 'sita'] and role in ['admin', 'manager']:
    print("Login successful")
else:
    print("Access denied")

