from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning
from MainWindow import *

rightLog = "Login"
rightPass = "Password"

def AcceptLogPass():
    if rightLog == EntryLog.get() and rightPass == EntryPass.get():
        print("nice")

        mainWindow = MainWindow()

    else:
        print("not nice")

        showwarning(title="Неверный логин или пароль", message="Неверный логин или пароль, попробуйте снова")


LogPassWindow = Tk()
LogPassWindow.title("Bibki 3D - Log in")
LogPassWindow.geometry("400x300")

EntryLog = ttk.Entry(LogPassWindow,width=15, font=("Arial", 20))
EntryLog.insert(0, "Login")
EntryLog.pack(anchor=CENTER, pady=20)

EntryPass = ttk.Entry(LogPassWindow,width=15, font=("Arial", 20))
EntryPass.config(show="*")
EntryPass.insert(0, "Password")
EntryPass.pack(anchor=CENTER)

BTLogPassAccept = ttk.Button(LogPassWindow,text="Log in", width=20, command=AcceptLogPass)
BTLogPassAccept.pack(anchor=CENTER)