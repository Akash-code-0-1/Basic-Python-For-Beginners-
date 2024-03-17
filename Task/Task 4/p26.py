def letsCount(nd):
    count = 0
    for key, value in nd.items():
        count += 1
        if isinstance(value, dict):
            count += letsCount(value)
    return count

nd = {
    "student1": {
        "name": "Akash",
        "age": 23,
        "address": "Konabri"
    },
    "student2": {
        "name": "Bobi",
        "age": 22,
        "address": "456 No. Street"
    }
}

tp = letsCount(nd)
print(f"Toral pair: {tp}")

