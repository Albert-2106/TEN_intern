# Python Basics Practice Program

# Variables
name = "Abhiram Yalla"
age = 20
height = 5.9
is_student = True

# Output
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student Status:", is_student)

print("\n--- User Input Section ---")

# Input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# Processing
birth_year = 2026 - user_age

# Output
print("\nHello,", user_name)
print("You were born around:", birth_year)

# Data Types Check
print("\n--- Data Types ---")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Simple Calculator
print("\n--- Simple Addition Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2

print("Sum =", sum_result)
