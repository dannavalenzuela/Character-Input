# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import date

repeat = "Y"

while repeat == "Y":

    name = str(raw_input("Please enter your name: "))
    a = True
    while a is True:
        try:
            age = int(raw_input("What is your age? "))
            a = False
        except ValueError:
            print "That is an invalid value. Please enter a number as your age and try again."
    b = True
    while b is True:
        try:
            num = int(raw_input("Enter a number from 1-5: "))
            if num < 1 or num > 5:
                print "That is an invalid value. Please enter a number from 1-5 and try again."
            else:
                b = False
        except ValueError:
            print "That is an invalid value. Please enter a number as your age and try again."

    yearsto100 = 100 - age
    currentyear = date.today().year
    year100 = currentyear + yearsto100

    print num * "Hello {}, you will turn 100 years old in the year {}.\n".format(name, year100)
    c = True
    while c is True:
        repeat = raw_input("Do you want to try again? Y or N: ")
        if repeat == "Y" or repeat == "y" or repeat == "N" or repeat == "n":
            repeat = repeat.upper()
            c = False
        else:
            print "That is an invalid value. Please enter Y or N and try again."

print "Good-bye!"
