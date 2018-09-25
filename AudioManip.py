from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np
import sqlite3
import io


def AudioEncoding(file = fileSrc):
    f,s = wavfile.read(file)

    return s

def AudioDecoding(data, file = fileSrc):
    song = TextAudio(data)
    name = input("Enter File Name:")
    write(file+"\\"+name+".wav", 22050, song)

def AudioText(data):
    output = io.BytesIO()
    np.savez(output, data = data)
    output.seek(0)
    content = sqlite3.Binary(output.read())

    return content

def TextAudio(t):
    data = np.load(io.BytesIO(t))
    x = data['data']

    return x
