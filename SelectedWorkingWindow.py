from tkinter import *
from tkinter import ttk
import sqlite3
import MainWindow
from tkinter.messagebox import showwarning
from MainWindow import *
from LogPassWindow import *
import LogPassWindow

class SelectedWorkingWindow(Tk):

    textFromTextBox=""
    LogPassWindow=LogPassWindow
    checkIfDestroed = False

    def __init__(self):
        super().__init__()

        self.connect = LogPassWindow.MainWindow.connect

        self.entrysList = list()
        self.selectedPeopleList = LogPassWindow.MainWindow.selectedPeopleList.copy()
        self.columns = LogPassWindow.MainWindow.columns

        self.title("Bibki 3D - Selected work window")
        self.geometry("800x300")

        self.label = ttk.Label(self, text="Измените строку в окне ниже. Нажмите \"Сохранить\" когда закончите")
        self.label.pack(expand=1,side=TOP)

        for x in range(len(self.selectedPeopleList)):
            self.entry = ttk.Entry(self,name="entry_"+str(x), state=NORMAL)
            self.entry.insert(0,f"{self.selectedPeopleList[x]}")
            self.entry.pack(expand=1,side=LEFT)
            self.entrysList.append(self.entry)

        self.BT_save = ttk.Button(self, text="Сохранить", command=self.BT_save)
        self.BT_save.pack(expand=1,side=BOTTOM)

    def BT_save(self):

        self.cursor = self.connect.cursor()
        for x in range(len(self.columns)):
            self.cursor.execute("UPDATE People SET %(first)s = '%(second)s' WHERE ID = '%(third)s'" % {"first": self.columns[x], "second": self.entrysList[x].get(), "third": self.selectedPeopleList[0]})
            self.connect.commit()
        SelectedWorkingWindow.checkIfDestroed=True
        self.destroy()