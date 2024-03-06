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

    def __init__(self):
        super().__init__()

        self.textExampleOld = list()
        self.textExampleNew = list()
        for x in LogPassWindow.MainWindow.selectedPeopleList:
            self.textExampleOld.append(x)
        self.textSaver = LogPassWindow.MainWindow.selectedPeople

        for x in self.textExampleOld[0]:
            if isinstance(x,int) == True:
                 self.textExampleNew.append(0)
            elif isinstance(x,str) == True:
                self.textExampleNew.append("")
            elif isinstance(x,float) == True:
                self.textExampleNew.append(0.0)

        self.title("Bibki 3D - Selected work window")
        self.geometry("800x500")

        self.label = ttk.Label(self, text="Измените строку в окне ниже. Нажмите \"Сохранить\" когда закончите")
        self.label.pack(expand=1)

        self.editTextWindow = Text(self)
        self.editTextWindow.pack(expand=1)
        self.editTextWindow.insert(1.0, LogPassWindow.MainWindow.selectedPeople)

        self.BT_save = ttk.Button(self, text="Сохранить", command=self.BT_save)
        self.BT_save.pack(expand=1)

    def BT_save(self):
        self.tempTextForOld = "["
        for x in self.textExampleOld[0]:
            if isinstance(x,int) or isinstance(x,float) == True:
                 self.tempTextForOld += str(0)
            elif isinstance(x,str) == True:
                self.tempTextForOld += ""
            self.tempTextForOld+=", "
        self.tempTextForOld+="]"
        self.tempTextFor = "["
        for x in self.textExampleNew:
            if isinstance(x, int) or isinstance(x, float) == True:
                self.tempTextFor += str(0)
            elif isinstance(x, str) == True:
                self.tempTextFor += ""
            self.tempTextFor += ", "
        self.tempTextFor += "]"
        if self.editTextWindow.get("1.0",END) == self.tempTextFor:
            SelectedWorkingWindow.textFromTextBox = self.editTextWindow.get("1.0",END)
            print("good work")
        else:
            showwarning(title="Неверный логин или пароль", message="Неверный логин или пароль, попробуйте снова")
