import random

user_choice = input("Roll the dice? (y/n): ")

if user_choice == "y":
    for roll in range(2):
        roll_result = random.randint(1, 6)
        print(roll_result) 

# Loop
    # Ask user "Roll dice? (y/n)" 
    # If user answer == "y":
        # Randomize dice roll 1
        # Randomize dice roll 2
        # Print (dice roll 1/dice roll 2)
    # If user answer == "n":
        # Print "Thanks for playing"
        # break
    # If user answer not valid choice:
        # Print "Invalid choice!"
