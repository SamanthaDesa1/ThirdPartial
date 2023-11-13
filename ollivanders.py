https://replit.com/join/pfollvctfa-samanthadesaida

"""
Create a program that records the customers who enter a store and how many of them buy wands. 
You should record which customers bought which wands. The wand options are: 1. Elder Wand, 2. Hawthorn Wand, 3. Willow Wand, and 4. Holly Wand.
"""
counter = 0
number_of_wands = 0
elder =0
hawthorn =0
willow =0 
holly =0

client = input("Is there any client? please answer with yes/no  ")

while client == "yes":
  counter += 1
  wand = input("Has a wand been sold? yes/no  ")
  if wand == "yes":
    print("""
    1. Elder wand
    2. Hawthorn wand
    3. Willow wand
    4. Holly wand
    """)
    type_of_wand = input("What type of wand has been? please enter the number  ")
    if type_of_wand == 1:
       elder += 1
    elif type_of_wand == 2:
       hawthorn += 1
    elif type_of_wand == 3:
       willow += 1
    elif type_of_wand == 4:
       holly += 1
  client = input("Is there any client? please answer with yes/no  ")

print(f"The number of costumers that came in today was:{counter}")
print(f"Number of elder wands sold: {elder}")
print(f"Number of hawthorn wands sold: {hawthorn}")
print(f"Number of willow wands sold: {willow}")
print(f"Number of holly wands sold: {holly}")
