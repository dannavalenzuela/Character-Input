# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Improvement Needed:
# Loop if invalid values

import datetime

repeat = "Y"
repeat = repeat.upper()

while (repeat == "Y"):
    
    name = raw_input("Please enter your name: ")
    age = int(raw_input("Please enter your age: "))
    birthday = raw_input("Did you already celebrate your birthday this year?, Enter Y or N: ")
    printNum = int(raw_input("Desired count of print?, Please enter a number: "))
    
    birthday = birthday.upper()
    
    if birthday == "N":
        age = age + 1
    elif birthday == "Y":
        age
    else:
        print "Invalid value provided."
    
    date = datetime.datetime.now()
    year = date.year
    
    minus100 = 100 - age
    year100 = year + minus100
    
    for i in range(printNum):
        print "Hello %s! You will turn 100 years old in the year %d." % (name, year100)
        
    repeat = raw_input("Do you want to try again? Y or N: ")
    repeat = repeat.upper()

print "Good-bye!"
