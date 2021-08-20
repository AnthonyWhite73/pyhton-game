#Challenge 1
password = "dogdogdog"
if len(password) < 8:
    print("This password is too short!")
else:
    print(password)
    print(f"Your password is {password}")
#Challenge 2
num = 101
if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")
#Challenge 3
num = 21
if num % 3 == 0 and num % 7 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(num)
#Challenge 4
word = "disappointed"
first_letter = word[0]
last_letter = word[-1]

if first_letter == last_letter:
    print(True)
else:
    print(False)
#Challenge 5
time = 18
place = "Manchester"
home = "Stockport"
if time < 8 or time > 18:
    print(f"I am in {home}")
elif time == 8 or time == 18:
    print("I am communting")
else:
    print(f"I am in {place}")
#Challenge 6
#Anthony's Version
num1 = 1
num2 = 2
num = num1+num2
if (num % 2) == 0:
    print("Success")
else:
    print("Try again!")
#Basil's Version
num1 = 45
num2 = 35
result = num1 + num2
print(str(num1) +" + "+str(num2)+ " = " +str(result))
if str(result)[-1] == "0":
    print("This is an even number")
if str(result)[-1] == "0":
    print(str(result) + " is an even number")
elif str(result)[-1] == "2": 
    print(str(result) + " is an even number")
elif str(result)[-1] == "4": 
    print(str(result) + " is an even number")
elif str(result)[-1] == "6": 
    print(str(result) + " is an even number")
elif str(result)[-1] == "8":
    print(str(result) + " is an even number")
else:
    print(str(result) + " is not an even number")
#Dave's Version
import random
num1 = random.randint(0,23)
num2 = random.randint(0,23)
num3 = num1 + num2
if num3 % 2 == 0:
    print(f"{num3} is even. Success")
elif num3 % 2 != 0:
    print(f"{num3} is odd. Try again")
else:
    print("")