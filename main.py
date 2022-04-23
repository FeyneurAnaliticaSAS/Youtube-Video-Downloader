from gc import callbacks
from tkinter import *
from PIL import ImageTk, Image
import requests
import os 
#import downloader 


TEMP_IMG  = ''
def on_change(e):
    print (e.widget.get())

#link1 = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

def link_handler(youtube_link):
    template = 'https://img.youtube.com/vi/{}/0.jpg'
    a,b = youtube_link.split('=')
    new = template.format(b)

    return new

def join(e):
    print(e)

def set_thumbnail():

    loaded_img_temp = Image.open("img_temp/sample_image.png")
    resize_img_temp = loaded_img_temp.resize((150,80))
    img_temp = ImageTk.PhotoImage(resize_img_temp)
    return img_temp


def get_thumbnail():
    img_link = link_handler(video_link.get())
    data = requests.get(img_link).content
    with open('img_temp/sample_image.png','wb') as file:
        file.write(data)
    print(os.path.exists('img_temp/sample_image.png'))    
    #response = requests.get(img_link)
    #print(data.status_code == 200)
  
  
    
def foo():
    print(os.path.exists('img_temp/sample_image.png'))    
    loaded_img = Image.open("img_temp/sample_image.png")
    resize_img = loaded_img.resize((150,80))
    imge = ImageTk.PhotoImage(resize_img)
    img_logo_temp.configure(image=imge)
    img_logo_temp.image = imge
    


    
link_handler('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

root = Tk() # Objeto Tkinter
root.config(bd=15) # Margen
root.geometry('500x500')
root.title("Youtube video downloader")

text_prompt = "Ingrese el link del video que desea descargar: "
prompt = Label(root, text = text_prompt, font = ('Courier', '15'),fg = 'black',)
prompt.place(x=19,y=30)

loaded_img = Image.open("img/feyneur_logo.jpeg")
resize_img = loaded_img.resize((150,80))
img = ImageTk.PhotoImage(resize_img)

img_logo = Label(root, image = img)
img_logo.place(x = 310, y = 380)

video_link = Entry(root, width = 40, font = ('Courier', '15'))
video_link.grid(row=1, column=1)
video_link.place(x=45,y=65)

btn_buscar = Button(root, text = 'Buscar', command=get_thumbnail)
btn_buscar.place(x=100,y=100)

btn_buscar1 = Button(root, text = 'ppp', command=foo)
btn_buscar1.place(x=200,y=100)



img_logo_temp = Label(root, image = img)
img_logo_temp.place(x = 200, y = 200)
       



#get_thumbnail(link_handler(video_link.get()))
#btn_buscar.place(x=60,y=60)

#command=downloader.download_video(video.get(), "videos/"
#boton = Button(root, text="Descargar", command=downloader.download_video("https://www.youtube.com/watch?v=ZZFU-miI3Es", "videos/"))
root.mainloop()