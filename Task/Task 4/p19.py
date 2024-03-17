studentScore={
    "akash" : 30,
    "siam" : 80,
    "tuhin" : 90,
    "moni" : 99,
}
prodects={
    "kewboard": 3000,
    "Laptop": 70000,
    "Mous": 2000
}

merged_dict = studentScore.copy()
merged_dict.update(prodects)

print(merged_dict)