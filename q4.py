# Q4: Check if an integer input from the user is positive, negative, or zero

number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")