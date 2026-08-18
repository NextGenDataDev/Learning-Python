# write a program that asks the user for 3 numbers, catches non-numeric input gracefully, and prints their average.
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    avg = (a + b + c)/3
    print(f"The three numbers: {a}, {b} and {c} gives the average: {avg:.2f}.")

except ValueError:
    print("Your input isn't a valid number. Please try again.")

finally:
    print("Come again next time.")

# Write your own text file with 5 lines of "lessons learned this week", then read it back and print it.
with open("Lessons Learned This Week.txt", "w") as file:
    file.write("""
These are the fice lessons I learned this week:
(1.) If you can't explain a concept simply, you don't fully get it yet.
(2.) Can't get motivated? Move first.
(3.) If something takes less than 2 minutes, do it now.
(4.) That awkward thing you said 3 days ago? No one remembers it.
(5.) Start messy.\n
""")

with open("Lessons Learned This Week.txt", "r") as text:
    content = text.read()
    print(content)