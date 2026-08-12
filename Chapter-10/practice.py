# Write a function calculate_average(numbers) that takes a list and returns the average.
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

scores = [69, 76, 96, 84, 91]
print(calculate_average(scores))

# Write a function is_first_class(gpa) returning True/False.
def is_first_class(gpa):
    if gpa >= 4.5:
        return True
    else:
        return False

gpa = 3.9
print(is_first_class(gpa))