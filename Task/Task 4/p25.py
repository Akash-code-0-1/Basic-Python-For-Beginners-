student_details = {
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

student_name = student_details["student1"]["name"]
student_age = student_details["student1"]["age"]
student_address = student_details["student1"]["address"]

print("Student Details:")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Address: {student_address}")