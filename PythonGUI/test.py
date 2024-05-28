def Number_Guessing_Game():
    print("Starting Number Guessing Game...")
    Guessing_Func()
    print("Number Guessing game goes here.")

def Guessing_Func():
    #game goes in here

def Pig_Dice_Game():
    print("Starting Pig Dice Game...")
    # Placeholder for Pig Dice game logic
    print("Pig Dice game goes here.")


def Rock_Paper_Scissors_Game():
    print("Starting Rock Paper Scissors...")
    # Placeholder for Rock Paper Scissors game logic
    print("Rock paper Scissors game goes here.")


def Simon_Game():
    print("Starting Simon...")
    # Placeholder for Simon game logic
    print("Simon game goes here")


def exit_game():
    print("Exiting the games menu. We hope to see you again!")
    quit()


def main_menu():
    while True:
        print("\nWelcome To Mega Cool Games Centre")
        print("Please select a game from the menu below:")
        print("1. Number Guessing Game")
        print("2. Pig Dice Game")
        print("3. Rock Paper Scissors Game")
        print("4. Simon Game")
        print("5. Exit Game Centre")


        choice = input("Enter your choice (1-5): ")
       
        if choice == '1':
            Number_Guessing_Game()
        elif choice == '2':
            Pig_Dice_Game()
        elif choice == '3':
            Rock_Paper_Scissors_Game()
        elif choice == '4':
            Simon_Game()
        elif choice == '5':
            exit_game()
        else:
            print("Invalid choice, please choose from 1-5.")


main_menu()