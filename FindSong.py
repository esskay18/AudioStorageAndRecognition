import AudioManip as AM
from AudioManip import AudioText
from AudioManip import AudioEncoding
from AudioManip import TextAudio
import CreateConnection
from CreateConnection import ConnectDB
import numpy as np
import os as os
from CreateTable import UpdateTable


identified = None
path = os.path.abspath(__file__)
directory = os.path.split(path)[0]
dbname = "pythonsqlite.db"
database = os.path.join(directory, dbname)

def SelectAudio(file):
    audioNumpy = AudioEncoding(file = file)
    audioText = AudioText(audioNumpy)

    return audioText

def FindMatch(audioText):
    conn = ConnectDB(database)
    l = conn.execute("SELECT id, name, artist, audio, identified FROM music")

    fileDB = []
    for i in l:
        fileDB.append(i)

    found = 0
    for i in range(len(fileDB)):
        TextDB = fileDB[i][3]
        numpyTextDB = TextAudio(TextDB)
        givenNumpy = TextAudio(audioText)
        audioLen = len(numpyTextDB)
        givenLen = len(givenNumpy)
        pointer = 0
        reversePointer = audioLen-givenLen-1
        while(pointer<reversePointer):
            if(np.array_equal(numpyTextDB[pointer:pointer+givenLen],givenNumpy) or np.array_equal(numpyTextDB[reversePointer:reversePointer+givenLen],givenNumpy)):
                identified = i
                found = 1
                break;
            pointer += 1
            reversePointer -= 1
        if found == 1:
            break;
        
    flag = None
    if found == 0:
        find = "No match found in current database."
        flag = "Not Found"
    else:
        UpdateTable(fileDB[identified][0], fileDB[identified][4]+1)
        find = fileDB[identified][1]
        flag = [fileDB[identified][2], fileDB[identified][4]+1]

    answer = [find, flag]
    
    return answer
if __name__ == '__main__':
    FindMatch(SelectAudio(filename))
