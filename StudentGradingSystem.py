 #Student Grading System

print("Welcome to the Student Grading System")

students = {}

for i in range(3):
    name = input(f"Enter the student {i+1} name:")
    grades = []
    for j in range(3):
        grade = float(input(f"Enter the grade {j+1} for {name}:"))
        grades.append(grade)
    students[name] = grades
print(students)

print("Student averages:")
highest_avg = 0
top_student = ""

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name}'s average: {avg:.2f}")
    if avg > highest_avg:
        highest_avg = avg
        top_student = name
        
print(f"Top student: {top_student} with average {highest_avg:.2f}")
    
print("Thank you for using the Student Grading System!")    






  



    
    














