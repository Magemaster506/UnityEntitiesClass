#Imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

#Initialise varaibles
TITLE = "Python Playhouse"
WINWIDTH = 600
WINHEIGHT = 400

#Mainmenu Window Setup
window = Tk()
window.title(TITLE) 
window.minsize(WINWIDTH, WINHEIGHT)
window.resizable(False, False)

total_guesses = 1

player_score = 0
opponent_score = 0

blankString = ""

#Declaring functions

#Function to test buttons
def ReturnHello():
    msg=messagebox.showinfo("CallBack", "Text")

#Function to open the guessing game window
def OpenGuessingWindow():
    GWindow = Toplevel(window)
    GWindow.title("Guessing Game")
    GWindow.minsize(WINWIDTH, WINHEIGHT)
    GWindow.resizable(False, False)
    lbl = Label(GWindow, text = "Press the button below to guess.", font =("Helvetica", 25)).pack()
    minimumRandomNumber = 1
    maximumRandomNumber = 100 
    correct_number = random.randint(minimumRandomNumber, maximumRandomNumber)
    print(correct_number)
    input_entry = Entry(GWindow, font=("Helvetica", 12))
    input_entry.pack()
    
    def guessingFunc():
        global total_guesses
        numberOfGuesses.config(text="Total guesses = " + str(total_guesses))
        total_guesses += 1
        print(total_guesses)
        user_input = input_entry.get()

        try:
            user_input = int(user_input)  
            if user_input == correct_number:
                correctnessLabel.config(text="Good job!")
            else:
                if user_input == correct_number:
                    correctnessLabel.config(text="Good job!")
                elif abs(user_input - correct_number) <= 2:
                    correctnessLabel.config(text="Boiling!")
                elif abs(user_input - correct_number) <= 5:
                    correctnessLabel.config(text="You're Hot!")
                else:
                    correctnessLabel.config(text="Cold!")
        except ValueError:
            correctnessLabel.config(text="Please enter a valid number")


    correctnessLabel = Label(GWindow, text="", font=("Helvetica", 17))
    correctnessLabel.pack()

    numberOfGuesses = Label(GWindow, text="", font=("Helvetica", 10))
    numberOfGuesses.pack()

    buttonOne = Button(GWindow, text="Guess", height = 3, width = 30, command = guessingFunc, bg="lightblue")
    buttonOne.place(x=190, y=200)
    
    buttonTwo = Button(GWindow, text="Back", height = 3, width = 60,command = GWindow.destroy, bg="tomato")
    buttonTwo.place(x=85,y=300)  

