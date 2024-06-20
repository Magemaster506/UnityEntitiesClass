import sys
import random
from time import sleep

def print_menu():
    print("Welcome to the Stoda's Game Center!")
    print("1. High, Low")
    print("2. Pig Dice")
    print("3. Rock, Paper, Scissor")
    print("4. Simon Says")
    print("5. Quit")

def high_low_game():
    # Implementing the High-Low game here
    print("Welcome to the High-Low game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    guess_counter = 0

    # Responding to the users guess
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        guess_counter += 1
        low_boiling = secret_number - 2
        high_boiling = secret_number + 2
        low_very_warm = secret_number - 5
        high_very_warm = secret_number + 5
        low_warm = secret_number - 10
        high_warm = secret_number + 10

        # Guessing the number corresponding to the text
        if guess < secret_number and guess > low_boiling:
            print("Boiling!")
        elif guess < secret_number and guess > low_very_warm:
            print("Very Warm! So close")
        elif guess < secret_number and guess > low_warm:
            print("Warm! Your getting there")
        elif guess < secret_number:
            print("You are Cold! Keep trying")
        elif guess > secret_number and guess < high_boiling:
            print("Boiling!")
        elif guess > secret_number and guess < high_very_warm:
            print("Very Warm!")
        elif guess > secret_number and guess < low_warm:
            print("Warm! Your getting there")
        elif guess > secret_number:
            print("You are Cold! Keep trying")

        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {guess_counter} attempts.")
            break
    main()

def pig_dice_game():
    # Get player's name and opponent's name
    username = input("Enter your name to get started: ")
    print("Welcome to Pig, a dice game. First to get to 30 points wins, good luck " + username + "!")
    opponent_name = input("What would you like your opponent to be called " + username + "?: ")
    
    # Initialize game variables
    game = True
    user_score = 0
    ai_score = 0
    roll_count = 0

    
    while game == True:
        # Check winning conditions
        if user_score >= 30 and ai_score >= 30:
            game = False
            print("You Tied!")
            main()  
        elif user_score >= 30:
            game = False
            print("Congratulations! " + username + " Won The Game!")
            print(" ")
            main()  
        elif ai_score >= 30:
            game = False
            print(opponent_name + " Won, Better Luck Next Time.")
            print(" ")
            main()  

        # Roll the dice
        if roll_count == 0:
            start = input("Press Enter to roll")
            roll_count = 1
            user_roll = random.randint(1, 6)
            ai_roll = random.randint(1, 6)

            # Handle user's roll
            if user_roll == 1:
                print(" ")
                print(username + " rolled A 1! No Points Will be Added.")
                print(" ")
            else:
                user_score += user_roll

            # Handle AI's roll
            if ai_roll == 1:
                print(" ")
                print(opponent_name + " rolled A 1! No Points will be Added.")
                print(" ")
            else:
                ai_score += ai_roll

            # Print scores
            print(" ")
            print(username + " rolled a " + str(user_roll))
            print(opponent_name + " rolled a " + str(ai_roll))

            print("######################")
            print(username + "'s Score is", user_score)
            print(opponent_name + "'s Score is", ai_score)
            print("######################")
        else:
            cont = input("Press Enter to roll again")
            user_roll = random.randint(1, 6)
            ai_roll = random.randint(1, 6)

            # Handle user's roll
            if user_roll == 1:
                print(" ")
                print(username + " rolled A 1! No Points will be Added.")
            else:
                print(" ")
                print(username + " rolled a " + str(user_roll))
                user_score += user_roll

            # Handle AI's roll
            if ai_roll == 1:
                print(opponent_name + " rolled A 1! No Points Will be Added.")
            else:
                print(opponent_name + " rolled a " + str(ai_roll))
                ai_score += ai_roll

            # Print scores
            print("######################")
            print(username + "'s Score is", user_score)
            print(opponent_name + "'s Score is", ai_score)
            print("######################")
    main()    

def rock_paper_scissor(player_score_t, computer_score_t):
    # Implement Rock-Paper-Scissor game here
    isPlaying = True

    global player_score_rps
    global computer_score_rps

    player_score_rps = 0
    computer_score_rps = 0

    while isPlaying == True:
        user_action = input ("Enter a choice (Rock, Paper or Scissors): ")

        possible_action = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_action)
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        # Determining a winner

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
            print("Your Score Is Still " + str(player_score_t))
            print("Their Score Is Still " + str(computer_score_t))
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win")
                player_score_t += 1 
                if player_score_t == 5:
                    print("You Got to 5 Points, You Win!")
                    return
                elif computer_score_t == 5:
                    print("They Got To 5 Points, You Lose!")
                    return
                else:
                    print("Your Score Is Now " + str(player_score_t))
                    print("Their Score Is Still " + str(computer_score_t))
            else:
                print("Paper cover rock! You lose")
                computer_score_t += 1 
                if player_score_t == 5:
                    print("You Got to 5 Points, You Win!")
                    return
                elif computer_score_t == 5:
                    print("They Got To 5 Points, You Lose!")
                    return
                else:
                    print("Your Score Is Still " + str(player_score_t))
                    print("Their Score Is Now " + str(computer_score_t))
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win")
                player_score_t += 1 
                if player_score_t == 5:
                    print("You Got to 5 Points, You Win!")
                    return
                elif computer_score_t == 5:
                    print("They Got To 5 Points, You Lose!")
                    return
                else:
                    print("Your Score Is Now " + str(player_score_t))
                    print("Their Score Is Still " + str(computer_score_t))
            else:
                print("Scissor cuts paper! You lose")
                computer_score_t += 1
                if player_score_t == 5:
                    print("You Got to 5 Points, You Win!")
                    return
                elif computer_score_t == 5:
                    print("They Got To 5 Points, You Lose!")
                    return
                else:
                    print("Your Score Is Still " + str(player_score_t))
                    print("Their Score Is Now " + str(computer_score_t))
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissor cuts paper! You win")
                player_score_t += 1 
                if player_score_t == 5:
                    print("You Got to 5 Points, You Win!")
                    return
                elif computer_score_t == 5:
                    print("They Got To 5 Points, You Lose!")
                    return
                else:
                    print("Your Score Is Now " + str(player_score_t))
                    print("Their Score Is Still " + str(computer_score_t))
            else:
                print("Rock smashes scissors! You lose")
                computer_score_t += 1 
                if player_score_t == 5:
                    print("You Got to 5 Points, You Win!")
                    pass
                elif computer_score_t == 5:
                    print("They Got To 5 Points, You Lose!")
                    pass
                else:
                    print("Your Score Is Still " + str(player_score_t))
                    print("Their Score Is Now " + str(computer_score_t))
        elif user_action != "rock" and user_action != "paper" and user_action != "scissors":
                    print("Invalid option! Tony would not be happy with that would he?")
        play_again = input("Play again? (y/n): ")
        if play_again == "y":
            rock_paper_scissor(player_score_t, computer_score_t)
        else:
            pass
        
        main()

