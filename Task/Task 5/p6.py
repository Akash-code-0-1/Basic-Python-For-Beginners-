def checkUniq(input_string):
    seen_chars = set()
    for char in input_string:
        if char in seen_chars:
            print("String does not contain all unique characters.")
            break
        seen_chars.add(char)
    else:
        print("String contains all unique characters.")

user_input = input("Enter a string: ")
checkUniq(user_input)