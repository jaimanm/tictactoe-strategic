from tkinter import *
from tkinter import messagebox

class Board:
    def __init__(self, frame, frameNumber, clicked):
        self.player = clicked
        self.win = None
        self.count = 0
        self.frame = frame
        self.frameNumber = frameNumber
        self.buttons = []
        for x in range(3):
            for y in range(3):
                index = x*3+y
                b = Button(
                    master=frame,
                    # text=str(frameNumber) + '.' + str(index),
                    text=' ',
                    width=6,
                    height=3
                )
                b.grid(row=x, column=y)
                b.configure(command=lambda b=b: self.bClick(b))
                self.buttons.append(b)

    def updatePlayer(self, clicked):
        self.player = clicked

    def disableButtons(self, winner):
        if winner == 'X':
            color = 'blue'
        elif winner == 'O':
            color = 'red'
        else:
            color = 'grey'
        
        for b in self.buttons:
            b['bg'] = color
            b.configure(state=DISABLED)


    def checkWin(self):
        self.win = False
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
        for i in winConditions:
            if self.buttons[i[0]]['text'] == self.buttons[i[1]]['text'] == self.buttons[i[2]]['text'] and not self.buttons[i[0]]['text'] == ' ':
                self.win = True
                self.disableButtons(self.buttons[i[0]]['text'])
            if self.count == 9 and self.win == False:
                self.disableButtons(' ')

    def bClick(self, b):
        if b['text'] == ' ':
            if self.player == True: b['text'] = 'X'
            else: b['text'] = 'O'
            self.player = -self.player
            self.count += 1
            self.checkWin()
        else:
            messagebox.showerror('Tic Tac Toe', 'Spot is taken.\nTry Again...')