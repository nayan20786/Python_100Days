import math

# Day2 Project :Tip calculator

# If the bill was $150.00, split between 5 people, with 12% tip.
bill = 150
total_bill = bill + .12 * bill
share = total_bill / 5

print(f"Each person has to give ${share}")

# Each person should pay (150.00 / 5) * 1.12 = 33.6
print(f"{round(share,2)}")
print("{:.2f}".format(share))
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

exit()
# Create a program using maths and f-Strings that tells us how many days, weeks, months
# we have left if we live until 90 years old.

age = int(input("What is your current age?"))
years_left = 90 - age
months_left = 12 * years_left
days_left = 365 * years_left
print(f"You have {years_left} years, {months_left} months and {days_left} days left to live")

print(float(5.5))
exit()

# BMI CALCULATOR CODE EXERCISE
# BMI =WEIGHT/(HEIGHT^2)


weight = float(input("Enter the value of your weight in KG"))
height = float(input("Enter the value of your Height in METER"))

BMI = weight / (math.pow(height, 2))
print(round(BMI, 2))
