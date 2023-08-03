## Functions in Python
## Build-in-Functions line print(),len(),int() and so on

print("Hello") 
num_char=len("Hello")
print(num_char)

## We can also create our own functions and for defining the function we can use def() keyword followed by calling the function 

def my_function():                                              ##Defining the function
    print("Hello")
    print("Bye")

my_function()                                                   ## Calling the function

## Coding Challenge 1:
 
## https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
    
#def hurdles():
#    move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()
#for i in range(6):
#    hurdles()

## While Loops

# while something_is_true
   ## Do something repeatedly

## number_of_hurdles=6
#  while number_of_hurdles > 0:
#  hurdles()
#  number_of_hurdles-=1
#  print(number_of_hurdles)

## Challenge 2- Hurdle 2

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# while not at_goal():
#    hurdles()

## when to use for loop and when to use while loop

## Challenge 3: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
    
#def hurdles():
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()
   
#while not at_goal():
#    if wall_in_front():
#        hurdles()
#    else:
#        move()

## Challenge 4 


#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
    
#def hurdles():
#    turn_left()
#    while wall_on_right():
#        move()
#    turn_right()
#    move()
#    turn_right()
#    while  front_is_clear():
#        move()
#        turn_left()
            
#while not at_goal():
#    if wall_in_front():
#        hurdles()
#    else:
#        move()


      