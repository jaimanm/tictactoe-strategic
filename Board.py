from tkinter import *

class Board:
    def __init__(self, frame, frameNumber):
        self.frame = frame
        self.frameNumber = frameNumber
        self.buttons = []
        for x in range(3):
            for y in range(3):
                index = x*3+y
                b = Button(
                    master=frame,
                    text=str(frameNumber) + '.' + str(index),
                    width=6,
                    height=3
                )
                b.grid(row=x, column=y)
                b.configure(command=lambda b=b: self.buttonClick(b))
                self.buttons.append(b)
    
    def buttonClick(self, button):
        print('button ' + button['text'] + ' pressed')