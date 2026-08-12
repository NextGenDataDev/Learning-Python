# Build a dictionary representing yourself with keys: name, department, gpa, courses (a list).
me = {"Name": "NeuralMutee", "Department": "Computer Science",
      "GPA": 3.0, "Courses": ["CSC335", "CSC301", "CSC313",
      "MAT352", "GES103", "GES301"]}
print(me)

# Use a list comprehension to get only courses that start with "CSC3" from a list of course codes.
find = [course for course in me["Courses"] if course.startswith("CSC3")]
print(find)

# Write a code that safely checks if a key exists in a dictionary before accessing it
# Method One:
if "GPA" in me:
    print(me["GPA"])
else:
    print("GPA doesn't exist.")

# Method Two:
gpa = me.get("GPA")
if gpa is not None:
    print(gpa)
else:
    print("GPA does not exist.")