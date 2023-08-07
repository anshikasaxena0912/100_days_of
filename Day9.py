# Python Dictionary

#  {Key:Value}

family={
    "anshika":"a cute girl",
    "arjit":"badmaswa papa",
    "cutie":"our princess"
}
print(family)

# Retrieving Items from Dictionary

print(family["anshika"])    
print(family["cutie"])
print(family["arjit"])

#Add new items in Dictionary

family["sheru"]="a teacup doggo"
print(family["sheru"])

# Create a empty Dictionary

full_family={}

# Wipe an existing Dictionary

#family={}
#print(family)

#Edit an Item in Dictionary

family["arjit"]="cutu papa"
print(family["arjit"])

# Loop through Dictionary

for thing in family:
    print(thing)

for key in family:
    print(key)

    print(family[key])

#Program 1:

# convert scores into grade

student_scores={
    "Harry":81,
    "Ron":78,
    "Hermoine":99,
    "Draco":74,
    "Neville":62
}

student_grades={}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)

# Nesting

#{
#    Key:[List],
#    Key2:{Dictionary}
#}

### Nesting

capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

#### Nesting a List in a Dictionary

travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg"]
}

## Nesting Dictionary In a Dictionary

travel_log = {
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visisted":["Berlin","Hamburg"],"total_visits":5}
}

#### Nesting Dictionary Inside the List

travel_log = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
        },
    {
        "country":"Germany",
    "cities_visisted":["Berlin","Hamburg"],
    "total_visits":5}
]


####Coding Exercise 2

travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    }
]

def add_new_country(country,visits,cities):
    new_country = {}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["cities"]=cities
    travel_log.append(new_country)
add_new_country("Russia",2,["Moscow","Saint_Perl"])
print(travel_log)


# 

import os
bid={}

def find_highest_bidder(bid):
     highest_bid=0
     winner=""
     for bidder in bid:
               bid_amount=bid[bidder]
               if bid_amount > highest_bid:
                     highest_bid=bid_amount
                     winner=bidder
                     print(f"The winner is {winner} with a bid of $ {highest_bid}")
          
bidding_finished = False
while not bidding_finished :
        name=input("Enter your name ")
        price=int(input("Enter your bid "))
        bid[name]=price
        cont=input("Do you wish to continue?").lower()
        if cont == "no":
            bidding_finished = True
            find_highest_bidder(bid)
        elif cont == "yes":
            os.system('cls')
            