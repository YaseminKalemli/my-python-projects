 #Student Grading System

print("Welcome to the Student Grading System")
print("Please enter the 3 students' names and their 3 grades.")

student1_name = input("Enter the name of the first student:")
student1_grade1 = float(input(f"Enter {student1_name}'s first grade:"))
student1_grade2 = float(input(f"Enter {student1_name}'s second grade:"))
student1_grade3 = float(input(f"Enter {student1_name}'s third grade:"))

student2_name = input("Enter the name of the second student:")
student2_grade1 = float(input(f"Enter {student2_name}'s first grade:"))
student2_grade2 = float(input(f"Enter {student2_name}'s second grade:"))
student2_grade3 = float(input(f"Enter {student2_name}'s third grade:"))

student3_name = input("Enter the name of the third student:")
student3_grade1 = float(input(f"Enter {student3_name}'s first grade:"))
student3_grade2 = float(input(f"Enter {student3_name}'s second grade:"))
student3_grade3 = float(input(f"Enter {student3_name}'s third grade:"))

students = {student1_name: [student1_grade1, student1_grade2, student1_grade3], student2_name: [student2_grade1, student2_grade2, student2_grade3], student3_name: [student3_grade1, student3_grade2, student3_grade3] }
print("Students = ", students)  

print("Calculating averages... ") 
student1_avg = sum(students[student1_name]) / 3
student2_avg = sum(students[student2_name]) / 3
student3_avg = sum(students[student3_name]) / 3 
print(f"{student1_name}'s average is: {round(student1_avg)}")
print(f"{student2_name}'s average is: {round(student2_avg)}")
print(f"{student3_name}'s average is: {round(student3_avg)}")
 
print("The student with the highest average is:" )
if student1_avg > student2_avg and student1_avg > student3_avg:
    print(f"{student1_name} with an average of {round(student1_avg)}")
elif student2_avg >student1_avg and student2_avg> student3_avg:
    print(f"{student2_name} with an average of {round(student2_avg)}")
else:
    print(f"{student3_name} with an avarege of {round(student3_avg )}")
    
print("Thank you for using the Student Grading System!")    






  



    
    














