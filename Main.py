from tkinter import *

root = Tk()
root.title('Strategic TicTacToe')

# make the buttons
frames = [None] * 9
buttons = [[None] * 9] * 9
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
        for x in range(3):
            for y in range(3):
                index2 = x*3+y
                buttons[index][index2] = Button(
                    frames[index],
                    text=str(index*9 + index2 + 1),
                    width=6,
                    height=3,
                    # command=lambda: buttonClick()
                )
                buttons[index][index2].grid(row=x, column=y)

root.mainloop()