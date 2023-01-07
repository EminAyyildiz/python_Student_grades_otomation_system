# Written by Emin Ayyıldız
print("Written by Emin Ayyıldız")
import time
file_name = "students'_grades.txt.txt"
def show_grades():
    with open("students'_grades.txt","r", encoding="utf-8") as file:
        for line in file:
            print(grade_letter_calculator(line))
def grade_letter_calculator(line):
    line = line[:-1]
    new_list = line.split(':')
    student_name = new_list[0]
    grades = new_list[1].split(',')
    grade_1 = int(grades[0])
    grade_2 = int(grades[1])
    grade_3 = int(grades[2])
    average = (grade_1 + grade_2 + grade_3)/3
    if average >= 90 and average <=100:
        letter_grade = "AA"
    elif average >= 85  and average <=89:
        letter_grade = "BA"
    elif average >= 80  and average <=84:
        letter_grade = "BB"
    elif average >= 75  and average <=79:
        letter_grade = "CB"
    elif average >= 70  and average <=74:
        letter_grade = "CC"
    elif average >= 65  and average <=69:
        letter_grade = "DC"
    elif average >= 60  and average <=64:
        letter_grade = "DD"
    elif average >= 50  and average <=59:
        letter_grade = "FD"
    else:
        letter_grade = "FF"
    return student_name+ ": " +letter_grade+ "\n"
def enter_grade():
    name = input("Student's Name :")
    surname = input("Student's Surname :")
    grade_1 = input("First Grade :")
    grade_2 = input("Second Grade :")
    grade_3 = input("Third Grade :")

    with open("students'_grades.txt","a", encoding="utf-8") as file:
        file.write(name+' '+surname+' :'+grade_1+','+grade_2+','+grade_3+ '\n')

def save_grades():
    last_list = []
    with open("students'_grades.txt", "r", encoding="utf-8") as file:
        for i in file:
            last_list.append(grade_letter_calculator(i))
    with open("last_grade_with_letter.txt", "w", encoding="utf-8") as file2:
        for i in last_list:
            file2.write(i)
def select_student(file_name):
  names = []
  grades = []
  with open("students'_grades.txt", "r") as file:
    for line in file:
        line = line[:-1]
        new_list = line.split(':')
        student_name_line = new_list[0].strip()
        grades_line = new_list[1].split(',')
        names.append(student_name_line)
        grades.append(grades_line)
  name = input("Please Enter a Student name : ")
  if name in names:
    index = names.index(name)
    print(grades[index])
  else:
    print("Invalid Student name.")
while True:

    choice = input("Please select your want do do.\n"
                   "1- Show Students' Grades\n"
                   "2- Enter Student's Grade \n"
                   "3- Save Grades \n"
                   "4- Select a Student \n"
                   "5- EXIT\n------>")
    if choice == "1":
        print("All students' grades are displayed. Please wait...")
        time.sleep(1.5)
        show_grades()
    elif choice == "2":
        enter_grade()
    elif choice == "3":
        save_grades()
        print("Grades are being saved....")
        time.sleep(1.5)
        print("All Grades Saved \n")
    elif choice == "4":
        select_student(file_name)
    elif choice == "5":
        print("Thank you for using our system :) ")
        break
    else:
        print("Invalid Selection")
