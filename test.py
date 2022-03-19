from tkinter import * 

root = Tk()

f = Frame(root, bg = "red", highlightbackground='black', highlightthickness=2, width=100)
f.grid(row=0, column=0)
f2 = Frame(root, bg='blue', highlightbackground='black', highlightthickness=2, width=50)
f2.grid(row=1, column=1)

b = Button(f, text = "1")
b.grid(row=0, column=0)
b2 = Button(f, text = "2")
b2.grid(row=0, column=1)

# b3 = Button(f2, text='3')
# b3.grid(row=0, column=0)

buttons = [None] * 9
for i in range(3):
    buttons[i] = Button(f2, text = str(i))
    buttons[i].grid(row=i, column=0)
    print(buttons[i])


root.mainloop()