# Reading a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Writing a file
with open("output.txt", "w") as file:
    file.write("This is my first written file.\n")

# Error handling
try:
    gpa = float(input("Enter your GPA: "))
    print(f"Your GPA is {gpa}.")

except ValueError:
    print("That's not a valid number. Try again.")

finally:
    print("Attempt finished.")

# Importing modules
import datetime
today = datetime.date.today()
print(f"Today is {today}.")