

from tkinter import *
import time, datetime

import keyboard

#Create an instance of tkinter window or frame
win = Tk()

# Setting the geometry of window (position and location)
#win.geometry("600x350")
win.geometry("80x30+1500+1055")
# TODO set location based on screen size

# Create a Label
#Label(win, text= "!!!!",font=('Helvetica bold', 15)).pack(pady=0)

# Hide the title bar (Linux?)
# win.wm_attributes('-type', 'splash')
# win.attributes('-type','splash')

# eliminate the titlebar
win.overrideredirect(1)

def handleClick():
	""" Shows the taskbar. """
	keyboard.press_and_release('windows')

	print("Showing task bar.")

# add button
Button(win, text=(" " * 30) + "Exit" + (" " * 30), command=handleClick).pack()


def setOnTop():
	if 7 < datetime.datetime.now().time().hour < 12+5:
		win.attributes('-topmost', True)
		print("on top")
	win.after(1000, setOnTop)

win.after(1000, setOnTop)

# Make the window jump above all
# while 1:
	
# 	# same as non-blocking win.mainloop
# 	win.update_idletasks()
# 	win.update()

win.mainloop()
