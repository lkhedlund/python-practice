# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial: 02

"""
TITLE: Circle colour changer
EDITING AUTHOR: Lars Hedlund
FEATURES: Changes the colour of three circle when the button is pressed.
VERSION: 0.0
BUGS: None
"""

# Author:  James Tam
# Version: November 21, 2013
#
# Drawing simple primitive shapes and setting their properties
# Creating 'animations' by moving shapes on the drawing canvas

from tkinter import *
from random import randint

WINDOW_WIDTH = 270 # 10 pixels on either side of each circle
WINDOW_HEIGHT = 100

# Create a window containing the control button
buttonWindow = Frame()
aButton = Button(buttonWindow)

# Create an animation window with certain visual characteristics
animationWindow = Tk()
aDrawingCanvas = Canvas(animationWindow,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,bg ="grey")

###############################################################
# Define any necessary functions here
###############################################################
def random_colour():
    # AUTHOR: Lars Hedlund
    # FUNCTION: Sets three variables to a random colour
    # RETURNS: string, string, string

    colours = ["violet", "PeachPuff4", "maroon", "red", "gold", \
    "lawn green", "cyan", "midnight blue", "dark green", "orange", \
    "DeepPink2", "blue"]

    # Colours are randomely selected from the list, but only in a
    # small range to ensure that the colours are different
    colour1 = colours[randint(0, 3)]
    colour2 = colours[randint(4, 7)]
    colour3 = colours[randint(8, 11)]

    return colour1, colour2, colour3

def create_circles():
    # AUTHOR: Lars Hedlund
    # FUNCTION: Draws three circles in a window

    global aDrawingCanvas
    colour1, colour2, colour3 = random_colour()
    aDrawingCanvas.create_oval(10, 20, 80, 90, fill=colour1, tag="oval1")
    aDrawingCanvas.create_oval(100, 20, 170, 90, fill=colour2, tag="oval2")
    aDrawingCanvas.create_oval(190, 20, 260, 90, fill=colour3, tag="oval3")

def change_colour():
    # AUTHOR: Lars Hedlund
    # FUNCTION: Changes the colour of each circle

    global aDrawingCanvas
    # different colour options are defined by changing the order
    colour3, colour1, colour2 = random_colour()
    # button press output to screen
    print("Changing colours to %r, %r, %r" % (colour1, colour2, colour3))
    # changes each circle
    aDrawingCanvas.itemconfig("oval1", fill=colour1)
    aDrawingCanvas.itemconfig("oval2", fill=colour2)
    aDrawingCanvas.itemconfig("oval3", fill=colour3)

def start():
    global buttonWindow
    global aButton

    # Draw window and start the gui
    buttonWindow.pack()
    aButton['text'] = "Press to change colors"
    aButton['command'] = change_colour
    aButton.grid(row=0, column=0)
    aDrawingCanvas.pack()
    create_circles()
    ###########################################################
    # Make any modifications to this function before this point
    ###########################################################

    animationWindow.mainloop()
    buttonWindow.mainloop()

start()
