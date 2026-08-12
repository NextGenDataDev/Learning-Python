# List
courses = ["CSC321", "CSC322", "CSC331"]
courses.append("CSC341")
print(courses[0])      # First Item
print(courses[-1])     # Last Item
print(courses[1:3])    # Slice

# Dictionary
student = {"name": "Data Muse", "gpa": 4.5, "department": "Computer Science"}
print(student["gpa"])
student["year"] = 300
print(student)    # Add a new key

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)
high_gpas = [g for g in [4.8, 3.2, 2.9, 4.1] if g > 3.5]
print(high_gpas)