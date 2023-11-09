# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sabrina Fechtner, 11/8/2023, Wrote Code
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.JSON"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: list= ""
import json
from typing import TextIO
file:TextIO = None
menu_choice: str

#Inserting Data into JSON file so there is no error

student1: dict[str, str, str] = {"student_first_name": "Bob","student_last_name": "Ross", "course_name": "Painting 101"}
student2: dict[str, str, str] = {"student_first_name": "Issac", "student_last_name": "Newton", "course_name":"Physics 500"}
students: list[dict[str,str,str]] = [student1, student2]

file = open(FILE_NAME, "w")
json.dump(students, file)
file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_data = {"student_first_name": student_first_name, "student_last_name": student_last_name, "course": course_name}

        continue

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        for item in students:
            print(student_data)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "r")
        student = json.dump(student_data, file)
        file.close()

        print(
            f"You have registered and saved all data input."
        )
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
