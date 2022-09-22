password = input("password: ")
while len(password) < 8:
    print("The password should be consisted of at least 8 characters.")
    password = input("password: ")
print(f'password: {len(password) * "*"}')