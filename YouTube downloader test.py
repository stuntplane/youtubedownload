from pytube import YouTube
from tkinter import *
from tkinter import ttk

def YTDV():
    yt = YouTube(e.get())
    tytul = print(yt.title)
    stream = yt.streams.get_highest_resolution()
    stream.download()

def YTDA():
    yt = YouTube(e.get())
    tytul = print(yt.title)
    stream = yt.streams.get_audio_only()
    stream.download()

root = Tk()
myLabel1 = Label(root, text="Paste your YouTube Link here: ", width=60, justify=CENTER)
myLabel1.pack()

e = ttk.Entry(root, width=60)
e.pack()

myLabel2 = Label(root, text="Made by Marcin G. ", justify=RIGHT)
myLabel2.pack()

dlVButton = ttk.Button(root, text="Download Video", command=YTDV)
dlVButton.pack()

dlAButton = ttk.Button(root, text="Download Audio", command=YTDA)
dlAButton.pack()

root.mainloop()
