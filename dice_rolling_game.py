import random

user_choice = input("Roll the dice? (y/n): ").lower()

if user_choice == "y":
    dice_rolls_tuple = ()
    for roll in range(2):
        roll_result = random.randint(1, 6)
        dice_rolls_tuple += (roll_result,)
    print(dice_rolls_tuple)
elif user_choice == "n":
    print("Thanks for playing!")
else:
    print("Invalid choice!")


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
