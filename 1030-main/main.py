# Importing the module
import calculator

print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_num = float(first_input)
second_num = float(second_input)

# Replace the operation and print statment with the calculator module created
if operation == "divide":
    result = calculator.divide(first_num, second_num)

elif operation == "multiple":
    result = calculator.multi(first_num, second_num)

elif operation == "add":
    result = calculator.add(first_num, second_num)

elif operation == "subtract":
    result = calculator.sub(first_num, second_num)

else:
    print("Sorry, I do not understand your request.")

# print result
print(f"Result of input is equal to: {result}")