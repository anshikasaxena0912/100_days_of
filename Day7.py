import random
word_list=["Mouse","Rat","Cookie","Badmaswa"]

chosen_word=random.choice(word_list)
print(chosen_word) #mouse
word_length=len(chosen_word)#5
blank=["_"]*word_length
print(blank)

counter=0
while counter < word_length: #0 is less than 5
    guess=input("Guess a letter in a word? ")
    guess1=guess.lower() #o
    counter+=1
    for i in range(word_length): #5 mean it will go from 0 to 4counter
        if chosen_word[i] == guess1: #mouse [0]=o
            blank[i]=guess1
            print("in if block")

        else:
            print("Wrong attempt")
        print(blank)        
-------------------

import random

word_list = ["Mouse", "Rat", "Cookie", "Badmaswa"]

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
blank = ["_"] * word_length
print(blank)

counter = 0
while counter < word_length:
    guess = input("Guess a letter in a word? ")
    guess1 = guess.lower()
    counter += 1
    for i in range(word_length):
        if chosen_word[i] == guess1:
            blank[i] = guess1
            print("in if block")
    
    print("Wrong attempt")
    print(blank)

