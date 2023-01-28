import csv

tt1 = ["RollNo", "Name", "Subject"]
with open('students.csv', 'w', newline='') as student_file:
    writer = csv.writer(student_file)
    writer.writerow(tt1)
