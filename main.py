# First try of the window.
from tkinter import *
from tkinter import messagebox as MessageBox
import downloader 

root = Tk() # Objeto Tkinter
root.config(bd=15) # Margen
root.title("Youtube video downloader")

intro = Label(root, text = "Probando")
video = Entry(root)
video.grid(row=0, column=1)
#command=downloader.download_video(video.get(), "videos/"
boton = Button(root, text="Descargar", command=downloader.download_video("https://www.youtube.com/watch?v=ZZFU-miI3Es", "videos/"))
root.mainloop()