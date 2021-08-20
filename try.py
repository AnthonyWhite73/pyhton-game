def input_number(message):
   while True:
      try:
         user_input = int(input(message))
         if user_input == 5 or user_input == 3 or user_input ==1:
            return user_input
            break            
         else:
            print("You need to enter 5,3 or 1\n")
            continue
      except ValueError:
         print("You need to enter 5,3 or 1\n")
         continue

player_choice = input_number("Enter your strength, 5(maximum), 3 or 1(lowest)")

print(player_choice)