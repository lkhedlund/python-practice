# Author:  James Tam
# Version: November 21, 2013
#
# Drawing simple primitive shapes and setting their properties
# Creating 'animations' by moving shapes on the drawing canvas


from tkinter import *

def createShapes(aDrawingCanvas):
    # Shape's first four properties: Top LHS(x,y),Bottom RHS(x,y)
    aDrawingCanvas.create_rectangle(10,10,100,50)
    aDrawingCanvas.create_oval(50,100,200,90, fill = "red")


    aDrawingCanvas.create_text(200,250, text="Tam's boring text msg: I clash btw", font = "Times 12 bold underline",fill="green")
    aDrawingCanvas.create_rectangle(300,100,200,200,fill = "orange",outline="blue",tag="rect2")

    # Point 1(x1,y2), Point 2(x2,y2)
    aDrawingCanvas.create_line(1,1,100,200)

def animate(aDrawingCanvas):
    input("Hit enter to see rectangle two move")
    aDrawingCanvas.move("rect2",100,300)


def start():
    # Create a window with certain visual characteristics
    window = Tk()
    window.title("Tamj's gui example")   # Label the title bar
    aDrawingCanvas = Canvas(window,width=640,height=480,bg ="grey")
    createShapes(aDrawingCanvas)

    # Draw window and start the gui
    aDrawingCanvas.pack()
    animate(aDrawingCanvas)

    window.mainloop()

start()
