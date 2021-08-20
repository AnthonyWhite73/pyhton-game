pos1 = "1"
pos2 = "2"
pos3 = "3"
pos4 = "4"
pos5 = "5"
pos1 = "X"
pos2 = "O"
pos3 = "X"
pos4 = "X"
pos5 = "X"
print("     |     |     |     ")
print("  "+pos1+"  |  "+pos2+"  |     |     ")
print("     |     |     |     ")
print("=======================")
print("     |     |     |     ")
print("  "+pos3+"  |  "+pos4+"  |     |     ")
print("     |     |     |     ")
print("=======================")
print("     |     |     |     ")
print("  "+pos5+"  |     |     |     ")
print("     |     |     |     ")

if pos1 == "X" and pos2 == "X" and pos3 == "X":
    print("X wins!")
elif pos1 == "O" and pos2 == "O" and pos3 == "O":
    print("O wins!")
else:
    print("no winner!")

# cinema ticket machine
child = "Ticket price: £8"
adult = "Ticket price: £10.95"
senior = "Ticket price: £7.50"

age = 60
if age <18:
    print(child)
elif age >= 60:
    print(senior)
else:
    print(adult)



def grind_beans():
    print("Grinding for 20 seconds")

grind_beans()

def withdraw(amount, account):
    print(f"Withdrawing {amount} from account {account}.")

withdraw(8, 123456789)

def drink_order(size, type_of_drink):
    print(f"You ordered a {size} {type_of_drink}, enjoy!")

drink_order("Large", "Cappuccino")


w_ammount = 100
account_n = 123456789
def withdraw(amount, account):
    print(f"Withdrawing {amount} from account {account}.")

withdraw(w_ammount, account_n)
withdraw(50, 123456789)

def add_up(num1, num2):
    return num1 + num2

print(add_up(2,5))

def process_1(celsius):
    return celsius * (9/5)

def process_2(celsius):
    return process_1(celsius) + 32

print(f"The temperature today is {process_2(20)} degrees fahrenheit")

#input function

def question():
    response = input("are you alive?\n")
    if question == "yes":
        print("Yay!")
    else:
        print("That's a shame...")

question()

