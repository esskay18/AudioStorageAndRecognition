from CreateConnection import ConnectDB
import os
import AudioManip as AM
from tabulate import tabulate
import tkinter as tk

path = os.path.abspath(__file__)
directory = os.path.split(path)[0]
dbname = "pythonsqlite.db"
songFolder = "Songs"

database = os.path.join(directory, dbname)
#database = "C:\\Users\\saura\\Desktop\\Notes\\Sem 3\\DBMS\\Project\\pythonsqlite.db"
fileSrc = os.path.join(directory, songFolder)
#fileSrc = "C:\\Users\\saura\\Desktop\\Notes\\Sem 3\\DBMS\\Project\\Songs"

global artistName
artistName = None

def ReadArtist(songName):
    def buttonOK():
        global artistName
        artistName = entry.get()

        root.destroy()
        root.quit()

    root = tk.Tk()
    root.title("Enter Artist")

    frame = tk.Frame(root)
    frame.grid()

    tk.Label(root, text = "Song:").grid(row = 0)
    tk.Label(root, text = "Artist:").grid(row = 1)
    tk.Label(root, text = songName).grid(row = 0, column = 1)

    entry = tk.Entry(root)
    entry.grid(row = 1, column = 1)

    button = tk.Button(root, text = "OK", command = buttonOK)
    button.grid(row = 2, column = 1)

    root.mainloop()

    
def AddAudio():
    conn = ConnectDB(database)
    l = conn.execute("SELECT name from music")

    fileDB = []
    for i in l:
        fileDB.append(i)

    fileData = []
    for i in range(len(fileDB)):
        fileData.append(fileDB[i][0])

    filesToAdd = []
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) from music")
    dataCount = cursor.fetchall()
    dataCount = dataCount[0][0]

    fileFolder = [f for f in os.listdir(fileSrc) if f.endswith('.wav')]
    fileNames = []
    for i in fileFolder:
        if(dataCount!=0):
            if i not in fileData:
                fileNames.append(i)
        else:
            fileNames.append(i)

    idCount = 1
    for i in fileNames:
        temp = fileSrc+"\\"+i
        song = AM.AudioEncoding(temp)
        songText = AM.AudioText(song)
        ReadArtist(i)
        param = (dataCount+idCount, i, artistName, songText)
        cursor.execute("INSERT INTO music(id, name, artist, audio) VALUES(?, ?, ?, ?)", param)
        idCount += 1

        conn.commit()

    cursor.close()

    return fileNames

def ShowAudio():
    conn = ConnectDB(database)
    l = conn.execute("select id, name, artist from music")

    file = []
    for i in l:
        file.append(i)

    return file

def ArtistSongs(artistName):
    conn = ConnectDB(database)
    param = (artistName,)
    l = conn.execute("select name from music where artist = ?", param)
    file = []
    for i in l:
        file.append(i)

    return file

if __name__ == '__main__':        
    AddAudio()
    ShowAudio()
