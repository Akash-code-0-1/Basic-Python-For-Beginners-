def print_reverse_list(lst):
    if not lst:
        return
    print(lst[-1])
    print_reverse_list(lst[:-1])

numbers = list(map(int, input("Enter a list of Numbers: ").split()))
print("Reverse List is:")
print_reverse_list(numbers)
