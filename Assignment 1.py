
# Task 1 - Variables: Your First Python Intro

# Create a name variable that stores a string (like your name or a fictional character’s name).
# Create an age variable that stores an integer value.
# Create a height variable that stores a floating-point number.

# Task 2 - Operators: Playing with Numbers
# We all love some math, don’t we? Okay, maybe not everyone, but trust me, this will be easy and fun!

# Pick two numbers, let’s say num1 and num2 (you choose the values!).
# Perform the following operations on these numbers:
# Addition
# Subtraction
# Multiplication
# Division
# Write your Python code to calculate and display the results with a nice message for each.

# Task 3 - Conditional Statements: The Number Checker
# Now for the real challenge: let’s make your code think!

# Write a program that takes a number from the user and tells them whether it’s positive, negative, or zero.
# Here’s how it should work:

# Ask the user to enter a number (use the input() function).
# Use if, elif, and else statements to check:
# If the number is greater than 0, print: "This number is positive. Awesome!"
# If the number is less than 0, print: "This number is negative. Better luck next time!"
# If the number is exactly 0, print: "Zero it is. A perfect balance!"
# Make sure to test your code with a few different numbers. You’ll be surprised how fun it is to see your program come to life! 💻✨

# Assignments will be completed in IntelliJ or your preferred IDE. You will need to generate a new Python project from scratch to complete this assignment and host it on GitHub.

# Task 1
name = 'Liz'
age = 21 
height = 5.9

# print introduction. 
print("Hi my name is " + name +" and I am " + str(age) + " years old. I am also "+ str(height) + " inches tall! Happy to be working with everyone!")

#Task 2
num1 = 3
num2 = 10

#print the results
print("The sum of the two numbers is " + str(num1+num2))
print("The result of subtracting them is " + str(num2-num1))
print("Multiplying them will give us " + str(num1*num2))
print("Finally, dividing them makes " + str(num2/num1))

#Task 3
chosen_num = input("Please enter a number ", )

#logic to determine if positive or negative number
if int(chosen_num) > 0: 
    print("Congrats! You have a positive number.")
elif int(chosen_num) < 0: 
    print("This number is negative, better luck next time!")
else: 
    print("0 it is, perfect balance!")

