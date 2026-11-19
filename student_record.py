
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    students.append({
        "name": name,
        "marks": marks
    })

print("\nStudent Records")

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    

