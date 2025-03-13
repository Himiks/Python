import random
from dicepicture import dice_drawing
def roll_dice():
    roll = input("Roll the dice (Yes/No): ").lower()
    while roll == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)

        print(f"dice rolled: {dice1} and {dice2}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input("Roll the dice (Yes/No): ").lower()



roll_dice()