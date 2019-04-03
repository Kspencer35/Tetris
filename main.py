from tkinter import *


class Tetris:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.blue = PhotoImage(file='')
        self.label = Label(frame, image=self.blue)
        self.label.pack()

        self.label1 = Label(frame, image='', bg="black", width=400, height=200)
        self.label1.pack()

        self.btn = Button(self.label1, text='Button', command=self.printmess)
        self.btn.place(relx=.1, rely=.1, )

    def printmess(self):
        print('Yes!')


root = Tk()
t = Tetris(root)
root.mainloop()
