""" 
Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail.
"""

percMark = float(input("Enter Percentage : "))

if percMark >= 90:
    print("Grade: A+")
elif 80 <= percMark <= 89:
    print("Grade: A")
elif 70 <= percMark <= 79:
    print("Grade: B")
elif 60 <= percMark <= 69:
    print("Grade: C")
else:
    print("Grade: Fail")