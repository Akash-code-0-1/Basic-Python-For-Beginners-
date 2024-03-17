items = {
    "apple": 5,
    "banana": 10,
    "orange": 8,
    "grapes": 15
}

for item, quantity in items.items():
    print(f"{item}: {quantity}")


item_to_remove = input("Enter the item you want to remove: ")

if item_to_remove in items:
    del items[item_to_remove]

for item, quantity in items.items():
    print(f"{item}: {quantity}")