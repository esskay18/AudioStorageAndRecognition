from tkinter import Tk
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import FindSong as FS
from FindSong import SelectAudio
from FindSong import FindMatch
from os.path import basename
from AddAudio import ArtistSongs
from tabulate import tabulate
global filename
filename = None

root = tk.Tk()
root.title("Song Detection")

fileNameLabel = tk.StringVar()
frame = tk.Frame(root, height = 100, width = 100)
frame.grid()

title = tk.Label(root, text = "Follow in order to find song")
title.grid(row = 0, column = 0, columnspan = 4)

def Insert():
    global filename
    
    filename = askopenfilename() 
    fileNameLabel.set(basename(filename))
    songTitle.update()
    

def Check():
    audioText = SelectAudio(filename)
    answer = FindMatch(audioText)

    if(len(answer[1]) == 2):
        window = tk.Toplevel()
        frame1 = tk.Frame(window)
        frame1.grid()

        def ArtistDetails():
            window1 = tk.Toplevel(root)
            window1.geometry("400x300")
            window1.title("Current Database")
            window1.grid()
            database = tk.Text(window1, height = 30, width = 50, wrap = "none")
    
            scrollx = tk.Scrollbar(window1, orient = tk.HORIZONTAL)
            scrollx.pack(side = tk.BOTTOM, fill = tk.X)
            scrollx.config(command = database.xview)
            
            scrolly = tk.Scrollbar(window1, orient = tk.VERTICAL)
            scrolly.pack(side = tk.RIGHT, fill = tk.Y)
            scrolly.config(command = database.yview)

            database.config(yscrollcommand = scrolly.set)
            database.config(xscrollcommand = scrollx.set)

            database.insert(tk.END, tabulate(ArtistSongs(answer[1][0]), headers = ["Name"]))
            database.pack()

        foundLabel = tk.Label(frame1, text = "Song Found:")
        foundLabel.grid(row = 0, column = 0)

        songLabel = tk.Label(frame1, text = answer[0])
        songLabel.grid(row = 0, column = 1)

        artistLabel = tk.Label(frame1, text = "Artist:")
        artistLabel.grid(row = 1, column = 0)

        artistName = tk.Label(frame1, text = answer[1][0])
        artistName.grid(row = 1, column = 1)

        identifiedLabel = tk.Label(frame1, text = "This song was identified "+str(answer[1][1])+" times.")
        identifiedLabel.grid(row = 2, column = 0, columnspan = 2)

        artistButton = tk.Button(frame1, text = "Other Songs by this artist", command = ArtistDetails)
        artistButton.grid(row = 3, column = 0, columnspan = 2)

    else:
        msg = tk.messagebox.showinfo("Checking Song", answer[0])


step1 = tk.Label(root, text = "1.")
step1.grid(row = 1, column = 0)

step2 = tk.Label(root, text = "2.")
step2.grid(row = 3, column = 0)

insertSong = tk.Button(root, text = "Insert Song", command = Insert)
insertSong.grid(row = 1, column = 2)

inserted = tk.Label(root, text = "Inserted Song")
inserted.grid(row = 2, column = 1)

songTitle = tk.Label(root, textvariable = fileNameLabel)
songTitle.grid(row = 2, column = 2)

checkSong = tk.Button(root, text = "Check Song", command = Check)
checkSong.grid(padx = 10, pady = 30, row = 3, column = 2)

root.mainloop()
