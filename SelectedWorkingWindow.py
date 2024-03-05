from tkinter import *
from tkinter import ttk
import sqlite3
from MainWindow import *
class SelectedWorkingWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Bibki 3D - Selected work window")
        self.geometry("800x500")

        self.editTextWindow = Text(self)
        self.editTextWindow.pack(expand=1)
        self.editTextWindow.insert(1,MainWindow.selectedPeople)
