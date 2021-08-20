#This code makes a nested list (a list of lists) that populates it with records for #three characters'''

#a character will have:
#name (A string)
#age (an integer)
#gender (true false for male female)
#health points (an integer)
#weapon (list/function that returns a damage die)
#armour (integer)
#dead (boolean)

#7 fields of data in total so 7 columns
#will try 3 characters, so 3 rows

#element indexes will be:
#0=name, 1=age, 2=gender, 3=health points, 4=weapon, 5=armour, 6 = dead

#so list of lists for three characters

def bark(textIn):


 print("ADMIN MESSAGE -----> "+textIn)

bark("Beginning program!")

charList = [
    ["Name","Age","Is Male?", "Hit Points", "Weapon", "Armour", "Is Dead?"],
    ["Stealy the Thief", 13, False, 10, "Dagger", 3, False],
    ["Lenny the Idiot", 32, True, 30, "Sledgehammer", 5, False],
    ["Shooty the Murderer", 25, False, 20, "Gun", 4, False],
]

#foundChar is set to true when callled in the function 'spitCharData'
foundChar = False
#charChosen is set to true when the while loop confirms the user has picked a character
charChosen = False
charChosenIndex = 0

while charChosen == False:
    charSel = input("Choose your character: 'Stealy the Thief', 'Lenny the Idiot' or 'Shooty the Murderer'\n")
    if charSel != "Stealy the Thief" and charSel != "Lenny the Idiot" and charSel != "Shooty the Murderer":
        print("\n-----------------------------------------------------------------------")
        print("You did not choose a character with the proper name. Please try again.")
        print("-----------------------------------------------------------------------\n")

    elif charSel == "Stealy the Thief":
        charChosenIndex = 1
        charChosen = True

        print("You have chosen " +charSel+".")
        print("Let us begin...\n")

    elif charSel == "Lenny the Idiot":
        charChosenIndex = 2
        charChosen = True        
        print("You have chosen " +charSel+".")
        print("Let us begin...\n")

    elif charSel == "Shooty the Murderer":
        charChosenIndex = 3
        charChosen = True  
        print("You have chosen " +charSel+".")
        print("Let us begin...\n")

    else:
        print("Something went wrong :(")


#element indexes will be:
#0=name, 1=age, 2=gender, 3=health points, 4=weapon, 5=armour, 6 = dead

#Function to spit out all character data from the input one (determined by while loop above)
def spitCharData(input):
    global isMale
    global isDead
    global foundChar
    index = int(input)

    #va
    isMale = charList[input][2]
    isDead = charList[input][6]

    while foundChar == False:
        if charSel == charList[index][0]:
            for i in range(0,7):
                print(str(charList[0][i]) + ": " + str(charList[input][i]))
                foundChar = True
        else:
            print("Bad juju... so breaking out of loop")
            break

spitCharData(charChosenIndex)