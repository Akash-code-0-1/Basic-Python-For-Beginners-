while True:
    password = input("Enter a password: ")

    if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        print("Please try again.")
        continue
    else:
        print("Password accepted.")
        break