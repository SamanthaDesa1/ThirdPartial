https://replit.com/join/vdczizjhde-samanthadesaida

#Student
print("Did you study for the math exam? Answer yes/no")
study = input()
print("Did you pay attention to class? Answer yes/no")
attention = input()

print("Subjects")
print("1. 2. Piecewise Functions, 2. Logarithmic Functions, 3. Exponential and Logarithmic models")
print("Write the number of the topic you find the easiest")
easy = int(input())
print("Write the number of the topic you found the most difficult")
difficult = input()

if study == "yes" and attention == "yes":
  print("Research in books for the things you don't understand")
  print("Ask Chris for extra sessions")
  print("Make a study group, that can also help :)")
elif study =="no" and attention == "yes":
  print("Study!!!") #just in case :)
elif study == "yes" and attention == "no":
  print("Pay attention in class!!")

if difficult == "1":
  print("Looks like your struggling with Piecewise Functions")
  print("Start with the basics and start building your way up")
elif difficult == "2":
   print("Looks like your struggling with Logarithmic functions")
   print("Try to understand the formula of the logarithms, so the you can understand the complex ones")
elif difficult == "3":
   print("Looks like your struggling with Exponential and Logarithmic models")
   print("I recommend you to try and watch some videos")
