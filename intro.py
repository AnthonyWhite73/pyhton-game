import random
for i in range(10):
    print (i)
    #This is a comment
    print(f"Hello World {i}")
    #Another comment
    

print(len("antidisestablishmentarianism"))
print("hello".capitalize())

print(random.random())
print(random.uniform(1, 10))

print(random.randint(1, 10))

print("     I     I")
print("     I     I")
print("     I     I")
print("----------------")
print("     I     I")
print("     I     I")
print("     I     I")
print("----------------")
print("     I     I")
print("     I     I")
print("     I     I")

print ("hello".upper())
# .upper() Converts a string into upper case
print ("hello".lower())
# .lower() Converts a string into lower case
print ("hello".capitalize())
# .capitalize() Converts the first character to upper case
print ("hello".count("l"))
# .count() Returns the number of times a specified value occurs in a string
print ("hello".find("o"))
# find() Searches the string for a specified value and returns the position of where it was found
print ("hello".replace("h","f"))
# .replace() Returns a string where a specified value is replaced with a specified value
print ("   hello   ".strip())
# .strip() Returns a trimmed version of the string


print("All Around the World" [7].upper())
# more efficient

print("All Around the World".upper() [7])
# uppercase it all at first, less efficent

my_name = "Anthony"
fav_Sport = "football"

print("My name is {} and my favorite sport is {}".format(my_name, fav_Sport))

print(f"My name is {my_name} and my favorite sport is {fav_Sport}")
# f string
# more updated way to do it

my_new_name = input("What is your name? \n")
print(f"Pleased to meet you {my_new_name}")

x = 5%3
# modular
print(x)

y = 5**3
# to the power of
print(y)

i = 27
i += 34
print(i)