from tkinter import *

root = Tk()
root.title('Strategic TicTacToe')

# Button click method
def buttonClick(button):
    print('button clicked')

buttons = [None] * 9
for i in range(3):
    for j in range(3):
        index = 3 * i + j
        buttons[index] = Button(root, text='b' + str(index), font=('Helvetica', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: buttonClick(buttons[index])).grid(row=i, column=j)

root.mainloop()