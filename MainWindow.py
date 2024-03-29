from tkinter import *
from tkinter import ttk
import sqlite3
from SelectedWorkingWindow import *
from NewColumnWindow import *
from NewRowWindow import *
from tkinter import filedialog

class MainWindow(Tk):

    sqlPath=""
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
        self.mainMenu.add_cascade(label="Delete selected row", command=self.menuDeleteSelected)

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

    def menuDeleteSelected(self):
        self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                       isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                       cached_statements=128, uri=False)
        self.cursor = self.connect.cursor()
        if(len(self.selectedPeopleList)==0):
            self.label["text"] = "Ничего не выбрано"                #Не работает если удалить строку посередине
        #elif self.selectedPeopleList[0] == max(self.selectedPeopleList):
        #    self.temp = self.cursor.execute("SELECT COUNT(*) FROM People").fetchone()[0]
        #    for x in range(self.temp):
        #        self.cursor.execute("DELETE FROM People WHERE ID = %(first)s; UPDATE People SET %(second)s = '%(third)s' WHERE ID = '%(fourth)s'" % {"first": self.selectedPeopleList[0], "second": self.columns[0], "third": self.selectedPeopleList[x]})
        #        self.connect.commit()
        #    mainWindow = MainWindow()
        #    mainWindow.tableViewInsert(True)
        #    self.destroy()
        else:
            self.cursor.execute("DELETE FROM People WHERE ID = %(first)s" % {"first": self.selectedPeopleList[0]})
            self.connect.commit()
            self.cursor.execute("SELECT COUNT(*) FROM People")
            self.numOfRows = self.cursor.fetchone()
            for x in range(self.numOfRows[0]):
                self.cursor.execute("UPDATE People SET ID = '%(first)s'" % {"first": x})
                self.connect.commit()
            for x in range(self.numOfRows[0]):
                self.cursor.execute("UPDATE People SET ID = '%(first)s' WHERE ID = '%(second)s'" % {"first": x,"second": x})
                self.connect.commit()
            mainWindow=MainWindow()
            mainWindow.tableViewInsert(True)
            self.destroy()

    def menuUpdateTable(self):
        mainWindow=MainWindow()
        mainWindow.tableViewInsert(True)
        self.destroy()

    def tableViewInsert(self,sqlPathExist):

        if(sqlPathExist==False):
            self.sqlPath = filedialog.askopenfilename()
            MainWindow.sqlPath = self.sqlPath
            self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                           isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection,
                                           cached_statements=128, uri=False)
            MainWindow.connect = self.connect
            self.cursor = self.connect.cursor()
            MainWindow.columns = ()
            self.cursor.execute("SELECT COUNT(*) FROM People")
            self.numOfRows = self.cursor.fetchone()[0]
            self.numOfColumns=self.cursor.execute("SELECT COUNT(*) FROM pragma_table_info('People')").fetchone()[0]
            for x in range(self.numOfColumns):
                MainWindow.columns += self.cursor.execute(f"SELECT name FROM pragma_table_info('People') Where cid={x}").fetchone()
            self.tree = ttk.Treeview(self, columns=MainWindow.columns, show="headings")
            self.tree.pack(anchor=S,fill=BOTH, expand=1)
            for x in MainWindow.columns:
                self.tree.heading(x,text=x)

            self.tree.bind("<<TreeviewSelect>>", self.select)

            for x in self.tree.get_children():
                self.tree.delete(x)

            self.headValues.extend(MainWindow.columns)
            self.checkTemp=False

            for x in range(self.numOfRows+1):
                self.cursor.execute(f"SELECT * FROM People WHERE id={x}")
                self.tuple = (x,)
                self.tupleFromDB = self.cursor.fetchone()
                if self.tupleFromDB==None and self.checkTemp==False:
                    self.checkTemp=True
                else:
                    for y in self.tupleFromDB:
                        self.tuple += (y,)
                    self.tableValues.append(self.tuple)
                    del self.tuple
            for x in self.tableValues:
                    self.tree.insert("", END, values=x)
        else:
            self.connect = sqlite3.connect(self.sqlPath, timeout=5.0, detect_types=0,
                                           isolation_level='DEFERRED', check_same_thread=True,
                                           factory=sqlite3.Connection,
                                           cached_statements=128, uri=False)
            MainWindow.connect = self.connect
            self.cursor = self.connect.cursor()
            MainWindow.columns = ("Row number",)
            self.cursor.execute("SELECT COUNT(*) FROM People")
            self.numOfRows = self.cursor.fetchone()[0]
            self.numOfColumns = self.cursor.execute("SELECT COUNT(*) FROM pragma_table_info('People')").fetchone()[0]
            for x in range(self.numOfColumns):
                MainWindow.columns += self.cursor.execute(
                    f"SELECT name FROM pragma_table_info('People') Where cid={x}").fetchone()
            self.tree = ttk.Treeview(self, columns=MainWindow.columns, show="headings")
            self.tree.pack(anchor=S, fill=BOTH, expand=1)
            for x in MainWindow.columns:
                self.tree.heading(x, text=x)

            self.tree.bind("<<TreeviewSelect>>", self.select)

            for x in self.tree.get_children():
                self.tree.delete(x)

            self.headValues.extend(MainWindow.columns)
            self.checkTemp = False

            for x in range(self.numOfRows + 1):
                self.cursor.execute(f"SELECT * FROM People WHERE id={x}")
                self.tuple = (x,)
                self.tupleFromDB = self.cursor.fetchone()
                if self.tupleFromDB == None and self.checkTemp == False:
                    self.checkTemp = True
                else:
                    for y in self.tupleFromDB:
                        self.tuple += (y,)
                    self.tableValues.append(self.tuple)
                    del self.tuple
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




