#students = [
#    "basil",
#    "anthony",
#    "dave",
#    "mohammad"
#]

#for name in students:
#    print(name)

# Activity 1
fav_films = [
    "Carlito's Way",
    "Starwars",
    "Ghostbusters",
    "TopGun"
]

for film in fav_films:
    print(film)

def film_check():
    #for film in fav_films:
    if fav_films[2] == "Ghostbusters":
        print("Yay it’s Ghostbusters!")
    else:
        print("Boo, we want Ghostbusters")

film_check()

# Activity 2

numbers = [
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
    "1",
    "0"
]

numbers2 = []

for i in range(0,10):
    numbers2.append(i)

def reverse_num():
    numbers2.reverse()
    print(numbers2)

reverse_num()

for i in reversed(fav_films):
    print(i)

# while loops
num = 0

#while num <10:
#    num += 1
#    print(num)

import random
rand_num = random.randint(0,50)
my_num = 50

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,50)

print(f"You've found {my_num}!")

