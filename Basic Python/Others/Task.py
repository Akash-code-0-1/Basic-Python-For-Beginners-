Student_Result = {
    "student1": {"Math": 75, "Physics": 83, "English": 76},
    "student2": {"Math": 81, "Physics": 85, "English": 72},
    "student3": {"Math": 75, "Physics": 81, "English": 85}
}

average_marks = []
for student in Student_Result:
    total_marks = (sum(Student_Result[student].values()))
    average_mark_perstudent= total_marks / len(Student_Result[student])
    
    
    average_marks.append(int(average_mark_perstudent))
    

print("Average-Marks:", average_marks)