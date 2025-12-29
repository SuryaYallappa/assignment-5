Student_marks={
    "Alice":88,
    "Bob":88,
    "Charlie":88,
    "David":88,
    "Eve":88,
}

name=input("Enter Student's Name: ")
if name in Student_marks:
    print(f"{name}'marks: {Student_marks[name]}")

else:
    print("Student not found")
