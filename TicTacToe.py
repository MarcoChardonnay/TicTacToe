#python program that draws an X when the user clicks with left button of mouse and O when user clicks with right button of mouse on the canvas
#using tkinter and python

#TODO: make a hitbox for the X and O (don't want to draw on the lines)
#TODO: make a tutorial on how to play the game
#TODO: make a menu
#TODO: make a score board
#TODO: make a game mode where you can play against the computer

#canvas dimensions
canvas_width = 800
canvas_height = 1000

from tkinter import *

root = Tk()

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

#divide canvas into 9 squares
def drawGrid():
    canvas.create_line(0, 266, 800, 266, width=5)
    canvas.create_line(0, 533, 800, 533, width=5)
    canvas.create_line(266, 0, 266, 800, width=5)
    canvas.create_line(533, 0, 533, 800, width=5)
    drawResetButton()

def drawX(event):
    # get the x and y coordinates of the mouse
    x = event.x
    y = event.y
    #draw X in red
    canvas.create_line(x-40, y-40, x+40, y+40, fill="red", width=5)
    canvas.create_line(x-40, y+40, x+40, y-40, fill="red", width=5)

def drawO(event):
    # get the x and y coordinates of the mouse
    x = event.x
    y = event.y
    #draw O in blue
    canvas.create_oval(x-40, y-40, x+40, y+40, outline="green", width=5)

def drawOnClickX(event):
    x = event.x
    y = event.y
    if x < 266:
        if y < 266:
            if figures[0][0] == 0:
                figures[0][0] = 1
                drawX(event)
        elif y < 533:
            if figures[1][0] == 0:
                figures[1][0] = 1
                drawX(event)
        else:
            if figures[2][0] == 0:
                figures[2][0] = 1
                drawX(event)
    elif x < 533:
        if y < 266:
            if figures[0][1] == 0:
                figures[0][1] = 1
                drawX(event)
        elif y < 533:
            if figures[1][1] == 0:
                figures[1][1] = 1
                drawX(event)
        else:
            if figures[2][1] == 0:
                figures[2][1] = 1
                drawX(event)
    else:
        if y < 266:
            if figures[0][2] == 0:
                figures[0][2] = 1
                drawX(event)
        elif y < 533:
            if figures[1][2] == 0:
                figures[1][2] = 1
                drawX(event)
        else:
            if figures[2][2] == 0:
                figures[2][2] = 1
                drawX(event)

def drawOnClickO(event):
    x = event.x
    y = event.y
    if x < 266:
        if y < 266:
            if figures[0][0] == 0:
                figures[0][0] = 2
                drawO(event)
        elif y < 533:
            if figures[1][0] == 0:
                figures[1][0] = 2
                drawO(event)
        else:
            if figures[2][0] == 0:
                figures[2][0] = 2
                drawO(event)
    elif x < 533:
        if y < 266:
            if figures[0][1] == 0:
                figures[0][1] = 2
                drawO(event)
        elif y < 533:
            if figures[1][1] == 0:
                figures[1][1] = 2
                drawO(event)
        else:
            if figures[2][1] == 0:
                figures[2][1] = 2
                drawO(event)
    else:
        if y < 266:
            if figures[0][2] == 0:
                figures[0][2] = 2
                drawO(event)
        elif y < 533:
            if figures[1][2] == 0:
                figures[1][2] = 2
                drawO(event)
        else:
            if figures[2][2] == 0:
                figures[2][2] = 2
                drawO(event)

#check if canvas is not empty
def checkIfCanvasIsNotEmpty():
    for i in range(3):
        for j in range(3):
            if figures[i][j] == 0:
                return True
    return False

#check if canvas is full
def checkIfCanvasIsFull():
    for i in range(3):
        for j in range(3):
            if figures[i][j] == 0:
                return False
    return True

#check if there is a winner and put the winner in a string "StrWinner"
def checkWinner():
    #check if there is a winner on the rows
    for i in range(3):
        if figures[i][0] == figures[i][1] and figures[i][1] == figures[i][2]:
            if figures[i][0] == 1:
                return "X"
            elif figures[i][0] == 2:
                return "O"
    #check if there is a winner on the columns
    for i in range(3):
        if figures[0][i] == figures[1][i] and figures[1][i] == figures[2][i]:
            if figures[0][i] == 1:
                return "X"
            elif figures[0][i] == 2:
                return "O"
    #check if there is a winner on the diagonals
    if figures[0][0] == figures[1][1] and figures[1][1] == figures[2][2]:
        if figures[0][0] == 1:
            return "X"
        elif figures[0][0] == 2:
            return "O"
    if figures[0][2] == figures[1][1] and figures[1][1] == figures[2][0]:
        if figures[0][2] == 1:
            return "X"
        elif figures[0][2] == 2:
            return "O"
    #check if there is a draw
    for i in range(3):
        for j in range(3):
            if figures[i][j] == 0:
                return ""
    return "draw"

#game reset
def resetGame():
    global figures
    figures = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    canvas.delete("all")
    drawGrid()
    canvas.bind("<Button-1>", drawOnClickX)
    canvas.bind("<Button-3>", drawOnClickO)
    StrWinner = ""
    checkForWinner()

#draw reset button on bottom right corner
def drawResetButton():
    resetButton = Button(root, text="Reset", command=resetGame, height=5, width=10, bg="light blue", fg="dark blue", font="Verdana 12 bold")
    resetButton.place(x=650, y=850)

#display the winner on the canvas from height 800 to 1000
def displayWinner(StrWinner):
    #check if there is a winner (StrWinner is not "draw")
    if StrWinner != "draw":
        canvas.create_text(400, 900, text=StrWinner + " wins!", font=("Verdana", 50), fill="blue")
        #disable the canvas
        canvas.unbind("<Button-1>")
        canvas.unbind("<Button-3>")

    #check if there is a draw (StrWinner is "draw")
    else:
        canvas.create_text(400, 900, text="Draw!", font=("Verdana", 50), fill="purple")
        #disable the canvas
        canvas.unbind("<Button-1>")
        canvas.unbind("<Button-3>")

#check if there is a winner every 500ms only if the canvas is not empty
def checkForWinner():
    if checkIfCanvasIsNotEmpty():
        StrWinner = checkWinner()
        if StrWinner != "":
            displayWinner(StrWinner)
        else:
            root.after(500, checkForWinner)
    #if canvas is full and there is no winner, display "draw"
    elif checkIfCanvasIsFull():
        displayWinner("draw")

#start the game
resetGame()
    
root.mainloop()