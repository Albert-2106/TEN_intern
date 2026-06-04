try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")


    
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid number.")

