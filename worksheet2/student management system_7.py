students={
    "Ravi":{"marks":75,"grade":"C"},
    "Shivani":{"marks":95,"grade":"A"},
    "Jyothi":{"marks":63,"grade":"D"},
    "Lavanya":{"marks":82,"grade":"B"},
    "Suresh":{"marks":43,"grade":"F"},
    "swathi":{"marks":100,"grade":"A"}
}
for name,details in students.items():
    print(f"{name},marks:{details["marks"]},grade:{details["grade"]}")
highest_student=0
highest_marks=75
highest_grade=" "
for name, details in students.items():
    if details["marks"] > highest_marks:   
        highest_marks = details["marks"]
        highest_student = name
        highest_grade= details["grade"]

print("\nStudent with highest marks:")
print("Name:", highest_student)
print("Marks:", highest_marks)
print("Grade",highest_grade)
