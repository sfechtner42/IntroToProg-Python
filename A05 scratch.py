student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file = None
import json
file_obj: None
menu_choice: str
FILE_NAME: str = "Enrollments.JSON"
#Inserting Data into JSON file so there is no error

student1: dict[str, str, str] = {"student_first_name": "Bob","student_last_name": "Ross", "course_name": "Painting 101"}
student2: dict[str, str, str] = {"student_first_name": "Issac", "student_last_name": "Newton", "course_name":"Physics 500"}
students: list[dict[str,str,str]] = [student1, student2]

file = open(FILE_NAME, "w")
json.dump(students, file)
file.close()

student_first_name = input("Enter the student's first name: ")
student_last_name = input("Enter the student's last name: ")
course_name = input("Please enter the name of the course: ")
student_data = {"student_first_name": student_first_name, "student_last_name": student_last_name, "course": course_name}

file = open(FILE_NAME, "r")
json.dump(student_data, file)
file.close()