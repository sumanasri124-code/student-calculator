# Result Calculator for student
student_name = input("Enter student name: ")
subject_marks = []
print("\nEnter marks for 5 subjects:")
for subject in range(1, 6):
 marks = int(input(f"Subject {subject}: "))
 subject_marks.append(marks)
# Calculate total and average
total_marks = sum(subject_marks)
average_marks = total_marks / len(subject_marks)
if average_marks >= 90: # calculating marks for grades
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "F"
# To know pass or fail
if min(subject_marks) >= 35:
    status = "PASS"
else:
    status = "FAIL"
print("\n STUDENT RESULT ") #showing marks
print("Student Name:", student_name)
print("Marks:", subject_marks)
print("Total Marks:", total_marks)
print("Average:", round(average_marks, 2))
print("Grade :", grade)
print("Result:", status)
print(" ")