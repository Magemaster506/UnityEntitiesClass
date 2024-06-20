import random

user_roll = 0
ai_roll = 0

def Pig_Dice_Game():
    user_score = 0
    ai_score = 0
    game = True

    while(game):
        if(user_score >= 30 and ai_score >= 30):
            game = False
            print("You Tied!")
        elif(user_score >= 30):
            game = False
            print("Congratulations! You  Won The Game!")
        elif(ai_score >= 30):
            game = False
            print("Your Oponent Won, Better Luck Next Time.")
        else:
            cont = input("Press Enter to roll again")

            user_roll = random.randint(1,6)
            ai_roll = random.randint(1,6)

            user_score += user_roll
            ai_score += ai_roll

            print("Your Score is", user_score)
            print("Your Oponents Score is", ai_score)

Pig_Dice_Game()