#Function to open the pig dice game window
def OpenPigDiceWindow():
    GWindow = Toplevel(window)
    GWindow.title("Pig Dice Game")
    GWindow.minsize(WINWIDTH, WINHEIGHT)
    GWindow.resizable(False, False)
    lbl = Label(GWindow, text = "Press on the button below to roll...", font=("Helvetica", 25)).pack()
    global player_score 
    global opponent_score 
    player_score = 0
    opponent_score = 0

    def RollFunc():
        global player_score
        global opponent_score

        if(player_score > 29):
            winnerLabel.config(text="Congratulations, You Won The Game!")
        elif(opponent_score > 29):
            winnerLabel.config(text="Your Opponent Won, Better Luck Next Time...")
        elif(player_score > 29 and opponent_score > 29):
            winnerLabel.config(text="You both tied!")
        else:
            player_roll = random.randint(1,6)
            opponent_roll = random.randint(1,6)

            if(player_roll == 1):
                player_score = 0
                playerTotalLabel.config(text="You total score is : " + str(player_score))
                playerAddLabel.config(text="You rolled a 1... Your score reset!")

                opponent_roll = random.randint(1,6)
                opponent_score += opponent_roll
                opponentTotalLabel.config(text="Their total score is : " + str(opponent_score))
                opponentAddLabel.config(text="They rolled a : " + str(opponent_roll))

            elif(opponent_roll == 1):
                opponent_score = 0
                opponentTotalLabel.config(text="Their total score is : " + str(opponent_score))
                opponentAddLabel.config(text="They rolled a 1... Their score reset!")

                player_roll = random.randint(1,6)
                player_score += player_roll
                playerTotalLabel.config(text="You total score is : " + str(player_score))
                playerAddLabel.config(text="You rolled a : " + str(player_roll))

            else:
                player_score += player_roll
                opponent_score += opponent_roll

                playerTotalLabel.config(text="You total score is : " + str(player_score))
                opponentTotalLabel.config(text="Their total score is : " + str(opponent_score))
                playerAddLabel.config(text="You rolled a : " + str(player_roll))
                opponentAddLabel.config(text="They rolled a : " + str(opponent_roll))

    playerAddLabel = Label(GWindow, text = blankString, font=("Helvetica", 12))
    opponentAddLabel = Label(GWindow, text = blankString, font=("Helvetica", 12))
    playerTotalLabel = Label(GWindow, text = blankString, font=("Helvetica", 15))
    opponentTotalLabel = Label(GWindow, text = blankString, font=("Helvetica", 15))

    winnerLabel = Label(GWindow, text = blankString, font=("Helvetica", 19))

    playerAddLabel.place(x=250,y=90)
    opponentAddLabel.place(x=245,y=130)
    playerTotalLabel.place(x=20,y=80)
    opponentTotalLabel.place(x=20,y=130)

    winnerLabel.place(x=50, y=170)

    rollButton = Button(GWindow, text="Roll The Dice...", height = 3, width = 30, command = RollFunc, bg="lightblue")
    rollButton.place(x=185, y=225)
    
    quitButton = Button(GWindow, text="Back", height = 3, width = 60,command = GWindow.destroy, bg="tomato")
    quitButton.place(x=85,y=300)  

#Function to open the calculator window
def OpenCalcWindow():

    adding = False
    subtracting = False
    multiplying = False

    GWindow = Toplevel(window)
    GWindow.title("Calculator")
    GWindow.minsize(WINWIDTH, WINHEIGHT)
    GWindow.resizable(False, False)
    lbl = Label(GWindow, text = "Press one of the buttons to calculate.", font =("Helvetica", 25)).pack()

    input_entry_1 = Entry(GWindow, font=("Helvetica", 12))
    input_entry_2 = Entry(GWindow, font=("Helvetica", 12))
    input_entry_1.pack()
    input_entry_2.pack()
    
    def addition():

        user_input_1 = input_entry_1.get()
        user_input_2 = input_entry_2.get()

        user_input_1 = int(user_input_1)  
        user_input_2 = int(user_input_2) 

        result = user_input_1 + user_input_2

        correctnessLabel.config(text=result)
        

    def subtraction():
        user_input_1 = input_entry_1.get()
        user_input_2 = input_entry_2.get()

        user_input_1 = int(user_input_1)  
        user_input_2 = int(user_input_2) 

        result = user_input_1 - user_input_2

        correctnessLabel.config(text=result)

    def multiplication():
        user_input_1 = input_entry_1.get()
        user_input_2 = input_entry_2.get()

        user_input_1 = int(user_input_1)  
        user_input_2 = int(user_input_2) 

        result = user_input_1 * user_input_2

        correctnessLabel.config(text=result)


    correctnessLabel = Label(GWindow, text="", font=("Helvetica", 17))
    correctnessLabel.pack()
    
    addButton = Button(GWindow, text="Addition", height = 2, width = 10, command = addition, bg="lightblue")
    addButton.place(x=150, y=200)
    minusButton = Button(GWindow, text="Subtraction", height = 2, width = 10, command = subtraction, bg="lightblue")
    minusButton.place(x=260, y=200)
    multiButton = Button(GWindow, text="Multiplication", height = 2, width = 10, command = multiplication, bg="lightblue")
    multiButton.place(x=370, y=200)
    
    quitButton = Button(GWindow, text="Back", height = 3, width = 60,command = GWindow.destroy, bg="tomato")
    quitButton.place(x=85,y=300)  

