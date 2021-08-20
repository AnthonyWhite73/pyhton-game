import random, time, sys
from typing import ClassVar
#set functions

#set color variables
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
purple = "\033[35m"
teal = "\033[36m"
blue = "\033[34m"
no_color = "\033[0m"

#colorful functions
def print_red(string_in):
    convertstring = str(string_in)
    return(red + convertstring + no_color)

def print_green(string_in):
    convertstring = str(string_in)
    return(green + convertstring + no_color)

def print_yellow(string_in):
    convertstring = str(string_in)
    return(yellow + convertstring + no_color)

def print_purple(string_in):
    convertstring = str(string_in)
    return(purple + convertstring + no_color)

def print_teal(string_in):
    convertstring = str(string_in)
    return(teal + convertstring + no_color)

def print_blue(string_in):
    convertstring = str(string_in)
    return(blue + convertstring + no_color)

#run script

#print("hello " + str(print_yellow("money")) + " " + print_red("strength") + " world!")

age = random.randint(1, 150)
print(f"You're " + str(print_yellow(age)) + f" years old! You don't look a day over {age - 5} ")
print("hello {}".format(age))

txt3 = "My name is {}, I'm {}".format("John", str(print_yellow(age)))
print(txt3)
