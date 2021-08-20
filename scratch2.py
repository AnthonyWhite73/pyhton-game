#need to figure out how to handle events in the game

#event should be randomized, so choose them by an index [CAN BE DONE EASILY]
#event should spit out some dialogue, informing the player of what happens [DONE]
#a challenge should be issued to the player [DONE THROUGH DIALOGUE]
#player should then be given multiple options on how to handle it 
#whichever choice is made, a dice roll must be done to try and succeed at it.

#===========================================================================================================================================
#IMPORTS
import random

#===========================================================================================================================================
#VARIABLE DECLARATIONS
rollResult = 0

charList = [["The Player", 33, 50, "Protagonist", 1, 2, False, 5, 3, 3],
            ["The Strongman", 40, 30, "Strongman", 1, 2, False, 5, 1, 3]]

eventsList = [
    ["ID", "Event Name", "Dialogue 1", "Dialogue 2","Dialogue 3", "PLAYER CHOOSES AN OPTION"],
    [1,"Strongman", 
        "You see a well built man. He sees you and moves to block your path. When you try to step around him, he blocks your movement.", 
        "You ask him: 'Let me pass. I need to buy milk, urgently!", 
        "He responds: 'You shall not pass. I move... for no man. Unless you can beat me in an arm wrestle!'.\n\nWhat will you do?"]]

eventBodyBuilderChoicesList = [
    ["Event ID", "Choice 1", "Choice 2", "Choice 3"],
    ["1", "Try to knock him out", "Try to baffle him", "Try to somersault over him"],
    ["2", "something", "sOmEtHiNg", "SOMETHING ELSE"]]

#===========================================================================================================================================
#FUNCTION DECLARATIONS    
def bark(input):1
    print("ADMIN MESSAGE -----> " + str(input))

def fightOver(actorRef, plr_dead, rounds, plr_misses, act_misses, plr_crits, act_crits):
    print ("")
    #print("\n=|AFTER ACTION REPORT|===============================================================")
    """ if plr_dead == True:
        print("|\tOh no! Your vision went black as your spine was punched out of your back! You died!!!")
    else: 
        print(f"|\tYou managed to punch the {actorRef} to death! You won!")
        print(f"|\tYou dealt {rounds} blows between you.")
    if plr_misses == 0:
        print("|\tAmazingly, you didn't miss a single of those punches!.")    
    elif plr_misses == 1:
        print("|\tYou only missed a single one of those punches!.")    
    else:
        print(f"|\tUnfortunately, you also punched the air {plr_misses} of those times.")

    if act_misses == 0:
        print("|\tTo your great shame, they didn't miss a single one of their punches!")    
    elif act_misses == 1:
        print("|\tUnfortunately, they missed only one of their punches.")    
    else:
        print(f"|\tYou almost laughed each time they missed {act_misses} of their punches.")

    if plr_crits == 0:
        print("|\tYou didn't do any major damage with any punches.")
    elif plr_crits == 1:
        print("|\tYou made him scream once with a lucky hit!")
    else:
        print(f"|\tYou made him scream {plr_crits} times with BRUTAL attacks.")
        print("|\tHe no longer looks human...Ew...")
    if act_crits == 0:
        print("|\tYou thank the heavens that they didn't land a single devastating punch.")
    elif act_crits == 1:
        print("|\tYou coughed blood when they punched you in the throat.")
    else:
        print(f"|\tYour cried like a baby, {act_crits} times, from their BRUTAL strikes.")
        print("|\tYou're going to need plastic surgery before your open casket funeral...Ew...") """
    #print("====================================================================================\n")

def genSTRBonus():
    #this function will set a bonus to strength rolls depending on the str attribute
    pl_str_bonus = 0
    if charList[1][7] == 1:
        pl_str_bonus = -5
        return pl_str_bonus
    elif charList[1][7] == 3:
        pl_str_bonus = 0
        return pl_str_bonus
    elif charList[1][7] == 5:
        pl_str_bonus = 5
        return pl_str_bonus
    else:
        print("Something went wrong when setting the pl_str_bonus. Setting it to 0")
        return pl_str_bonus

def diceRoller(count, sides, bonus):
#convert inputs to variables
    count_to_roll = count
    number_of_sides = sides
    bonus_to_add = bonus
    #create variables for use inside the function
    loop_index = count_to_roll
    x = 0
    rollTotal = 0

    #as long as x is less than the number of times you roll the dice...
    while x < count_to_roll:
    #increase the x index...
        x += 1
    #create a variable to store a random dice roll between 1 and the number of sides the dice has...
        result = random.randint(1, number_of_sides)
    #print out the result...
        #print("Roll "+str(x)+": [1d"+str(number_of_sides)+"] = " +str(result))
    #set a variable to store the result of the roll (including multiple rolls)...
        rollTotal = rollTotal + result

    #...then if there are any bonuses to the roll, add them here whilst printing them out
    #print("Bonus: +"+str(bonus_to_add)+".")   
    #print("Total (with bonus): "+str(rollTotal+bonus_to_add)+".\n")   

    #beware. this only returns the result of the last roll done in the while loop, not the first or any others in between.
    return result