#Function to open the rock, paper, scissors window
def OpenRpsWindow():
    #Setting up the game window
    GWindow = Toplevel(window)
    GWindow.title("Rock Paper Scissors")
    GWindow.minsize(WINWIDTH, WINHEIGHT)
    GWindow.resizable(False, False)
    #Setting up the header
    title = Label(GWindow, text = "Rock Paper Scissors.", font =("Helvetica", 25)).pack()

    global player_choice
    global computer_choice
    player_choice = ""
    computer_choice = ""

    global player_rps_score
    global computer_rps_score
    player_rps_score = 0
    computer_rps_score = 0

    options = ['scissors', 'paper', 'rock']

    def scissors():
        global player_choice
        global computer_choice
        global player_rps_score
        global computer_rps_score

        if player_rps_score >= 5:
            playerChoiceLabel.config(text = blankString)
            computerChoiceLabel.config(text = blankString) 

            resultLabel.config(text = "You Won The Game!!!")
            resultLabel.place(x=300,y=200, anchor=CENTER)

        elif computer_rps_score >= 5:
            playerChoiceLabel.config(text = blankString)
            computerChoiceLabel.config(text = blankString)

            resultLabel.config(text = "You Lost The Game!!!")
            resultLabel.place(x=300,y=200, anchor=CENTER)

        else:
            player_choice = "scissors"
            playerChoiceLabel.config(text = "Player chose scissors.")
            computer_choice = random.choice(options)
            computerChoiceLabel.config(text = "The Computer chose " + computer_choice)

            if(computer_choice == player_choice):
                resultLabel.config(text = "It was a tie!")
            elif(computer_choice == 'rock'):
                resultLabel.config(text = "You Lose!")
                computer_rps_score += 1 
                computerScoreLabel.config(text = "Computer Score = " + str(computer_rps_score))
            elif(computer_choice == 'paper'):
                resultLabel.config(text = "You Win!")
                player_rps_score += 1
                playerScoreLabel.config(text = "Player Score = " + str(player_rps_score))

    def paper():
        global player_choice
        global computer_choice
        global player_rps_score
        global computer_rps_score

        if player_rps_score >= 5:
            playerChoiceLabel.config(text = blankString)
            computerChoiceLabel.config(text = blankString) 

            resultLabel.config(text = "You Won The Game!!!")
            resultLabel.place(x=300,y=200, anchor=CENTER)

        elif computer_rps_score >= 5:
            playerChoiceLabel.config(text = blankString)
            computerChoiceLabel.config(text = blankString) 

            resultLabel.config(text = "You Lost The Game!!!")
            resultLabel.place(x=300,y=200, anchor=CENTER)

        else:
            player_choice = "paper"
            playerChoiceLabel.config(text = "Player chose paper.")
            computer_choice = random.choice(options)
            computerChoiceLabel.config(text =  "The computer chose " + computer_choice)

            if(computer_choice == player_choice):
                resultLabel.config(text = "It was a tie!")
            elif(computer_choice == 'rock'):
                resultLabel.config(text = "You Win!")
                player_rps_score += 1
                playerScoreLabel.config(text = "Player Score = " + str(player_rps_score))
            elif(computer_choice == 'scissors'):
                resultLabel.config(text = " You Lose!")
                computer_rps_score += 1 
                computerScoreLabel.config(text = "Computer Score = " + str(computer_rps_score))

    def rock():
        global player_choice
        global computer_choice
        global player_rps_score
        global computer_rps_score

        player_choice = "rock"
        if player_rps_score >= 5:
            playerChoiceLabel.config(text = blankString)
            computerChoiceLabel.config(text = blankString) 

            resultLabel.config(text = "You Won The Game!!!")
            resultLabel.place(x=300,y=200, anchor=CENTER)

        elif computer_rps_score >= 5:
            playerChoiceLabel.config(text = blankString)
            computerChoiceLabel.config(text = blankString)

            resultLabel.config(text = "You Lost The Game!!!")
            resultLabel.place(x=300,y=200, anchor=CENTER)
            
        else:
            playerChoiceLabel.config(text = "Player chose rock.")
            computer_choice = random.choice(options)
            computerChoiceLabel.config(text = "The computer chose " + computer_choice)

            if(computer_choice == player_choice):
                resultLabel.config(text = "It was a tie!")
            elif(computer_choice == 'paper'):
                resultLabel.config(text = "You Lose!")
                computer_rps_score += 1 
                computerScoreLabel.config(text = "Computer Score = " + str(computer_rps_score))
            elif(computer_choice == 'scissors'):
                resultLabel.config(text = "You Win!")
                player_rps_score += 1
                playerScoreLabel.config(text = "Player Score = " + str(player_rps_score))


    
    playerScoreLabel = Label(GWindow, text = "Player Score = 0", font = ("Helevtica", 14))
    computerScoreLabel = Label(GWindow, text = "Computer Score = 0", font=("Helvetica", 14))
    playerScoreLabel.place(x=35,y=100)
    computerScoreLabel.place(x=395,y=100)

    playerChoiceLabel = Label(GWindow, text = blankString, font = ("Helevtica", 14))
    computerChoiceLabel = Label(GWindow, text = blankString, font = ("Helevtica", 14))
    resultLabel = Label(GWindow, text = blankString, font = ("Helevtica", 14))

    playerChoiceLabel.place(x=300,y=150, anchor = CENTER)
    computerChoiceLabel.place(x=300,y=180, anchor = CENTER)
    resultLabel.place(x=300,y=225, anchor = CENTER)

    addButton = Button(GWindow, text="Scissors", height = 2, width = 10, command = scissors, bg="lightblue")
    addButton.place(x=150, y=240)
    minusButton = Button(GWindow, text="Paper", height = 2, width = 10, command = paper, bg="lightblue")
    minusButton.place(x=260, y=240)
    multiButton = Button(GWindow, text="Rock", height = 2, width = 10, command = rock, bg="lightblue")
    multiButton.place(x=370, y=240)
    
    quitButton = Button(GWindow, text="Back", height = 3, width = 60,command = GWindow.destroy, bg="tomato")
    quitButton.place(x=85,y=300)  

