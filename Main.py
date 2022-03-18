from tkinter import *

root = Tk()
root.title('Strategic TicTacToe')

frames = [None] * 9
for i in range(3):
    for j in range(3):
        frames[3*i+j] = Frame(
            master=root,
            height=50,
            width=100,
            bg='SystemButtonFace',
            highlightbackground='black',
            highlightthickness=2
        ).grid(row=i, column=j)
        Label(
            master=frames[3*i+j],
            text='label',
            font=('Helvetica', 20), height=3, width=6, bg='red'
        ).grid(row=i,column=j)

root.mainloop()