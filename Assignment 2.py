# Step 1: Ask the User’s Age
# Your program should start by asking the user:

# age = int(input("How old are you? "))
# Make sure you convert the input into an integer so you can use it in calculations later.

# Step 2: Decide the Eligibility
# Use a conditional statement to check if the age is 18 or older. Here’s the logic:

# If the user’s age is 18 or above, display a warm message like:
# "Congratulations! You are eligible to vote. Go make a difference!"
# If the user’s age is less than 18, calculate how many years they have to wait. Display a friendly message like:
# "Oops! You’re not eligible yet. But hey, only X more years to go!"
# Step 3: Test with Different Ages

age = int(input("How old are you? "))

if(age >= 18): 
    print("Congratulations! You are eligible to vote. Go make your parents proud :|")
else: 
    print("Oops! You aren't legal yet. BUt hey, only " + str(18 - age) + " years to go!")

