prodects={
    "kewboard": 3000,
    "Laptop": 70000,
    "Mous": 2000
}

target=70000

for key, value in prodects.items():
    if value==target:
        print(f"{key}")