from tkinter import *
from tkinter import messagebox
import os

tkWindow = Tk()  
tkWindow.title('Game Launcher')

def showMsg():  
    os.startfile(r'C:\Users\jigglyyy\Desktop\New folder\breakout.exe')

def showMsg2():  
    os.startfile(r'C:\Users\jigglyyy\Desktop\New folder\main.exe')

photo = PhotoImage(file = r"C:\Users\jigglyyy\Desktop\New folder\breakout.png")
photoimage = photo.subsample(2, 2)
photo2 = PhotoImage(file = r"C:\Users\jigglyyy\Desktop\New folder\pacman.png")
photoimage2 = photo2.subsample(2, 2)

button = Button(tkWindow,
    image=photoimage,
	text = 'Submit',
	command = showMsg)  
button.pack(side = LEFT)  

button = Button(tkWindow,
    image=photoimage2,
	text = 'Submit',
	command = showMsg2)  
button.pack(side = RIGHT)  
  
tkWindow.mainloop()