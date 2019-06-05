from tkinter import *
from Box import Box
import random
import Solver

window = None
canvas = None
cWidth = 450
cHeight = 450
boxSize = 50

boxes = []
puzzleArray = []


def findBoxByCoords(row, col):
    for box in boxes:
        if(box.row == row and box.col == col):
            return box

    return None


def boxClicked(event):

    num = canvas.find_withtag(CURRENT)[0]
    # print(num)
    res = 0
    temp = num % 2
    if(temp == 1):
        res = num - 1
    else:
        res = num - 2

    res = int(res / 2)

    box = boxes[res]
    # print(box)

    box.increase()

    if(temp == 1):
        num += 1

    if(box.num == 0):
        canvas.itemconfig(num, text="")
    else:
        canvas.itemconfig(num, text=str(box.num))

    createPuzzleArray()


def createPuzzleArray():
    global puzzleArray
    arr = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for k in range(9):
            arr[k][i] = boxes[(i * 9) + k].num

    puzzleArray = arr

    # Solver.printArray(arr)


def redrawPuzzle():
    for i in range(9):
        for k in range(9):
            box = boxes[(i * 9) + k]
            box.num = puzzleArray[i][k]
            canvas.itemconfig((((k * 9) + i) + 1) * 2, text=str(puzzleArray[i][k]))



def startSolver():
    global puzzleArray
    puzzleArray = Solver.solve(puzzleArray)

    redrawPuzzle()

def clearPuzzle():
    for i in range(9):
        for k in range(9):
            box = boxes[(i * 9) + k]
            box.num = 0
            canvas.itemconfig((((k * 9) + i) + 1) * 2, text="")

    createPuzzleArray()

def setupWindow():
    global canvas, boxes, window

    win = Tk()
    win.title = "Sudoku Solver"

    canvas = Canvas(win, width=cWidth, height=cHeight)
    canvas.pack()

    for row in range(0, 9):
        for col in range(0, 9):
            rand = random.randint(1, 9)

            rect = canvas.create_rectangle(row * boxSize, col * boxSize, (row + 1)
                                           * boxSize, (col + 1) * boxSize, fill="white", outline="gray", tag="box")

            text = canvas.create_text(row * boxSize + (boxSize / 2), col * boxSize + (
                boxSize / 2), font=("Times new roman", 22), text="", tag="box")

            box = Box(0, row, col)
            boxes.append(box)

    canvas.tag_bind("box", "<Button-1>", boxClicked)

    # Create borders of sections
    canvas.create_line(boxSize * 3, 0, boxSize * 3, cHeight, width="2")
    canvas.create_line(boxSize * 6, 0, boxSize * 6, cHeight, width="2")
    canvas.create_line(0, boxSize * 3, cWidth, boxSize * 3, width="2")
    canvas.create_line(0, boxSize * 6, cWidth, boxSize * 6, width="2")

    separator = Frame(height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)

    buttonFrame = Frame()
    buttonFrame.pack()

    startButton = Button(buttonFrame, text="Start Solving", command=startSolver)
    startButton.pack(side=LEFT, anchor=W, padx=20)

    clearButton = Button(buttonFrame, text="Clear Puzzle", command=clearPuzzle)
    clearButton.pack(side=LEFT, anchor=E, padx=20)

    createPuzzleArray()

    win.mainloop()


if __name__ == "__main__":
    setupWindow()
