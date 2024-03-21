from tkinter import *
from tkinter import messagebox

TITLE = "Game Center"

WINWIDTH = 600
WINHEIGHT = 400

window = Tk()

window.title(TITLE)
window.minsize(WINWIDTH, WINHEIGHT)
window.resizable(False, False)

def HelloCallBack():
    msg=messagebox.showinfo("CallBack", "Text")

def OpenSnakeWindow():
    snakeWindow = Toplevel(window)
    snakeWindow.title("Snake")
    Label(snakeWindow, text = "this is the text for snake").pack()

def OpenAstroidsWindow():
    snakeWindow = Toplevel(window)
    snakeWindow.title("Snake")
    Label(snakeWindow, text = "this is the text for Astroids").pack()

def TitleSetup(text):
    titleText = Label(window, text=text)
    titleText.config(font=("Helvetica", 30))
    titleText.pack()

def SnakeButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13,command = OpenSnakeWindow, bg="silver")
    buttonOne.place(x=xPos,y=yPos)
    
def AstroidsButtonSetup(text, xPos, yPos):
    buttonOne = Button(window, text=text, height = 2, width = 13, command = OpenAstroidsWindow, bg="silver")
    buttonOne.place(x=xPos, y=yPos)
    
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
    ButtonSetup("option3", 400, 100)
    ButtonSetup("option4", 175, 175)
    ButtonSetup("option4", 325, 175)
    
    QuitButtonSetup("Quit", 85, 300)

DrawMenu()

window.mainloop()