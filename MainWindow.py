from tkinter import *
from tkinter import ttk
import sqlite3
from SelectedWorkingWindow import *
from NewColumnWindow import *
from NewRowWindow import *

class MainWindow(Tk):

    selectedPeople = ""
    selectedPeopleList = list()
    columns = tuple()
    connect = sqlite3.connect

    def __init__(self):
        super().__init__()

        self.tableValues=list()
        self.headValues=list()
        self.numOfRows=any
        self.selectedPeople = ""

        self.mainMenu = Menu(self)
        self.editMenu = Menu(self,tearoff=0)
        self.editMenu.add_cascade(label="Edit table",command=self.menuEdit)
        self.mainMenu.add_cascade(label="Edit",menu=self.editMenu)

        self.AddMenu = Menu(self, tearoff=0)
        self.AddMenu.add_cascade(label="Add row", command=self.menuAddRow)
        self.AddMenu.add_cascade(label="Add column", command=self.menuAddColumn)

        self.mainMenu.add_cascade(label="Add", menu=self.AddMenu)

        self.mainMenu.add_cascade(label="Update Table", command=self.menuUpdateTable)

        self.title("Bibki 3D - Work window")
        self.geometry("1000x500")
        self.config(menu=self.mainMenu)

        self.label=ttk.Label(self,text="asd")
        self.label.pack(anchor=N, fill=X,expand=1)

    def menuEdit(self):
            MainWindow.selectedPeople = self.selectedPeople
            selectedWorkingWindow = SelectedWorkingWindow()

    def menuAddRow(self):
        newRowWindow = NewRowWindow()

    def menuAddColumn(self):
        newColumnWindow = NewColumnWindow()

    def menuUpdateTable(self):
        mainWindow=MainWindow()
        mainWindow.tableViewInsert()
        self.destroy()

    def tableViewInsert(self):
        self.connect = sqlite3.connect("D:\\Sqlite\\databases\\db_bibki.db", timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        MainWindow.connect = self.connect
        self.cursor = self.connect.cursor()
        MainWindow.columns = self.connect.
        self.tree = ttk.Treeview(self, columns=MainWindow.columns, show="headings")
        self.tree.pack(fill=BOTH, expand=1)
        for x in MainWindow.columns:
            self.tree.heading(x,text=x)

        self.tree.bind("<<TreeviewSelect>>", self.select)

        for x in self.tree.get_children():
            self.tree.delete(x)

        self.cursor.execute("SELECT COUNT(*) FROM People")
        self.numOfRows = self.cursor.fetchone()
        self.headValues.extend(MainWindow.columns)
        self.checkTemp=False
        for x in range(self.numOfRows[0]+1):
            self.cursor.execute(f"SELECT * FROM People WHERE id={x}")
            self.tableValues.append(self.cursor.fetchone())
            if self.tableValues[0]==None and self.checkTemp==False:
                self.checkTemp=True
                self.tableValues.clear()
        for x in self.tableValues:
            self.tree.insert("", END, values=x)

    def select(self,event):
        for selected_item in self.tree.selection():
            MainWindow.selectedPeopleList.clear()
            self.selectedPeople = ""
            self.item = self.tree.item(selected_item)
            self.person = self.item["values"]
            MainWindow.selectedPeopleList = self.item["values"].copy()
            self.selectedPeople = f"{self.selectedPeople}{self.person}\n"
        self.label["text"] = self.selectedPeople
        print(self.selectedPeople)

