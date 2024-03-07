from tkinter import *
from tkinter import ttk

import LogPassWindow


class NewColumnWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Bibki3D - New column")
        self.geometry("350x300")

        self.entry = ttk.Entry(self)
        self.entry.pack(expand=1, side=TOP)

        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.pack(expand=1, side=BOTTOM)

    def BT_OK(self):
        LogPassWindow.MainWindow.columns += (self.entry.get(),)
        self.destroy()



