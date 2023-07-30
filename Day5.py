#Loops

#for Loop

fruits=["Apple","Mango","Strawberry"]                               
for fruit in fruits:                                       #Loops allows us to execute whole block of statements multiple times
    print(fruit)
    print(fruit + "Pie")                                   #Inside the for Loop
print(fruits)                                              #Outside the for Loop
                                                           #Indentation is really important
####
#Calculate average height of student from a List of heights
##You can't use len() and sum() functions

height=input("Enter the height of students? ").split()
for n in range(0,len(height)):
    height[n]=int(height[n])
print(height)
total_height=0
count=0
for h in height:
    total_height=total_height+h
    count=count+1
avg=total_height/count

print(f"the average of {count} student's height is {avg}")

####

#Highest score from the list of score of students in class

student_scores=input("Enter the list of students scores ?").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
highest_score=0
for score in student_scores:
    if(highest_score<score):
        highest_score=score
print(f"The highest score is {highest_score}")

#### For Loop with Lists ####
## Range Function 

for number in range(1,10):                              #It will not include 10
    print(number)

for n in range(1,11,3):                                 # 3 is the step
    print(n)

# Print the sum of numbers from 1 to 100
    
sum=0
for n in range(1,101):
    sum=n+sum
print(f"The sum of all numbers between 1 to 100 is {sum}")

# Sum of Even numbers

sum=0
for n in range(2,101,2):
    sum=n+sum
print(f"The sum of Even numbers between 1 to 100 is {sum}")

#FizzBuzz Exercise

for n in range(1,101):
    if  n % 3 == 0 &  n % 5 == 0 :
        print("FizzBuzz")
    elif n % 3 == 0 :
        print("Fizz")
    elif  n % 5 == 0:
        print("Buzz")
    else:
        print(n)

## Final Project of Day:pyPassword Generator####

##Easy Level

import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','#','$','%']
print("Welcome to Pypassword Generator")
nr_letters=int(input("How many letters would you like in password\n "))
nr_symbol=int(input("How many symbols would you like in password\n "))
nr_number=int(input("How many numbers would you like in password\n "))

password=""
for l in range(1,nr_letters+1):
    let=random.choice(letters)
    password+=let
for s in range(1,nr_symbol+1):
    sym=random.choice(symbol)
    password+=sym
for n in range(1,nr_number+1):
    num=random.choice(number)
    password+=num

print(password)

## Hard Level

import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','#','$','%']
print("Welcome to Pypassword Generator")
nr_letters=int(input("How many letters would you like in password\n "))
nr_symbol=int(input("How many symbols would you like in password\n "))
nr_number=int(input("How many numbers would you like in password\n "))

password=[]
for l in range(1,nr_letters+1):
    let=random.choice(letters)
    password.append(let)
for s in range(1,nr_symbol+1):
    sym=random.choice(symbol)
    password.append(sym)
for n in range(1,nr_number+1):
    num=random.choice(number)
    password.append(num)

random.shuffle(password)
print(password)

new_pass=""
for p in password:
    new_pass=new_pass+p
print(f"The complex password in hard way is {new_pass}")    