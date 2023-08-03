def greet():
    print("Hello Good Morning")
    print("how are you")
    print("Love u kichu")


greet()    

#Functions with Inputs:
def greet_name(name):
    print(f"hello {name}")

v=input("enter your name")


greet_name(v)


def employee_info(name,age,contact):
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My contact number is {contact}")

name=input("Enter your name")
age=input("Enter your age")
contact=input("Enter you contact number")

employee_info(name,age,contact)

## Function with Multiple inputs

def info(name,location):
    print(f"My name is {name}")
    print(f"I am from {location}")

n=input("Enter your name? ")
l=input("Enter you location? ")

info(n,l)

## Program 1

test_h=int(input("Height of the wall: "))

test_w=int(input("Width of the wall: "))

coverage=5
def paint_calc(height,width,cover):
    no_of_cans=(height*width)/cover
    need_to_buy=round(no_of_cans)
    print(f"You need to buy {need_to_buy} cans to paint")

paint_calc(height=test_h,width=test_w,cover=coverage)

## Program 2 :Check whether number is prime or not

n=int(input("Check this number: "))

def prime_checker(number):
    prime=True
    for i in range(2,number):
            if number % i == 0 :
                prime=False
    if(prime==False):
         print("It's not a prime number")
    else:
         print("It's a prime number")

prime_checker(number=n)

## Final = Caesar Cipher Task

should_continue=True
while should_continue:
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n ")
    text=input("type your message:\n ").lower()
    shift=int(input("Type your shift number:\n"))
    val=""
    def caeser(direction,text,shift):
        cipher_text=""
        plain_text=""
        for letter in text:
            position=alphabet.index(letter)
            if(direction=="encode"):
                new_position=position+shift
                new_letter=alphabet[new_position]
                cipher_text +=new_letter
                val=cipher_text
            else:
                new_position1=position-shift
                new_letter1=alphabet[new_position1]
                plain_text +=new_letter1
                val=plain_text
            
        print(f"The {direction} message is {val}")
    caeser(direction,text,shift)
    
    cont=(input("Do you wish to continue? "))
    if cont=="no":
        should_continue=False
        print("User do not wish to continue")











