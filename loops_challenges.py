# Activity 1
# Create a loop that print "hello world" 13 times
for i in range(1, 14):
    print(f"hello world {i}")

# Convert into a while loop
num = 1
while num < 14:    
    print(f"hello world {num}")
    num += 1

# Activity 2
# Create a variable
# use a loop to generate a random number between 1 and 30 six times
# check if the number is divisible ny 7 or not
import random

rand_num = random.randint(1,30)
for i in range(6):
    rand_num = random.randint(1,30)
    if rand_num % 7 == 0:
        print(f"{rand_num} is divisible by 7")
    else:
        print(f"{rand_num} is not divisible by 7")

# Activity 3
# Create a while loop to randomly cycle through a list of cards
# until a given suit is reached
import random

cards = ["Diamond", "Spade", "Club", "Heart"]
current_card = random.choice(cards)
wanted_card = "Heart"

while current_card != wanted_card:    
    current_card = random.choice(cards)
    print(current_card)

print(f"You've found {current_card}!")