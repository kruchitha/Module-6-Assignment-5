'''Module 6: Data Structures and Strings in Python
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''
mark_sheet = {'Alice':85, 'Bob': 60, 'Charlie': 95}
name=input("Enter the student's name: ")
if name in mark_sheet:
    print(f"{name}'s marks:", mark_sheet[name])
else:
    print("Student not found.")

