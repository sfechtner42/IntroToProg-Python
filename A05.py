# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sabrina Fechtner, 11/8/2023, Wrote Pseudocode
#   Sabrina Fechtner, 11/9/2023, Finished Writing Intial Code
#   Sabrina Fechtner, 11/10/2023, Added Exceptions
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
import json
from typing import TextIO

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
student_data: dict = None
file: TextIO = None
menu_choice: str
students: list[dict] = []

# Try reading existing data first
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
    print("Data successfully loaded from the file.")
except FileNotFoundError as e:
    print(f"File not found, creating it...")
    students = []
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)
except json.JSONDecodeError as e:
    print(f"Invalid JSON file: {e}. Resetting it...")
    students = []
except Exception as e:
    print(f"An unexpected error occurred while loading data: {e}")
    students = []
finally:
    if file and not file.closed:
        file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do?: ")

    # Input user data
    if menu_choice == "1":
        while True:
            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("The first name cannot be alphanumeric. Please re-enter the first name.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name cannot be alphanumeric. Please re-enter the last name.")
                break
            except ValueError as e:
                print(e)
        course_name = input("Please enter the name of the course: ")
        student_data = {"student_first_name": student_first_name, "student_last_name": student_last_name,
                        "course": course_name}
        students.append(student_data)
        continue

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        for item in students:
            print(item)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file)
                file.write('\n')
            print("Data successfully written to the file.")
        except (FileNotFoundError, IOError) as e:
            print(f"Error writing to the file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            if file and not file.closed:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
