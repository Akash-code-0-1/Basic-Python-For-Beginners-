Names = input("Enter list of Names: ").split()

AddedNamesAscii_list = []

for name in Names:
    ascii_sum = 0
    for char in name:
        ascii_sum += ord(char)
    AddedNamesAscii_list.append(ascii_sum)

print("Numerical Values=", AddedNamesAscii_list)
