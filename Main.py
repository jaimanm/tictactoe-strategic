from tkinter import *
from Board import Board

root = Tk()
root.title('Strategic TicTacToe')

def setup():
    # create 9 frames with a tictactoe board in each
    frames = [None] * 9
    boards= [None] * 9
    for i in range(3):
        for j in range(3):
            index = 3*i+j
            frames[index] = Frame(
                master=root,
                bg='SystemButtonFace',
                highlightbackground='black',
                highlightthickness=2
            )
            frames[index].grid(row=i, column=j)
            boards[index] = Board(frames[index], index)

setup()
root.mainloop()