from tkinter import *
from Box import Box

window = None
canvas = None
cWidth = 450
cHeight = 450
boxSize = 50

boxes = []

def findBoxByCoords(row, col):
    for box in boxes:
        if(box.row == row and box.col == col):
            return box
    
    return None

def fillStartingNumbers():
    



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
    
    print(res)

def setupWindow():
    global canvas, boxes, window

    win = Tk()
    win.title = "Sudoku Solver"

    canvas = Canvas(win, width=cWidth, height=cHeight)
    canvas.pack()

    for row in range(0, 9):
        for col in range(0, 9):
            rect = canvas.create_rectangle(row * boxSize, col * boxSize, (row + 1)
                                           * boxSize, (col + 1) * boxSize, fill="white", outline="gray", tag="box")

            text = canvas.create_text(row * boxSize + (boxSize / 2), col * boxSize + (
                boxSize / 2), font=("Times new roman", 22), text="", tag="box")

            box = Box(-1, row, col)
            boxes.append(box)

            

    canvas.tag_bind("box", "<Button-1>", boxClicked)

    # Create borders of sections
    canvas.create_line(boxSize * 3, 0, boxSize * 3, cHeight, width="2")
    canvas.create_line(boxSize * 6, 0, boxSize * 6, cHeight, width="2")
    canvas.create_line(0, boxSize * 3, cWidth, boxSize * 3, width="2")
    canvas.create_line(0, boxSize * 6, cWidth, boxSize * 6, width="2")

    fillStartingNumber()
    

    win.mainloop()

def setupInputWindow():
    global window

    window = Tk()

    canvas = Canvas(window, width=cWidth, height=cHeight)
    canvas.pack()

            






if __name__ == "__main__":
    # setupInputWindow()
    setupWindow()
