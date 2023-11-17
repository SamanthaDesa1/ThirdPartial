https://replit.com/join/wkuisyczlf-samanthadesaida

"""
Using the randint() function, generate a number between 1 and 10.

Create a game whose goal is to guess the generated number in less than 3 attempts. You need a loop to ask for the number; if the number is guessed, exit the loop, or if the 3 chances are exhausted.

In the end, you should report whether it was successful and in how many attempts or if it was lost.

Note: Place this instruction at the beginning of your program:

     from random import randint
"""

from random import randint

random = randint(1,10)
chances = 3
tries = 0
number = 0

print("Guess the number from 1 to 10")
while tries < chances:
  tries = float(input("Try to guess:  "))
  tries += 1

if tries == number:
  print("Congrats! you guessed the number")
else:
  print("sorry try again :(")
tries = float(input("Try to guess:  "))

if tries == number:
  print("Congrats! you guessed the number")
else:
  print("sorry try again :(")
tries = float(input("Try to guess:  "))
if tries == number:
  print("Congrats! you guessed the number")
else:
  print("sorry try again :(")
tries = float(input("Try to guess:  "))

if tries == chances:
  print("sorry, your chances are over")
