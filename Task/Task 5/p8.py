def display_menu():
    print("Welcome to the Grocery Shop!")
    print("1. Add item to the bucket list")
    print("2. Remove item from the bucket list")
    print("3. View bucket list")
    print("4. Exit")

def add_item(bucket_list):
    item = input("Enter the item you want to add: ")
    bucket_list.append(item)
    print(f"{item} added to the bucket list.")

def remove_item(bucket_list):
    item = input("Enter the item you want to remove: ")
    if item in bucket_list:
        bucket_list.remove(item)
        print(f"{item} removed from the bucket list.")
    else:
        print(f"{item} is not in the bucket list.")

def view_bucket_list(bucket_list):
    print("\nBucket List:")
    for index, item in enumerate(bucket_list, 1):
        print(f"{index}. {item}")

bucket_list = []

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_item(bucket_list)
    elif choice == '2':
        remove_item(bucket_list)
    elif choice == '3':
        view_bucket_list(bucket_list)
    elif choice == '4':
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")