from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Strategic TicTacToe')

def endGame():
    pass

def checkWin(boardNum):
    global count
    board = buttons[boardNum]
    winConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    winBoard = False
    for i in winConditions:
        if board[i[0]] == board[i[1]] == board[i[2]] and not board[i[0]]['text'] == ' ':
            boardWinners[boardNum] = board[i[0]]['text']
            winBoard = True
            count += 1
    if boardCounts[boardNum] == 9 and winBoard == True:
        boardWinners[boardNum] = ' '

    for i in winConditions:
        if boardWinners[i[0]] == boardWinners[i[1]] == boardWinners[i[2]] and not boardWinners[i[0]] == None and not boardWinners[i[0]] == ' ':
            endGame()
    pass

def disableButtons(position):
    for i in range(len(buttons)):
        for j in buttons[i]:
            if i == position[1]:
                if j['text'] == ' ':
                    j.config(state=NORMAL)
                else:
                    j.config(state=DISABLED)
            else:
                j.config(state=DISABLED)

    for i in range(len(frames)):
        if i == position[1]:
            frames[i]['highlightbackground'] = 'green'
        else:
            frames[i]['highlightbackground'] = 'black'

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
    global frames, buttons, clicked, boardCounts, boardWinners, count
    boardWinners = [None] * 9
    count = 0
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
                highlightthickness=3
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
                        width=5,
                        height=2,
                        font='Helvetica 15 bold'
                    )
                    b.grid(row=x, column=y)
                    b.configure(command=lambda b=b: bClick(b))
                    buttons[index].append(b)


reset()
root.mainloop()