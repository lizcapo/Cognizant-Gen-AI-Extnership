# Task 1 - Counting Down with Loops
# Write a Python program to create a countdown timer.

# Ask the user for a starting number.
# Use a while loop to print numbers from that number down to 1.
# When the countdown ends, print a celebratory message like "Blast off!"

# Task 2 - Multiplication Table with for Loops
# Write a program that generates the multiplication table for any number provided by the user.

# Ask the user to input a number.
# Use a for loop to print the multiplication table for that number (from 1 to 10).

# Task 3 - Find the Factorial
# Write a Python program to calculate the factorial of a number entered by the user.

# Ask the user for a number.
# Use a for loop to calculate the factorial.
# Print the result in a friendly format.

# TASK 1
user_num = int(input("Please give me a number "))

while user_num > 0: 
    print(user_num, end='')
    user_num -= 1

print("Hooray!")

# TASK 2
num2 = int(input("Please give me a number "))

for i in range(10): 
    print(num2 * i)


# TASK 3
num3 = int(input("Please give me a number "))
factorial = 1

for a in range(1, num3 + 1):
    factorial *= a

print(f"The factorial of {num3} is {factorial}")
    






