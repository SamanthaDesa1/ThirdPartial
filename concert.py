https://replit.com/join/niwpsuftlc-samanthadesaida

"""
Cost per seat: Zone 1 - $2000, Zone 2 - $1000, Zone 3 - $700
Complimentary coupons per person: Platinum $500, Gold $300, Silver $200
Note 1: These coupons are valid only from Monday to Thursday.
The algorithm should request the following input: customer name, zone, day of the week, and the type of coupon for each attendee (if they have a coupon).
Note 2: The loop will end if there are no more customers to attend, so ask if there is another customer in line.
"""
counter = 0
tickets = 0

clients = input("Are there any clients? answer with yes/no  ").lower()

while clients == "yes":
  counter += 1
  name = input("What is your name?  ")
  print("""
  1. zone 1 - $2000 
  2. zone 2 - $1000
  3. zone 3 - $700
  """)
  zone = int(input(f"Which zone do you want, {name}? please enter the number  "))
  
  if zone == 1:
    tickets += 2000
    print("That will be $2000")
  elif zone == 2:
    tickets += 1000
    print("That will be $1000")
  elif zone == 3:
    tickets += 700
    print("that will be $700")

  
  coupon = input("do you have a coupon? yes/no  ").lower()
  day = input("What day are you going?  ").lower()
  if coupon == "yes":
    if day == "friday" or day == "saturday" or day == "sunday":
      print("sorry, the coupon isn't valid :(")
    else:
      print("""
      1. Platinum $500
      2. Gold $300
      3. Silver $200
      """)
      coupon_num = input("What coupon do you have?  ")
      if coupon == 1:
        tickets -= 500
      elif coupon == 2:
        tickets -= 300
      elif coupon == 3:
        tickets -= 200
  clients = input("Are there any clients? answer with yes/no  ").lower()

print(f"{name}, your total price was, ${tickets}")
print(f"the total number of clients was: {counter}")
print(f"the total income was: {tickets}")
