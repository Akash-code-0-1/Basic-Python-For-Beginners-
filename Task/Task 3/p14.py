""" 
Write a Python program using a while loop to reverse a given string.

"""

def reverse_string_while(input_string):
    reversed_string = ""
    index = len(input_string) - 1

    while index >= 0:
        reversed_string += input_string[index]
        index -= 1

    return reversed_string

input_string = "Akash"
print("String: ",input_string)
reversed_string = reverse_string_while(input_string)
print("Reversed string:", reversed_string)