from tkinter import *
from tkinter import ttk
import sqlite3
import SelectedWorkingWindow

class MainWindow(Tk):

    selectedPeople=""

    def __init__(self):
        super().__init__()

        self.check = False
        self.tableValues=list()
        self.headValues=list()
        self.numOfRows=any
        self.selectedPeople = ""

        self.mainMenu = Menu(self)
        self.editMenu = Menu(self,tearoff=0)
        self.editMenu.add_cascade(label="Edit table",command=self.menuEdit)
        self.editMenu.add_cascade(label="Save table", command=self.menuSave)
        self.mainMenu.add_cascade(label="Edit",menu=self.editMenu)

        self.title("Bibki 3D - Work window")
        self.geometry("800x500")
        self.config(menu=self.mainMenu)

        self.label=ttk.Label(self,text="asd")
        self.label.pack(anchor=N, expand=1)

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

        self.tree.bind("<<TreeviewSelect>>", self.select)

    def menuEdit(self):
        if(self.check==False):
            self.check=True
            MainWindow.selectedPeople = self.selectedPeople
            self.selectedWorkingWindow = SelectedWorkingWindow
            #сделать эдит таблицы
        else:
            self.check=False
            #сделать конец эдита таблицы

    def menuSave(self):
        #сделать сейв таблицы в файл
        pass

    def tableViewInsertStart(self):
        self.cursor.execute("SELECT COUNT(*) FROM People")
        self.numOfRows = self.cursor.fetchone()
        self.headValues.extend(self.columns)
        self.checkTemp=False
        for x in range(self.numOfRows[0]):
            self.cursor.execute(f"SELECT * FROM People WHERE id={x}")
            self.tableValues.append(self.cursor.fetchone())
            if self.tableValues[0]==None and self.checkTemp==False:
                self.checkTemp=True
                self.tableValues.clear()
        for x in self.tableValues:
            self.tree.insert("", END, values=x)

    def select(self,event):

        for selected_item in self.tree.selection():
            self.item = self.tree.item(selected_item)
            self.person = self.item["values"]
            self.selectedPeople = f"{self.selectedPeople}{self.person}\n"
        self.label["text"] = self.selectedPeople
        print(self.selectedPeople)

