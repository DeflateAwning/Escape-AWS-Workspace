

from tkinter import *
import time, datetime

import keyboard

# Create an instance of tkinter window or frame
win = Tk() # Note: often called "root" by convention

# Setting the geometry of window (position and location)
xCoord = win.winfo_screenwidth() - 420
yCoord = win.winfo_screenheight() - 25
win.geometry(f"80x30+{xCoord}+{yCoord}") # str like "80x30+1500+1775"

# eliminate the titlebar
win.overrideredirect(1)

def handleClick():
	""" Shows the taskbar. """
	keyboard.press_and_release('windows')

	print("Showing task bar.")

# add button
Button(win, text=(" " * 30) + "Exit" + (" " * 30), command=handleClick).pack()

def setOnTop():
	# if 7 < datetime.datetime.now().time().hour < 12+5: # can be used to only put the button on top during work hours
	win.attributes('-topmost', True)

	win.after(1000, setOnTop)

win.after(1000, setOnTop)

win.mainloop()
