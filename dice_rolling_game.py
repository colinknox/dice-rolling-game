import random
    
roll_counter = 0

while True:
    user_choice = input("Roll the dice? (y/n): ").lower()
    if user_choice == "y":
        roll_quantity = int(input("How many dice do you want to roll?: "))
        dice_rolls_tuple = ()
        for roll in range(roll_quantity):
            roll_result = random.randint(1, 6)
            dice_rolls_tuple += (roll_result,)
        roll_counter += 1
        print(dice_rolls_tuple)
    elif user_choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")

    if roll_counter == 1:
        print(f"You have rolled {roll_counter} time.")
    else:
        print(f"You have rolled {roll_counter} times.")
        