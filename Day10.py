## Functions with Outputs
## Building a Calculator App

## Convert string to Title case

f_name=input("Enter the first name? ")
l_name=input("Enter the last name? ")

def format_name(f_name,l_name):
    f=f_name.title()
    l=l_name.title()
    t=f+" "+l
    return t

output=format_name(f_name,l_name)
print(output)

## Return always tell that its the end of function

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return True
        else:
            return False
        
def days_in_month(year,month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap=is_leap(year)
    monthval=month-1
    if year == True:
        month_days[1]=29
        return month_days[monthval]
    else:
        return month_days[monthval]
                

year = int(input("Enter a year: "))
month= int(input("Enter the month: "))
days = days_in_month(year,month)
print(days)

##Docstrings

## Calculator

# Add

def add(n1,n2):
    return n1+n2

# Subtract

def subtract(n1,n2):
    return n1-n2

# Multiply

def multiply(n1,n2):
    return n1*n2

# Divide

def divide(n1,n2):
    return n1/n2

# Create a dictionary

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calculator():
    num1=float(input("Enter the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:

        
        operation_chosen=input("Pick an operation  ")
        num2=float(input("Enter the next number? "))
        calculation_function=operations[operation_chosen]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_chosen} {num2} = {answer}") 

        cont=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation ")
        if (cont == "y"):
            num1 = answer
        else:
            should_continue=False
            calculator()
            