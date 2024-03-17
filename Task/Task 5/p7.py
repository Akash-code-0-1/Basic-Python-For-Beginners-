student_data = {}

def submit_information():
    print("Welcome to the Student Information System!")
    while True:
        print("\nChoose the information you want to submit:")
        print("1. Name")
        print("2. Age")
        print("3. ID")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name (max 5 characters): ")
            student_data['Name'] = name[:5]
        elif choice == '2':
            age = float(input("Enter your age: "))
            student_data['Age'] = age
        elif choice == '3':
            student_id = input("Enter your ID (max 5 characters): ")
            student_data['ID'] = student_id[:5]
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nStudent Information Submitted:")
    for key, value in student_data.items():
        print(f"{key}: {value}")

submit_information()