while True:
    word = input("Enter a word: ")

    if len(word) < 3:
        print("Word length is less than 3 characters. Skipping...")
        continue

    if word == word[::-1]:
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")