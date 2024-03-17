def employeSalary(employee_dict, emp_id, new_salary):
    for emp_details in employee_dict.values():
        if emp_details.get("employee_id") == emp_id:
            emp_details["salary"] = new_salary
            return
        
employee_details = {
    "emp1": {"employee_id": 101, "name": "Akash", "salary": 50000},
    "emp2": {"employee_id": 102, "name": "Tuhin", "salary": 60000}
}

print(employee_details)

employeSalary(employee_details, 102, 65000)

for key, emp_info in employee_details.items():
    print(f"Employee ID: {emp_info['employee_id']}, Name: {emp_info['name']}, Salary: {emp_info['salary']}")