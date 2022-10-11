import random
import os
import pygame
from tkinter import *

root = Tk()
root.minsize(300,300)
root.title("Music Player")

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def directorychooser():
    directory = 'C:\\Users\\BrokeSkill\\Desktop\\Musik'
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            realnames.append(files)

            listofsongs.append(realdir)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname

def playsong(event):
    pygame.mixer.music.play()

def pausesong(event):
    pygame.mixer.music.pause()

def unpausesong(event):
    pygame.mixer.music.unpause()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()



label = Label(root,text="Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
for items in realnames:
    listbox.insert(0,items)

realnames.reverse()

playbutton = Button(root, text='Play Music')
playbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

pausesbutton = Button(root,text='Pause Music')
pausesbutton.pack()

unpausesbutton = Button(root,text='Unpause Music')
unpausesbutton.pack()

nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text='Previous Song')
previousbutton.pack()



songlabel.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
pausesbutton.bind("<Button-1>",pausesong)
unpausesbutton.bind("<Button-1>",unpausesong)

root.mainloop()