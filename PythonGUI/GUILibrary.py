from tkinter import *
from tkinter import messagebox

TITLE = "Game Center"

WINWIDTH = 600
WINHEIGHT = 400

window = Tk()

window.title(TITLE)
window.minsize(WINWIDTH, WINHEIGHT)
window.resizable(False, False)

def helloCallBack():
    msg=messagebox.showinfo( "CallBack", "Text")

def openSnakeWindow():
    snakeWindow = Toplevel(window)
    snakeWindow.title("Snake")
    Label(snakeWindow, text = "this is the text for snake").pack()

def TitleSetup(text):
    titleText = Label(window, text=text)
    titleText.config(font=("Helvetica", 30))
    titleText.pack()

def ButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = openSnakeWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def QuitButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 3, width = 60,command = window.destroy, bg="tomato")
    buttonOne.place(x=xPos,y=yPos)

def DrawMenu():
    TitleSetup(TITLE)
    ButtonSetup("Snake", 100, 100)
    ButtonSetup("option2", 250, 100)
    ButtonSetup("option3", 400, 100)
    ButtonSetup("option4", 175, 175)
    ButtonSetup("option4", 325, 175)
    QuitButtonSetup("Quit", 85, 300)

DrawMenu()

window.mainloop()