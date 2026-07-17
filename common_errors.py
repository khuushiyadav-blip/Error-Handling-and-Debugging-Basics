# common_errors.py

# ValueError Example
try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Invalid input! Please enter a number.")

# IndexError Example
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("Index out of range.")

# FileNotFoundError Example
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")
