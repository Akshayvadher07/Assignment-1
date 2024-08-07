# Q7: Print the multiplication table of a given number using a while loop

number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
