## Type Error
#print(len(12345))

## Data Types
#String

print("Hello"[0])      #Pull out a character from string
                       #Counting always start from 0
                       #As far as a double quote is there it is always treated as a string Ex: "123" is a string not a number

#Number
#Integers

print(123+345)         #It will print the sum of two numbers

#Float
#3.14

#Boolean
#It is either True or False

###############################################3
#Type Casting

num_char=len(input("Enter your name? "))
print(type(num_char))
new_num_char=str(num_char)
print("Your name has " +new_num_char +" charaters")

print(70+float("100.7"))

## Adding of numbers

a = input("Enter a number?")
print(int(a[0]) + int(a[1]))

print(3*(3+3)/3-3)

## BMI calculator 

weight=input("Enter the weight? ")
height=input("Enter the height in metres? ")

bmi=float(weight)/float(height)**2
print(bmi)

print(round(8/3 ,2))    #Round off a number in Python

## f-String in Python

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height} , you are winning is {isWinning}")

##
total_years=90
age = int(input("What is your current age? "))

remaining_years=total_years-age
remaining_days=365*remaining_years
remaining_months=remaining_years*12
remaining_weeks=52*remaining_years
print(f"you have {remaining_years} years,{remaining_months} months,{remaining_weeks} weeks, {remaining_days} days remaining :(")


## Building a Tip Calculator

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give?10,12 or 15 "))
tip_total=bill*(tip/100)
split = int(input("How many people to split the bill"))
pay=(bill+tip_total)/split
print(pay)