
ages = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 20,
    "David": 35
}

sorted_Ages = dict(sorted(ages.items(), key=lambda x: x[1]))

for name, age in sorted_Ages.items():
    print(f"{name}: {age}")