
#Imports
from tkinter import *
from tkinter import messagebox
import random


#Initialise variables
TITLE = "Python Game Center"
WINWIDTH = 600
WINHEIGHT = 400


#Mainmenu Window Setup
window = Tk()
window.title(TITLE)
window.minsize(WINWIDTH, WINHEIGHT)
window.resizable(False, False)


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
    buttonOne = Button(window, text=text, height = 2, width = 13, bg="silver")
    buttonOne.place(x=xPos,y=yPos)


def GuessingButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
   
def CalcButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, bg="silver")
    buttonOne.place(x=xPos, y=yPos)


def ButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, bg="silver")
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