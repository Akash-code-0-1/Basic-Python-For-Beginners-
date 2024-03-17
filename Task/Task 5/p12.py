def compress_string():
    num_strings = int(input("Enter How many Strings: "))
    max_length = int(input("Enter Size of String: "))
    
    compressed_strings = []
    
    for _ in range(num_strings):
        input_string = input("Enter a string: ")
        compressed_string = ""
        
        i = 0
        while i < len(input_string):
            count = 1
            while i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
                count += 1
                i += 1
            compressed_string += str(count) + input_string[i]
            i += 1
        
        compressed_strings.append(compressed_string[:max_length])

    return compressed_strings

output = compress_string()
print("Output:")
print(output)