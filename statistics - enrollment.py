https://replit.com/join/abbemeijnw-samanthadesaida

#Samantha Desaida Sánchez   A00573926
#María Fernanda Hidalgo Hernandez   A00573839
#Nur Torres García  A00574487
"""
Create an algorithm to obtain statistics in a zoo where a count and percentage of “n” animals within a certain age range is required:
Less than 2 years
Between 2 and less than 5 years
Between 5 and less than 10 years
Greater than or equal to 10 years

The diagram should ask as input: if there is another animal to be recorded (yes/no response), the age (years) of each one. Tip: use the lower function to validate yes and no
The output must specify the number and percentage of animals in each age range.
"""

counter = 0
less_2 = 0
age2_5 = 0
age5_10 = 0
age10_higher = 0

animals = (input("Are there any animals to be recorded? please answer yes/no  "))

while animals == "yes":
  counter += 1
  age = int(input("How old is the animal?  "))
  if age < 2:
    less_2 += 1
  elif age == 2 and age < 5:
    age2_5 += 1
  elif age == 5 and age < 10:
    age5_10 += 1
  elif age == 10 and age > 10:
    age10_higher += 1
  animals = input("Are there any animals to be recorded? please answer yes/no  ")

print(f"the number of animals recorded was: {counter}")
percentage_2 = less_2*100/counter
print(f"the percentage of animals younger than 2 years is: {percentage_2}")
percentage_5 = age2_5*100/counter
print(f"the percentage of animals between 2 years and 5 years is: {percentage_5}")
percentage5_10 = age5_10*100/counter
print(f"the percentage of animals between 5 years and 10 years is: {percentage5_10}")
percentage_10 = age10_higher*100/counter
print(f"the percentage of animals that are 10 years or older is: {percentage_10}")
