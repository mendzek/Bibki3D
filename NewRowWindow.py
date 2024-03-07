from tkinter import *
from tkinter import ttk

import LogPassWindow


class NewRowWindow(Tk):

    def __init__(self):
        super().__init__()
        root = Tk()
        root.title("Bibki3D - New row")
        root.geometry("800x300")
        self.protocol("WM_DELETE_WINDOW", lambda: self.dismiss)
        close_button = ttk.Button(self, text="Закрыть окно", command=lambda: self.dismiss)
        close_button.pack(anchor="center", expand=1)
        self.grab_set()

        self.label = ttk.Label(self, text="Измените строку в окне ниже. Нажмите \"Сохранить\" когда закончите")
        self.label.pack(expand=1, side=TOP)

        for x in range(len(self.selectedPeopleList)):
            self.entry = ttk.Entry(self, name="entry_" + str(x), state=NORMAL)
            self.entry.insert(0, f"{self.selectedPeopleList[x]}")
            self.entry.pack(expand=1, side=LEFT)
            self.entrysList.append(self.entry)

        self.BT_save = ttk.Button(self, text="Сохранить", command=self.BT_save)
        self.BT_save.pack(expand=1, side=BOTTOM)

    def dismiss(self):
        self.grab_release()
        self.destroy()

