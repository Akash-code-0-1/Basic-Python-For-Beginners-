
def mydicco(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency
  
string = input("Enter a string: ")

char_frequency_dict = mydicco(string)

for char, freq in char_frequency_dict.items():
    print(f"'{char}': {freq}")