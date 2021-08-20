correct_pin = 1212
customer_balance = 100

def valid_pin(pin):
    if pin != correct_pin:
        return False
    else:
        return True

def new_balance(amount):
    return customer_balance - amount

def cash_machine():
    pin = int(input("Please enter your PIN\n"))
    
    if valid_pin(pin) == False:
        print("Wrong PIN dummy")        
    else:
        print("Correct PIN")
        amount = int(input("Enter the amount you want to withdraw\n"))
        
        new_balance1 = customer_balance - amount
        if new_balance1 >= 0:
            print("Dispensing cash")
            print(f"New balance is {new_balance1}")
        else:
            print("not enough cash, cheap skate!")

cash_machine()