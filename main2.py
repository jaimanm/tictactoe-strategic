from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Strategic TicTacToe')

def endGame():
    if winner == ' ': messagebox.showinfo('TicTacToe Strategic', "It's a tie.")
    elif winner == 'X' or winner == 'O': messagebox.showinfo('TicTacToe Strategic', winner + ' has won!')
    if not winner == None:
        turnLabel['text'] = 'Game Over'
        updateLabel['text'] = 'Reset to Play Again.'

def checkWin(boardNum):
    global count, winner
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
        if board[i[0]]['text'] == board[i[1]]['text'] == board[i[2]]['text'] and not board[i[0]]['text'] == ' ':
            updateLabel['text'] = board[i[0]]['text'] + ' wins on board ' + str(boardNum+1)
            boardWinners[boardNum] = board[i[0]]['text']
            winBoard = True
            count += 1
            break
    if boardCounts[boardNum] == 9 and winBoard == False:
        updateLabel['text'] = 'tie on board ' + str(boardNum)
        boardWinners[boardNum] = ' '
        count += 1
        winBoard = True

    for i in winConditions:
        if boardWinners[i[0]] == boardWinners[i[1]] == boardWinners[i[2]] and not boardWinners[i[0]] == None:
            winner = boardWinners[i[0]]
    if count == 9:
        winner = ' '

def disableButtons(position):

    # NEW METHOD - CHANGE ONLY WHAT NEEDS TO BE CHANGED
    
    if not winner == None:
        for board in buttons:
            for b in board:
                b.config(state=DISABLED)
        for f in frames:
            f['highlightbackground'] = 'black'
    else:
        # disable board with the clicked button if they just won the board
        if not boardWinners[position[0]] == None:
            frames[position[0]]['highlightbackground'] = 'black'
            for i in buttons[position[0]]:
                if boardWinners[position[0]] == 'X':
                    i['bg'] = 'blue'
                elif boardWinners[position[0]] == 'O':
                    i['bg'] = 'red'
                else:
                    i['bg'] = 'grey'
                i.config(state=DISABLED)
        
        # if the next board has been won, then make all frames available
        if not boardWinners[position[1]] == None:
            for i in range(len(frames)):
                if i == position[1] or not boardWinners[i] == None: frames[i]['highlightbackground'] = 'black'
                else: frames[i]['highlightbackground'] = 'green'
            for i in range(len(buttons)):
                for b in buttons[i]:
                    if i == position[1] or not boardWinners[i] == None or not b['text'] == ' ': b.config(state=DISABLED)
                    else: b.config(state=NORMAL)
        # otherwise make only that frame available
        else:
            for i in range(len(frames)):
                if i == position[1]: frames[i]['highlightbackground'] = 'green'
                else: frames[i]['highlightbackground'] = 'black'
            for i in range(len(buttons)):
                for b in buttons[i]:
                    if i == position[1] and b['text'] == ' ': b.config(state=NORMAL)
                    else: b.config(state=DISABLED)

def close_window():
    root.destroy()
    exit()

def bClick(b):
    global clicked
    for i in buttons:
        if b in i:
            position = [buttons.index(i), i.index(b)]
            break
    if clicked:
        b['text'] = 'X'
        b['bg'] = 'blue'
    else:
        b['text'] = 'O'
        b['bg'] = 'red'
    clicked = not clicked
    if clicked:
        turnLabel['text'] = "Player X's turn"
    else:
        turnLabel['text'] = "Player O's turn"
    
    boardCounts[position[0]] += 1
    checkWin(position[0])
    disableButtons(position)
    endGame()

def reset():
    global frames, buttons, clicked, boardCounts, boardWinners, count, winner, turnLabel, updateLabel
    boardWinners = [None] * 9
    winner = None
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
                highlightbackground='green',
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
    
    turnLabel = Label(
        master=root,
        bg='SystemButtonFace',
        font='Helvetica 10 italic bold',
        text="Player X's turn"
    )
    turnLabel.grid(row=4,column=0)

    updateLabel = Label(
        master=root,
        bg='SystemButtonFace',
        font='Helvetica 10 italic',
        text=''
    )
    updateLabel.grid(row=4, column=1, columnspan=2)
myMenu = Menu(root)
root.config(menu=myMenu)
# create menu
myMenu = Menu(root)
root.config(menu=myMenu)

# create Options menu
optionsMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label='Options', menu=optionsMenu)
optionsMenu.add_command(label='Reset Board', command=reset)
optionsMenu.add_command(label='Exit', command=close_window)

reset()
root.mainloop()