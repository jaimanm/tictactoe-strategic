from tkinter import *

root = Tk()
root.title('Strategic TicTacToe')

frames = [None] * 9
buttons = [[None] * 9] * 9
count = 0
for i in range(3):
    for j in range(3):
        index = 3*i+j
        frames[index] = Frame(
            master=root,
            height=50,
            width=100,
            bg='SystemButtonFace',
            highlightbackground='black',
            highlightthickness=2
        )
        frames[index].grid(row=i, column=j)
        print(frames[index])
        print(i, j)
        for x in range(3):
            for y in range(3):
                index2 = x*3+y
                buttons[index][index2] = Button(frames[index], text=str(index*9 + index2 + 1))
                buttons[index][index2].grid(row=x, column=y)
                print(buttons[index][index2])
                print(x, y)
                count+=1

root.mainloop()