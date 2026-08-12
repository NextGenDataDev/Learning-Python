# Write a program that loops through GPA values [4.8, 3.2, 2.9, 4.1] and prints the classification for each.

gpa = [4.8, 3.2, 2.3, 4.1, 1.0]
for m in gpa:
    if m >= 4.5:
        print("First Class")

    elif m >= 3.5:
        print("Second Class Upper")

    elif m >= 2.5:
        print("Second Class Lower")

    elif m >= 1.5:
        print("Third Class")

    else:
        print("Carryover")

# Write a while loop that counts down from 10 to 1, then prints "Liftoff!".
countdown = 10
while countdown > 0:
    print(f"{countdown}")
    countdown -= 1

print("Liftoff!")

# Write a loop that prints only even numbers from 1 to 20.
for m in range(1, 21):
    if m % 2 == 0:
        print(m)
