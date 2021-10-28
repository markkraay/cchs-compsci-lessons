# # Last week, we introduced to the basic concepts of datatypes through a
# # simple input / output example

# name = input()
# print(type(name))
# print(name)

# # If we want to get an integer
# number = int(input())
# print(number + 1)


# # These are great! But there's a lot more datatypes that are helpful
# # I am ending these variable names with a "_" because these names are RESERVED keywords in 
# # Python. Without the "_", we cannot use them as variable names
# bool_ = True
# print(type(bool_))

# float_ = 1.1231
# print(type(float_))

# set_ = {1, 2, 3} 
# print(type(set_))

# list_ = [1, 2, 3]
# print(type(list_))

# # Sets and maps both hold a collection of items. In sets however, there cannot be identitical items and 
# # for this reason, the order does not matter.

# # To eludicate the concept of lists and iteration, lets look at a how we can simplify a program using them.

# # Problem: Take 3 test scores as input and print the class average.

# # Solution: 
# score1 = int(input())
# score2 = int(input())
# score3 = int(input())
# print((score1 + score2 + score3) / 3)

# # Not many classes only have three students, so how would we handle this if there was, say, 10 students.

# # Solution

# num_students = 5
# total = 0
# for i in range(num_students):
# 	score = int(input("Enter your score: "))
# 	total += score
# print(total / num_students)

# # What if we want to remember the test scores so that we can look at them later

# # Introducing the LIST / ARRAY!
# scores = [] # Creating the array
# for i in range(num_students):
# 	score = int(input("Enter your score: "))
# 	scores.append(score)
# print(scores)

# # Final senario. What if we want to identify a student with their test score

# # Introducing the DICTIONARY!
# # A dictionary is collection of key: value pairs. We can use an item's key to get its corresponding value

# student_scores = {} # Creates a dictionary
# for i in range(num_students):
# 	name = input("Enter a student name: ")
# 	score = int(input("Enter their score: "))
# 	student_scores[name] = score
# print(student_scores)
# print(student_scores["Mark"])

# # Practice Problem:
# # Given an array of integers your solution should find the smallest integer.

# # For example:
# # Given [34, 15, 88, 2] your solution will return 2
# # Given [34, -345, -1, 100] your solution will return -345
