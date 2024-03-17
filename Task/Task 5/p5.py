input_string = input("Enter a string: ")
vowel_count = 0

for char in input_string:
    if char.lower() not in 'aeiou':
        continue
    vowel_count += 1
   
print(f"The number of vowels is: {vowel_count}")