def simon_says():

    #Function to clear screen
    def clear_screen():
        print("\n" * 50)

    numbers = ["1","2","3","4","5","6","7","8","9"]
    sequence = []
    isPlaying = True
    level = 0

    print("Welcome to Simon Says.")
    print("")

    while isPlaying == True:

        choice = random.choice(numbers)
        sequence.append(choice)

        if level <= 6:
            print("You have 4 seconds to memorize the sequence...")
            print(*sequence, sep=", ")
            sleep(4)
        elif level <= 11:
            print("You have 5 seconds to memorize the sequence...")
            print(*sequence, sep=", ")
            sleep(5)
        else:
            print("You have 6 seconds to memorize the sequence...")
            print(*sequence, sep=", ")
            sleep(6)

        clear_screen()

        player_input = input("Enter the sequence, seperated by a space. ")
        player_input = player_input.split()

        if player_input == sequence:
            print("Your guess was correct!")
            level = level + 1
            print("Your score is now " + str(level))
            input("Press enter to continue: ")
            print()
        else:
            print("Nice try, The sequence was ", *sequence, sep=", ")
            print("You reached a score of" + str(level))
            isPlaying = False


    main()

def main():
    print_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        high_low_game()
    elif choice == "2":
        pig_dice_game()
    elif choice == "3":
        rock_paper_scissor(0,0)
    elif choice == "4":
        simon_says()
    elif choice == "5":
        print("Thanks for playing!")
        sys.exit()
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
main()