#Function to open the simon says window
def OpenSimonWindow():

    global colours, sequence, player_sequence, level, buttons, start_button, message_label, main_window
    colours = ["red", "green", "blue", "yellow"]
    sequence = []
    player_sequence = []
    level = 0

    main_window = tk.Tk()
    main_window.title("Simon Says")
    main_window.minsize(WINWIDTH, WINHEIGHT)
    main_window.resizable(False,False)
    lbl = Label(main_window, text = "-Simon Says-", font = ("Helvetica", 25)).pack()
    buttonTwo = Button(main_window, text="Back", height = 3, width = 60,command = main_window.destroy, bg="tomato")
    buttonTwo.place(x=85,y=300)  

    buttons = {}
    for colour in colours:
        button = tk.Button(main_window, bg=colour, width=10, height=5, command=lambda c=colour: player_input(c))
        button.pack(side=tk.LEFT, padx=35, pady=0)
        buttons[colour] = button

    def start_game():
        global sequence, player_sequence, level
        sequence = []
        player_sequence = []
        level = 0
        message_label.config(text="")
        next_level()
    
    start_button = tk.Button(main_window, text="Start", command=start_game, width=20, height=2, bg="lightblue")
    start_button.place(x=225, y=80)

    message_label = tk.Label(main_window, text="", font=("Helvetica", 16))
    message_label.place(x=262.5,y=135)

    def next_level():
        global level, sequence, player_sequence
        level += 1
        player_sequence = []
        sequence.append(random.choice(colours))
        message_label.config(text=f"Level {level}")
        main_window.after(1000, play_sequence)
    
    def play_sequence():
        for index, colour in enumerate(sequence):
            main_window.after(index * 1000, lambda c=colour: flash_button(c))
    
    def flash_button(colour):
        original_colour = buttons[colour].cget("bg")
        buttons[colour].config(bg="white")
        window.after(500, lambda: buttons[colour].config(bg=original_colour))
    
    def player_input(colour):
        global player_sequence
        player_sequence.append(colour)
        if player_sequence == sequence[:len(player_sequence)]:
            if len(player_sequence) == len(sequence):
                message_label.config(text="Correct!")
                main_window.after(1000, next_level)
        else:
            message_label.config(text="Game Over!")
            start_button.config(state=tk.NORMAL)
    
