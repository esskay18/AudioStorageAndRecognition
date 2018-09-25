print("Running...")
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from AddAudio import ShowAudio
from AddAudio import AddAudio
from tabulate import tabulate
from CreateTable import ClearTable

root = tk.Tk()
root.title("Database Manager")

frame = tk.Frame(root, height = 300, width = 300)
frame.pack(expand = True)
frame.propagate(0)

def ShowCurrentDatabase():
    window = tk.Toplevel(root)
    window.geometry("400x300")
    window.title("Current Database")
    window.grid()
    
    database = tk.Text(window, height = 30, width = 50, wrap = "none")
    
    scrollx = Scrollbar(window, orient = HORIZONTAL)
    scrollx.pack(side = BOTTOM, fill = X)
    scrollx.config(command = database.xview)

    scrolly = tk.Scrollbar(window, orient = tk.VERTICAL)
    scrolly.pack(side = tk.RIGHT, fill = tk.Y)
    scrolly.config(command = database.yview)

    database.config(yscrollcommand = scrolly.set)
    database.config(xscrollcommand = scrollx.set)

    database.insert(END, tabulate(ShowAudio(), headers = ["No.", "Name", "Artist"]))
    database.pack()

def ScanDatabase():
    answer = AddAudio()
    window = tk.Toplevel(root)
    frameScan = tk.Frame(window, width = 50, height = 50)
    window.title("Scanning")
    frameScan.pack()
    
    msg = tk.Text(frameScan, height = 20, width = 50)
    msg.pack()
    
    if(len(answer)>0):
        msg.insert(END, "Inserted Songs:\n")
        for i in answer:
            msg.insert(END,i+"\n")
    else:
        msg.insert(END,"No new songs inserted")

def DeleteDatabase():
    ClearTable()
    try:
        tk.messagebox.showinfo("Clear Current Database", "Database Cleared.")
    except:
        import tkMessageBox
        tkMessageBox.showinfo("Clear Current Database", "Database Cleared.")
    
ShowDatabase = tk.Button(frame, text = "View Current Database", command = ShowCurrentDatabase)
ShowDatabase.place(in_ = frame, x = 80, y = 10)

UpdateDatabase = tk.Button(frame, text = "Scan For New Songs", command = ScanDatabase)
UpdateDatabase.place(in_ = ShowDatabase, x = 0, y = 50)

DeleteDB = tk.Button(frame, text = "Clear Current Database", command = DeleteDatabase)
DeleteDB.place(in_ = UpdateDatabase, x = -10,  y = 50)
root.mainloop()
