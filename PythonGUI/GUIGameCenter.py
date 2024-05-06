#Imports
from tkinter import *
from tkinter import messagebox
import random

#Initialise varaibles
TITLE = "Python Game Center"
WINWIDTH = 600
WINHEIGHT = 400

#Mainmenu Window Setup
window = Tk()
window.title(TITLE)
window.minsize(WINWIDTH, WINHEIGHT)
window.resizable(False, False)

total_guesses = 0

#Declaring functions
def ReturnHello():
    msg=messagebox.showinfo("CallBack", "Text")

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
                if user_input > correct_number:
                    correctnessLabel.config(text="Your guess was too high!")
                elif user_input < correct_number:
                    correctnessLabel.config(text="Your guess was too low!")
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
            "wagtail"]

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
    
    insult_label = Label(OpenInsultWindow.insultWindow, text="", font=("Helvetica", 14))
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

#Individual button setup
def InsultButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenInsultWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)

def GuessingButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = OpenGuessingWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def CalcButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenCalcWindow, bg="silver")
    buttonOne.place(x=xPos, y=yPos)

def ButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = ReturnHello, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def QuitButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 3, width = 60,command = window.destroy, bg="tomato")
    buttonOne.place(x=xPos,y=yPos)  

#Draw GUI elements to screen
def DrawMenu():
    TitleSetup(TITLE)
    
    GuessingButtonSetup("Guessing Game", 100, 135)
    CalcButtonSetup("Calculator", 250, 135)
    ButtonSetup("option3", 400, 135)
    InsultButtonSetup("Insult Me", 175, 210)
    ButtonSetup("option5", 325, 210)
    
    QuitButtonSetup("Quit", 85, 300)

DrawMenu()

window.mainloop()
