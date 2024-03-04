from tkinter import *
from tkinter import ttk
import sqlite3

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.check = False
        self.tableValues=list()
        self.headValues=list()

        self.mainMenu = Menu(self)
        self.editMenu = Menu(self,tearoff=0)
        self.editMenu.add_cascade(label="Edit table",command=self.menuEdit)
        self.editMenu.add_cascade(label="Save table")
        self.mainMenu.add_cascade(label="Edit",menu=self.editMenu)

        self.title("Bibki 3D - Work window")
        self.geometry("800x500")
        self.config(menu=self.mainMenu)

        self.connect = sqlite3.connect("D:\\Sqlite\\databases\\db_bibki.db", timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True,factory=sqlite3.Connection, cached_statements=128, uri=False)
        self.cursor = self.connect.cursor()
        self.columns = ("id", "Full_name", "exp", "salary", "position")
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        self.tree.heading("id", text="ID")
        self.tree.heading("Full_name", text="Full name")
        self.tree.heading("exp", text="Experience")
        self.tree.heading("salary", text="Salary")
        self.tree.heading("position", text="Position")

        self.cursor.execute("SELECT COUNT(*) FROM People")
        self.numOfRows = self.cursor.fetchone()
        self.headValues.extend(self.columns)
        for y in range(len(self.headValues)):
            for x in self.numOfRows:
                self.cursor.execute(f"SELECT {self.headValues[y]} FROM People WHERE id={x}")
                self.tableValues.extend(self.cursor.fetchone())

        for x in range(len(self.tableValues)):
            self.tree.insert("", END, values=self.tableValues[x])
    def menuEdit(self):
        if(self.check==False):
            self.check=True
            #сделать эдит таблицы
        else:
            self.check=False
            #сделать конец эдита таблицы

    def menuSave(self):
        #сделать сейв таблицы в файл
        pass