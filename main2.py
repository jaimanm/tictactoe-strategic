from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Strategic TicTacToe')

def checkWin(boardNum):
    pass

def disableButtons(position):
    for x in range(9):
        for y in range(9):
            if x == position[1]:
                buttons[x][y].config(state=NORMAL)
            else:
                buttons[x][y].config(state=DISABLED)

def bClick(b):
    global clicked
    for i in buttons:
        if b in i:
            position = [buttons.index(i), i.index(b)]
    if clicked:
        b['text'] = 'X'
        color = 'blue'
    else:
        b['text'] = 'O'
        color = 'red'
    b['bg'] = color
    disableButtons(position)
    clicked = not clicked
    boardCounts[position[0]] += 1
    checkWin(position[0])

def reset():
    global frames, buttons, clicked, boardCounts
    clicked = True # X goes first
    # create 9 frames with a tictactoe board in each
    boardCounts = [0] * 9
    frames = []
    buttons = []
    for i in range(3):
        for j in range(3):
            index = 3*i+j
            f = Frame(
                master=root,
                bg='SystemButtonFace',
                highlightbackground='black',
                highlightthickness=2
            )
            f.grid(row=i, column=j)
            frames.append(f)
            buttons.append([])
            for x in range(3):
                for y in range(3):
                    index2 = 3*x+y
                    b = Button(
                        master=f,
                        text=' ',
                        width=6,
                        height=3,
                        # relief=SOLID,
                        # borderwidth=2
                    )
                    b.grid(row=x, column=y)
                    b.configure(command=lambda b=b: bClick(b))
                    buttons[index].append(b)


reset()
root.mainloop()