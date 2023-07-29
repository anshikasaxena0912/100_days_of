import random
import my_module      #We can also use our own modules in python

randon_integer=random.randint(1,100)     # To print any random integer between 1 to 100 including 1 and 100
print(randon_integer)

print(my_module.pi)

random_float=random.random()            # To print any random float no between 0 and 1 excluding 0 and 1
print(random_float)

random_Float=random.random() * 5        ## To print any random float no between 0 and 5
print(random_Float)


random_String=random.randint(0,1)    
if(random_String==0):
    print("Heads")
else:
    print("Tails")

#### Python Lists ####

#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary,
#  all with different qualities and usage.
#Lists are created using square brackets

states_of_america=["Delaware","Pennysylvania"]
print(states_of_america[0]) 
length1=len(states_of_america)
print(length1)  

states_of_america.append("South California")        # To append in the existing list
print(states_of_america)

## Create a list of friends and a random name will pay the bill

name=input("Enter the names of your friends seperated by comma ")
name_list=name.split(",")
print(name_list)
length=len(name_list)
print(length)
random_name=random.randint(0,length-1)
payee=name_list[random_name]
print(f"{payee} will pay the bill")

## random.choice 
## Instead of writing the above code we can simply make use of random.choice function

payee=random.choice(name_list)
print(f"{payee} will pay the bill")

## Index Out of Range Error

fruits=["apple","mango","banana"]
print(fruits[8])

#Traceback (most recent call last):
#  File "c:\Users\sriva\Desktop\Anshika Python\Day4.py", line 57, in <module>
#    print(fruits[8])
#          ~~~~~~^^^
#IndexError: list index out of range

#Since there is no value at index 8

#### Lists within a list- nested lists

fruits=["Strawberries","Apples","grapes","cherries"]
vegetables=["Spinach","Kale"]
#dirty_dozen=fruits+vegetables
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)
print(dirty_dozen[1])
print(dirty_dozen[1][1])

###########


row1=["😇","😀","😘"]
row2=["🥺","😜","🤤"]
row3=["🤑","😴","😑"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
treasure=input("Where do you want to put the treasure")
if(len(treasure)!=2):
    print("Please enter a 2 digit number to proceed ")
else:
    horizontal=int(treasure[0])
    vertical=int(treasure[1])
    map[vertical-1][horizontal-1]="X"
    print(f"{row1}\n{row2}\n{row3}")
    
######

#Rock paper scissors game


import random
import sys
me=int (input("Choose 0 for rock,1 for paper or 2 for scissors "))
if (0< me <3):
    print("Enter a value between 0 and 2")
    sys.exit()
game=["rock","paper","scissor"]
comp=random.randint(0,2)
print(f"computer selected {comp}")
if ( comp==me ):
    print("It is a tie")
elif (( comp==0 and me==2 ) or ( comp==1 and me==0 ) or ( comp==2 and me==1 )):
    print("computer wins")
else:
    print("You win")