"""
Problem statement: Design a simple calculator with basic arithmetic operations. 
Prompt the user to input two numbers and an operation choice. 
Perform the calculation and display the result.
"""

#functions for different operations
def add(x,y):
    return x+y #addition
def subtract(x,y):
    return x-y #subtraction
def multiply(x,y):
    return x*y #multiplication
def quotient(x,y):
    return x/y #division with quotient
def remainder(x,y):
    return x%y #remainder of division

#welcoming statement
print(f"Welcome to calculator. \nRules are simple: select two numbers, choose an operator and find the result.")
print(f"Enter 1 for addition. \nEnter 2 for subtraction. \nEnter 3 for multiplication. \nEnter 4 for division.")

#for n number of trials
while True:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    choice = int(input("Enter the choice of operation: "))

    if choice == 1:
        sum = add(num_1,num_2)
        print(f"Sum of {num_1} and {num_2} is {sum}.")
    elif choice == 2:
        diff = subtract(num_1,num_2)
        print(f"Difference of {num_1} and {num_2} is {diff}.")
    elif choice == 3:
        prod = multiply(num_1,num_2)
        print(f"Product of {num_1} and {num_2} is {prod}.")
    elif choice == 4:
        quo = quotient(num_1,num_2)
        rem = remainder(num_1,num_2)
        print(f"Quotient of {num_1} and {num_2} is {quo}. Remainder is {rem}")
    else:
        print("Enter valid operator choice. Try again.")

    con = input('Do you want to continue? Enter yes or no: ').lower()
    if con == 'yes':
        print('Okay, please enter the numbers.')
    elif con == 'no':
        print("Thanks for using this calculator!")
        break
    else:
        print('Invalid input. Enter yes or no')
    