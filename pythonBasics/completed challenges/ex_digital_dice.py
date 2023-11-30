import random

def roll_dice():
    return random.randint(1,6)

def display_dice(number):
    dice_art=[
        "+--------+",
        "|        |",
        f"|    {number}   |",
        "|        | ",
        "+--------+"
    ]
    for line in dice_art:
        print(line)
        
def main():
    dice_result = 5
    display_dice(dice_result)
    
    
if __name__ == "__main__":
    main()
