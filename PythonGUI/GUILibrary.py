from tkinter import *
from settings  import *

window = Tk()

window.title(TITLE)
window.minsize(WINWIDTH, WINHEIGHT)

titleText = Label(window, text="test")
titleText.config(font=("Courier", 44))
titleText.pack()

window.mainloop()