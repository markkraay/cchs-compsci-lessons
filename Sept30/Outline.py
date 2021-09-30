# Basics of Programming
# PYTHON

# When we are writing software, the fundamental testing ground for our applications
# is the terminal. This was what computers were first like! Apple really
# revolutionized the computer into what it is today with Graphical User Iterfaces
# (GUIS) and the mouse.

# OUTPUT: Printing basic text to the screen
#print("Hello World!")

# Printing numbers to the screen
#print(123)

# VARIABLES: Remember the values we store in them, they are like little boxes that
# remember the values we put inside of them
# We want to pick something descriptive for our variables, rather than
# arbitrary combinations of letters. When you revisit your code months later,
# you want to be able to understand what you were doing!

#greeting = "Hello World"
#number = 123
#print(greeting)
#print(number)

# INPUT: Reading user submitted information (text, button presses, mouse movements).
# This input often determines how our program will execute

# We have to read our input into a variable, so the program can remember it.
number = input("Enter an number: ")
print(number)

# Now lets try to add one to the number
increment_value = 5
#print(number + increment_value)

# Our program crashed!
# First, lets analyze what the computer is telling us.
# It actually tells us what the error line the error was and the actual instruction
# our program was executing when the program errored out.
# Furthermore, this output even gives us a hint at what might be the problem with
# with the instruction we were trying to execute: "Cannot concatenate str (not int) to int"

# The next logical question is what is str and int, and what does contenate mean!

# DATA TYPES:
# First, let's look at some C code to help us understand what datatypes are.
# Notice, the data types
# Python abstracts away these datatypes, making it easier for us programmers to g
# simple tasks done, that often don't require the performance boost that C code offers
# However, as Python programmer, although we are not deliberately telling the program what 
# data types are variables are, we need to be aware of our variables datatypes so that we don't
# encounter errors like the one we did above.

# So, lets analyze the our variables datatypes
#print(type(number)) # Result in 'str'
#print(type(increment_value)) # Results in 'int'

# So when we got that error, Python was telling us we cannot add, or use the '+' operator, 
# which we will get into later, on arugments of 'str' and 'int'
# We can fix this by changing our datatype in our input statement to an int 

# Since, we just introduced the idea of operators, now would be a good time to do some 
# math in the terminal

# Now, since we understand some basic input / output operations and a little about datatypes, lets
# all work together to make our first program
# In this program, we will
# 1) Read in the name of three companies and their stock prices
# 2) Output the their names in table format and show the total and each stocks percentage of the total

# Now, let's introduce some complexity into our program
# What if you wanted to find the stock with the highest price
# This is were we introduce conditionals
# if stock1_price > stock2_price:
#   print(stock1_price)

# and what if we want to read in more than three prices!
# we need some sort of way to store our variables dynamically and we need some sort of looping mechanism to read
# a variable amount of inputs
