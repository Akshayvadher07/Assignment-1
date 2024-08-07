# Assignment-1

# Q1: Print "Hello, World!" to the console

print("Hello, World!")


# Q2: Create variables for name, age, and favorite hobby, then print them

name = "Alice"           # Your name
age = 25                 # Your age
favorite_hobby = "reading"  # Your favorite hobby

print("Name:", name)
print("Age:", age)
print("Favorite Hobby:", favorite_hobby)

# Q3: Add comments explaining what each line does

name = "Alice"           # Assigns the string "Alice" to the variable name
age = 25                 # Assigns the integer 25 to the variable age
favorite_hobby = "reading"  # Assigns the string "reading" to the variable favorite_hobby

print("Name:", name)  # Prints the label "Name:" followed by the value of name
print("Age:", age)    # Prints the label "Age:" followed by the value of age
print("Favorite Hobby:", favorite_hobby)  # Prints the label "Favorite Hobby:" followed by the value of favorite_hobby


# Q4: Check if an integer input from the user is positive, negative, or zero

number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Q5: Check if a given year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# Q6: Print the first 10 natural numbers using a for loop

for i in range(1, 11):
    print(i)


# Q7: Print the multiplication table of a given number using a while loop

number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1


# Q8: Print numbers from 1 to 10, skip those divisible by 3

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)


# Q9: Stop printing numbers when encountering a number greater than 5

for i in range(1, 11):
    if i > 5:
        break
    print(i)


# Q10: Define a function greet that takes a name as an argument and prints a greeting

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Q11: Create a function that takes two numbers and returns their sum

def sum_numbers(a, b):
    return a + b

result = sum_numbers(5, 3)
print("The sum is:", result)
