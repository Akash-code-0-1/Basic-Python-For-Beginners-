sum = 0
while True:
    num = int(input("Enter list of positive number (negative to stop): "))
    
    if num < 0:
        break
    
    sum += num

print(f"Total positive Sum: {sum}")