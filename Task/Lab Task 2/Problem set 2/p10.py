def unique_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    return sorted(unique_to_list1.union(unique_to_list2))

list1 = list(map(int, input("Enter a list of Numbers: ").split()))
list2 = list(map(int, input("Enter a list of Numbers: ").split()))
new_list = unique_numbers(list1, list2)
print("Unique and Sorted List is:", " ".join(map(str, new_list)))
