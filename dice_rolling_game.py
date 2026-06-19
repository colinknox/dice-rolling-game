import random

while True:
    user_choice = input("Roll the dice? (y/n): ").lower()
    if user_choice == "y":
        dice_rolls_tuple = ()
        for roll in range(2):
            roll_result = random.randint(1, 6)
            dice_rolls_tuple += (roll_result,)
        print(dice_rolls_tuple)
    elif user_choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
