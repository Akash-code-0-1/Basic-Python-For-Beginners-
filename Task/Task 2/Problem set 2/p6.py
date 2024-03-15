def indexFind(lst, key):
    for i, num in enumerate(lst):
        if num == key:
            return i
    return -1

numbers = list(map(int, input("Enter a list of Numbers: ").split()))
target_num = int(input("Enter Your Target Number: "))
res = indexFind(numbers, target_num)
if res != -1:
    print("Here,", target_num, "occurs in [", res+1, "] index for the first time.")
else:
    print("Your target number", target_num, " Not Found.")
