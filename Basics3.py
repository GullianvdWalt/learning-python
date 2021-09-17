# Functions

# Void function
# def printMessage(msg):
#     print("Message: ", msg)
# printMessage("Hello there")

# def getSum(num1, num2):
#     return num1 + num2
# print("The sum is: ", getSum(10, 10))

# Lambda Functions ~ Small anonymous function, can take parameters but can only have one expression
# x = lambda a, b, c:((a + 5) + b ) * c
# print(x(5, 5 ,6))
#####################################################################################################

# Conditionals
# If statement

# def calculate(num1, num2, type):
#     if(type == 0): return num1 + num2
#     elif(type == 1): return num1 * num2
#     elif(type == 2): return num1 - num2
#     elif(type == 3): return num1 / num2

# print("Sum: ", calculate(10, 20, 0))
# print("Multiply: ", calculate(10, 20, 1))
# print("Difference: ", calculate(10, 20, 2))
# print("Divide: ", calculate(10, 20, 3))
#####################################################################################################

# User Input
# def displayMsg(msg):
#     print("Yout message: ", msg)
# userInput = input("Enter your message: ")
# displayMsg(userInput)
#####################################################################################################

# Parsing
# print(float('7'))
# print(str(7))
# print(int('7')) 
#####################################################################################################

# Append varialbes in string
# userInput = input("Enter yout name: ")
# message = "Hello %s " % userInput
# message = f"Hello {userInput}"
# print(message)

# Multiple variables
# userName = input("Enter yout name: ")
# userSurname = input("Enter yout surname: ")
# message = "Hello %s %s " % (userName, userSurname)
# message = f"Hello {userName} {userSurname}"
# print(message)