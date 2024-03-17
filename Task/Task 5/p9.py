def unc():
    n = int(input("Enter the number of strings: "))
    unique_chars = set()

    for _ in range(n):
        strings = input("Enter a string: ")
        unique_chars.update(set(strings))

    sorted_chars = sorted(unique_chars)
    print(f"Output: {sorted_chars}")

unc()