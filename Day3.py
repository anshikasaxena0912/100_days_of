#Conditional Statements
# if-else statements

####
#if condition:
#    do this
#else:
#    do this
####

print("Welcome to the rollercoaster")
height=int(input("Enter the height in cm? "))
if(height<=120):
    print("You can't ride")
else:
    print("You can ride")

####

print("Check whether number is odd or even")
num=float(input("Enter the number? "))
if(num%2==0):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

####

#### nested if-else statement

####
#if condition:
#    if another condition:
#       do this
#    else:
#        do this
#else:
#    do this


print("Welcome to the rollercoaster")
height=int(input("Enter the height in cm? "))
if(height>=120):
    print("You can ride")
    age=float(input("What's your age? "))
    if(age>=7):
        print("Kindly pay 18$")
    else:
        print("Kindly pay 7$")
else:
    print("You can't ride")

## if/elif/else

#if condition1:
#    do this
#elif condition2:
#    do this
#else:
#    do this

####

print("Welcome to the rollercoaster")
height=int(input("Enter the height in cm? "))
if(height>=120):
    print("You can ride")
    age=float(input("What's your age? "))
    if(age<12):
        print("Kindly pay 5$")
    elif 12 <= age < 18:
        print("Kindly pay 7$")
    else:
        print("Kindly pay 12$")
else:
    print("You can't ride")

####

print("Let's calculate your BMI")
height=float(input("Enter your height in m? "))
weight=float(input("Enter your weight in kg? "))
bmi=round(weight / height**2)
print(f"Your BMI is {bmi}")
if(bmi<18.5):
    print("You are underweight")
elif(18.5 <= bmi <25):
    print("Congratulations you have a normal weight")
elif(25 <= bmi <30):
    print("Sorry,you are overweight")
elif(30 <= bmi <35):
    print("Really sorry you are obese")
else:
    print("You need to take care since you are clinically obese")

####

year=int(input("Enter the year? "))
if((year%4==0) & (year%100!=0) | (year%400==0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

####

print("Welcome to Anshika's Pizza Store! You can now select your order.")
size = input("Please select if you want a S, M, or L pizza: ")
pepperoni=input("Do you want to add pepporoni:Y or N? ")
extra=input("Do you want extra cheese:Y or N? ")
if (size=="S"):
    bill=15
elif(size=="M"):
    bill=20
else:
    bill=25
if pepperoni == "Y" and (size == "S" or size == "M"):
    bill += 2
elif pepperoni == "Y" and size == "L":
    bill += 3


if extra == "Y":
    bill += 1
print(f"the total bill is{bill}")

####

print("Welcome to Love Calculator \n")
name=input("Enter your name \n")
name1=input("Enter your partner's name \n")
a=name+name1
b=a.lower()
count=0

t=b.count("t") + b.count("r") + b.count("u") + b.count("e")
l=b.count("l") + b.count("o") + b.count("v") + b.count("e")

love_percentage=(t*10)+l
print(f"your love percentage is {love_percentage}")

if(10 > love_percentage <90):
    print(f"Your score is {love_percentage},you go together like coke and mentos")
elif(40 < love_percentage <50):
    print("You are alright together")
else:
    print("You don't need this bullshit game to decide your love")

#### Final Project

print("Welcome to Treasure Island \n")
print("Your mission is to find the treasure \n")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

a=input("Do yo want to go left or right? ")
if(a=="left"):
    b=input("Do you want to swim or wait? ")
    if(b=="wait"):
        c=input("Which door:red,blue or yellow? ")
        if(c=="yellow"):
            print("You win")
        else:
            print("Game Over")
    else:
        print("Game Over")
        
else:
    print("Game Over")