"""
1.	String Reverse: Write a Python function to reverse a given string and return the reversed string. 
"""
def reverse_string(input_string):
    return input_string[::-1]

input_string = input("Entter a String: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)



#another solution
for char in reversed(input_string):
    print(char,end='')