def attackTarget():
    #make vars to track a combat run...
    number_of_rounds = 0
    number_of_player_crits = 0
    number_of_player_misses = 0

    number_of_actor_crits = 0
    number_of_actor_misses = 0

    #make vars to control a loop that checks if the player or actor is dead...
    player_is_dead = charList[0][6]
    actor_is_dead = charList[1][6]
    #generate the strength bonus of the player...
    strBonus = genSTRBonus()
    #bark("In attackTarget(), strBonus was set to "+str(strBonus)+".")
    #this will change whose turn it is and apply rolls to the other target
    turnIndex = 0;

    #create the loop to attack and deal damage
    while player_is_dead == False or actor_is_dead == False:
    #as nobody is dead, take turns attacking until someone dies.
    #player always goes first

        #FIRST, check if the player or the actor are already dead  (have less than or equal to 0 hit points)
        if player_is_dead == True:
            charList[0][6] = True
            #bark("On loop "+str(number_of_rounds)+", the player was set to dead! Calling the fightOver() function...")
            fightOver(charList[0][3], player_is_dead, number_of_rounds, number_of_player_misses, number_of_actor_misses, number_of_player_crits, number_of_actor_crits)
            break
        elif actor_is_dead == True:
            charList[1][6] = True
            #bark("On loop "+str(number_of_rounds)+", the actor was set to dead! Calling the fightOver() function...")
            fightOver(charList[1][3], player_is_dead, number_of_rounds, number_of_player_misses, number_of_actor_misses, number_of_player_crits, number_of_actor_crits)
            break



        #NOW, generate an attack roll as neither character would be dead at this point
        attack_roll = diceRoller(1, 20, strBonus)
        #bark("On loop: "+str(number_of_rounds) +", the attack roll was " +str(attack_roll)+"...")
        number_of_rounds += 1


        #SECOND, check if the attack roll was a critical hit, then apply that damage to whoever's turn it isn't
        if int(attack_roll) == 20:
            damage_done = int((diceRoller(1,4, strBonus))*2)

            if turnIndex == 0:
                number_of_player_crits +=1
                charList[1][2] -= ((damage_done)+strBonus)
                #bark("\t" + str(charList[0][3] + "dealt CRITICAL Damage of " + str(int(damage_done)) +"."))
                #bark("\t" + str(charList[1][3] +" Now has: "+str(charList[turnIndex][2])+" HP left"))
                turnIndex = 1
                #bark("Its the ACTORS turn now...")

            else:
                number_of_actor_crits +=1
                charList[0][2] -= ((damage_done)+strBonus)
                #bark("\t" + str(charList[1][3] + "dealt CRITICAL Damage of " + str(int(damage_done)) +"."))
                #bark("\t" + str(charList[0][3] +" Now has: "+str(charList[0][2])+" HP left"))
                turnIndex = 0
                #bark("Its the PLAYERS turn now...")


        elif int(attack_roll) >= 13 and int(attack_roll) < 20:

            damage_done = int(diceRoller(1,4, strBonus))
            if turnIndex == 0:
                charList[1][2] -= ((damage_done)+strBonus)
                turnIndex = 1
                #bark("\tNORMAL Damage of "+str(int(damage_done)) +" was done to " + str(charList[1][3] +" They now have: "+str(charList[1][2])+" HP left"))
                #bark("\tIts now the ACTORS turn...")
            else:
                charList[0][2] -= ((damage_done)+strBonus)
                turnIndex = 0
                #bark("\tNORMAL Damage of "+str(int(damage_done)) +" was done to " + str(charList[turnIndex][3] +" They now have: "+str(charList[turnIndex][2])+" HP left"))
                #bark("\tIts now the PLAYERS turn...")

        #after applying damage, check if the actor is dead    
        if charList[turnIndex][2] <= 0:
            if turnIndex == 0:
                player_is_dead = True
                charList[0][6] = True
                continue

            else:
                actor_is_dead = True
                charList[1][6] = True
                continue


        elif int(attack_roll) < 13:
            if turnIndex == 0:
                number_of_player_misses += 1
                turnIndex = 1
                #bark("\tPLAYER MISSED! Its now the ACTORS turn...")
            else:
                number_of_actor_misses += 1
                turnIndex = 0
                #bark("\tACTOR MISSED! Its now the PLAYERS turn...")


def spitChoices(): 
    #x is the amount of times to loop
    #lengthOfList is the length of the  #eventBodyBuilderChoicesList[1]
    x = 0
    lengthOfList = len(eventBodyBuilderChoicesList[1])

    #print out the event dialogue
    for x in range(1,(lengthOfList)):
        print("\t"+str(eventsList[1][x+1]) +".")
        x +=1

    x = 0
    #for loop to print out all available choices... 
    #this will ignore the first element in the list (for x in range (1....))
    for x in range(1,(lengthOfList)):
        print("\t" +str(x)+": "+str(eventBodyBuilderChoicesList[1][x]) +"")
        x +=1

    #now allow the player to choose an option (1 to x from the loop above)
    #print("\nx is " +str(x))

    print("\nEnter your choice (1-" +str(x-1)+"):")
    player_choice = input()

    print("You chose: " +str(eventBodyBuilderChoicesList[1][int(player_choice)]))


    if int(player_choice) == 1:
        attackTarget()


#ADMIN: NEED TO CALL THE ATTACK TARGET FUNCTION HERE
    elif int(player_choice) == 2:
        print("do something!")

spitChoices()
bark("Broke out of the spitChoices function!")
#now to handle player choice.
#Print from a function and a list.
#function provides multiple choices for event from list


player_is_dead = charList[0][6]