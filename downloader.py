# python3 -m pip install --upgrade pytube
# Correction in the cipher class on pytube library. 
# https://stackoverflow.com/questions/68945080/pytube-exceptions-regexmatcherror-get-throttling-function-name-could-not-find


from tkinter import *
from tkinter import messagebox as MessageBox
from pytube import YouTube
# video.get()

def download_video(link)-> None :
    yt = YouTube(link) 
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download()



root = Tk() # Objeto Tkinter
root.geometry('500x200')
root.config(bd=15) # Margen
root.title("Youtube video downloader")

intro = Label(root, text = "Probando")
video = Entry(root)
video.grid(row=0, column=1)
#command=downloader.download_video(video.get(), "videos/"
#boton = Button(root, text="Descargar",width=20, height=2, bg='white', command=download_video)
#boton.place(x=150, y=450)
#root.mainloop()
download_video('https://www.youtube.com/watch?v=ZZFU-miI3Es')

