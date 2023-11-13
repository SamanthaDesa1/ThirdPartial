https://replit.com/join/xdrblaqxvj-samanthadesaida

"""
Develop a program that calculates the percentage error of an LM35 temperature sensor in a laboratory. The program must detect and store raw data, ultimately displaying the percentage of times that the sensor gave values ​​outside the expected range (between 10 and 40 degrees Celsius).
"""

temp_lect = int(input("How many temperatures do you have?  "))
c = 0 
temp = 0 
error_sensor = 0 
while c < temp_lect:
  c += 1
  temp = float(input("Insert the temperture:  "))
  if temp >= 10 and temp <= 40:
    pass
  else: 
     error_sensor += 1

print(f"The number of incorrect values was: {error_sensor}")
percentage = error_sensor*100/temp_lect
print(f"The percentage of incorrect lectures was: {percentage}")
