from tkinter import *
from tkinter import messagebox
import random

TITLE = "Game Center"
WINWIDTH = 600
WINHEIGHT = 400

SWINWIDTH = 300 
SWINHEIGHT = 300

AWINWIDTH = 300
AWINHEIGHT = 300

MWINWIDTH = 400
MWINHEIGHT = 400

window = Tk()

window.title(TITLE)
window.minsize(WINWIDTH, WINHEIGHT)
window.resizable(False, False)

def HelloCallBack():
    msg=messagebox.showinfo("CallBack", "Text")

def OpenMineWindow():
    mineWindow = Toplevel(window)
    mineWindow.title("Minesweeper")
    mineWindow.minsize(MWINWIDTH, MWINHEIGHT)
    mineWindow.resizable(False, False)
    Label(mineWindow, text = "this is the text for MineSweeper").pack()

def OpenSnakeWindow():
    snakeWindow = Toplevel(window)
    snakeWindow.title("Snake")
    snakeWindow.minsize(SWINWIDTH, SWINHEIGHT)
    snakeWindow.resizable(False, False)
    Label(snakeWindow, text = "this is the text for snake").pack()

def OpenAstroidsWindow():
    astroidsWindow = Toplevel(window)
    astroidsWindow.title("Astroids")
    astroidsWindow.minsize(AWINWIDTH, AWINHEIGHT)
    astroidsWindow.resizable(False, False)
    Label(astroidsWindow, text = "this is the text for Astroids").pack()

def OpenInsultWindow():
    insultWindow = Toplevel(window)
    insultWindow.title("Insult Me")
    insultWindow.minsize(WINWIDTH, WINHEIGHT)
    insultWindow.resizable(False, False)
    lbl = Label(insultWindow, text = "Press the button below to be insulted.", font =("Helvetica", 25)).pack()



    def onclick(target):
        target.lbl.destroy()
        textWindow = Toplevel(window)
        textWindow.title("YourInsult")
        textWindow.minsize(100,25)
        textWindow.resizable(False, False)
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
        value = column1[random.randint(0,maxcol1)],column2[random.randint(0,maxcol2)],column3[random.randint(0,maxcol3)]
        lbl = Label(textWindow, text = value).pack()

    buttonOne = Button(insultWindow, text="Insult Me", height = 6, width = 60,command= lambda: onclick(insultWindow), bg="lightblue")
    buttonTwo = Button(insultWindow, text="Back", height = 3, width = 60,command = insultWindow.destroy, bg="tomato")
    buttonTwo.place(x=85,y=300)  
    buttonOne.place(x=85,y=150)  
        


def TitleSetup(text):
    titleText = Label(window, text=text)
    titleText.config(font=("Helvetica", 30))
    titleText.pack()

def InsultButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenInsultWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)

def SnakeButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = OpenSnakeWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def AstroidsButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenAstroidsWindow, bg="silver")
    buttonOne.place(x=xPos, y=yPos)

def MineButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenMineWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def ButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = HelloCallBack, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def QuitButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 3, width = 60,command = window.destroy, bg="tomato")
    buttonOne.place(x=xPos,y=yPos)  

def DrawMenu():
    TitleSetup(TITLE)
    
    SnakeButtonSetup("Snake", 100, 100)
    AstroidsButtonSetup("Astroids", 250, 100)
    MineButtonSetup("MineSweeper", 400, 100)
    InsultButtonSetup("Insult Me", 175, 175)
    ButtonSetup("option4", 325, 175)
    
    QuitButtonSetup("Quit", 85, 300)

DrawMenu()

window.mainloop()