#function to open the insult me game window
def OpenInsultWindow():
    OpenInsultWindow.insultWindow = Tk()
    OpenInsultWindow.insultWindow.title("Insult Me")
    OpenInsultWindow.insultWindow.minsize(WINWIDTH, WINHEIGHT)
    OpenInsultWindow.insultWindow.resizable(False, False)
    lbl = Label(OpenInsultWindow.insultWindow, text = "Press the button below to be insulted.", font =("Helvetica", 25)).pack()

    def insultFunc():
        column1=["artless", "bawdy", "beslubbering", "bootless", "churlish", "cloven", "clouted", "craven", "currish",
        "dankish", "dissembling", "droning", "errant", "fawning", "fobbing", "forward", "frothy", "gleeking",
        "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering",
        "mangled", "mewling", "paunchy", "pribbling", "puking", "puny", "qualling", "rank", "reeky",
        "roguish", "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering", "unmuzzled", "vain", "venomed",
        "villainous", "warped", "wayward", "weedy", "yeast"]

        column2=["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed",
            "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted",
            "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-faced", "flap-mouthed",
            "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced",
            "hasty-witted", "hedge-born", "hell-hated", "idle-headed", "ill-breeding", "ill-nurtured",
            "knotty-pated", "milk-livered", "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep",
            "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne",
            "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", 
            "unchin-snouted", "weather-bitten"]

        column3=["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "box-bailey", "canker-blossom",
            "clack-dish", "clotpole", "coxcomb", "cod-fish", "death-token", "dewberry", "flap-dragon", "flax-wench",
            "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpo", "hedge-pig",
            "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet",
            "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut",
            "puttock", "pumpion", "ratsbane", "scud", "skainsmate", "trumpet", "varlot", "vassal", "whey-face",
            "wagtail", "foot licker"]

        maxcol1 = len(column1)
        maxcol2 = len(column2)
        maxcol3 = len(column3)
        value = column1[random.randint(0,maxcol1-1)],column2[random.randint(0,maxcol2-1)],column3[random.randint(0,maxcol3-1)]
        insult = value
        insult_label.config(text=insult)

    buttonOne = Button(OpenInsultWindow.insultWindow, text="Insult Me", height = 3, width = 30, command = insultFunc, bg="lightblue")
    buttonOne.place(x=190,y=200)
    buttonTwo = Button(OpenInsultWindow.insultWindow, text="Back", height = 3, width = 60,command = OpenInsultWindow.insultWindow.destroy, bg="tomato")
    buttonTwo.place(x=85,y=300)  
    
    insult_label = Label(OpenInsultWindow.insultWindow, text="", font=("Helvetica", 18))
    insult_label.pack()

#Header setup
def TitleSetup(text):
    topText = Label(window, text="Welcome to")
    topText.config(font=("Helvetica", 18))
    topText.pack()
    titleText = Label(window, text=text)
    titleText.config(font=("Helvetica", 30))
    titleText.pack()
    bodyText = Label(window, text="Click a button to get started")
    bodyText.config(font=("Helvetica", 11))
    bodyText.pack()

def GameOptionsSetup():
    GuessingButtonSetup("Guessing Game", 100, 135)
    CalcButtonSetup("Calculator", 250, 135)
    PigDiceButtonSetup("Pig Dice Game", 400, 135)
    SimonButtonSetup("Simon Says", 175, 210)
    RpsButtonSetup("RockPaperScissors", 325, 210)

#Individual button setup
#Function to settup and place the game specific buttons.
def InsultButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenInsultWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)

def GuessingButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = OpenGuessingWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def PigDiceButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenPigDiceWindow, bg = "silver")
    buttonOne.place(x=xPos, y=yPos)

def CalcButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenCalcWindow, bg="silver")
    buttonOne.place(x=xPos, y=yPos)

def RpsButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenRpsWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def SimonButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenSimonWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)

def ButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = ReturnHello, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def QuitButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 3, width = 60,command = window.destroy, bg="tomato")
    buttonOne.place(x=xPos,y=yPos)  


#Draw GUI elements to screen
def DrawMenu():
    TitleSetup(TITLE)

    GameOptionsSetup()
    
    QuitButtonSetup("Quit", 85, 300)

DrawMenu()

window.mainloop()
