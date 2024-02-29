m = int(input("Enter the size of the list: "))
converted_words = []

for _ in range(m):
    word = input("Enter a word: ")
    converted_word = ""
    for char in word:
            converted_word += char.swapcase()
    converted_words.append(converted_word)

print("New List:", converted_words)