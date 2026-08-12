# if/elif/else
gpa = 4.5

if gpa >= 4.5:
    print("First Class")

elif gpa >= 3.5:
    print("Second Class")

else:
    print("Keep Pushing")

# For Loop
for i in range(5):
    print(f"Week {i + 1}")

# While Loop
count = 0
while count < 3:
    print(f"Attempt {count + 1}")
    count += 1     # Forgetting this line = infinite loop.