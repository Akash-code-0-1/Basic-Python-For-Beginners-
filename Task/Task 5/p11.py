def generate_email_list():
    n = int(input("Enter the number of students: "))
    email_list = []

    for _ in range(n):
        name = input("Enter student name: ")
        
        if len(name) > 20:
            continue
        
        lowercase_name = name.lower()
        name_length = len(lowercase_name)
        ascii_value = ord(lowercase_name[0])
        
        email_id = f"{lowercase_name}_{name_length}_{ascii_value}"
        email_list.append(email_id)

    print("\nGenerated Email List:")
    for email in email_list:
        print(email)

generate_email_list()