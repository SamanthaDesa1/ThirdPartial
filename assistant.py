https://replit.com/join/sjjkxliyun-samanthadesaida

"""
Write a program that detects if 'Alexa' is written in a text. If you type more than once, the program should respond "Hey, just say my name once." Tip: use the split() functions to separate the text and count() to identify the times Alexa says.
"""

x = input("Write the name:")
y = x.split()
counter = y.count("alexa")
if counter == 1:
  print("Tell me, how can I help you?")
elif counter > 1:
  print("Hey, just say my name once :(")
  
