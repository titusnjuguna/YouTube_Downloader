#importing libraries
from tkinter import *
from pytube import YouTube
from urllib.request import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Youtube Downloader')

Label(root,text='Youtube Video Downloader',font ='arial 20 bold').pack()
link = StringVar()
Label(root,text = 'Paste Link Here:',font = 'arial 15 bold').place(x = 160 ,y = 60)
link_enter = Entry(root,width = 50,textvariable = link).place(x = 32 ,y = 90)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root,text = 'Video is Downloaded', font = 'arial 15').place(x= 180 , y = 210) 
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold',bg = 'pale violet red', 
    padx = 2, command = Downloader).place(x = 180  ,y= 150) 
root.mainloop()