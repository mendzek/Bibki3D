from tkinter import *
from tkinter import ttk
import sqlite3
import LogPassWindow
from MainWindow import *


class NewColumnWindow(Tk):

    def __init__(self):
        super().__init__()

        self.list = ["Integer","Text"]

        self.title("Bibki3D - New column")
        self.geometry("350x300")

        self.entry = ttk.Entry(self)
        self.entry.pack(expand=1, side=LEFT)

        self.SpinBox = ttk.Spinbox(self,values=self.list)
        self.SpinBox.pack(expand=1, side=RIGHT)

        self.BT_OK = ttk.Button(self, text="Сохранить", command=self.BT_OK)
        self.BT_OK.pack(expand=1, side=BOTTOM)

    def BT_OK(self):
        self.connect = LogPassWindow.MainWindow.connect
        self.cursor = self.connect.cursor()
        self.cursor.execute("ALTER TABLE People ADD %(first)s %(second)s" % {"first":self.entry.get(), "second":self.SpinBox.get()})
        self.connect.commit()
        self.destroy()



