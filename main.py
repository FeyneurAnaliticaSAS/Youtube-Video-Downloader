import requests
import os 
from tkinter import *
from PIL import ImageTk, Image
from pytube import YouTube


def get_video_name()-> None:
    """ Este metodo toma como parametro interno el link 
        de un video de Youtube y obtiene su nombre.

        - Edita un Label de Tkinter y coloca el nombre del video.
    """

    yt = YouTube(video_link.get())
    video_name.configure(text=yt.streams.first().default_filename)
    video_name.text = yt.streams.first().default_filename
    
    
def download_video()-> None :
    """ Descarga un video de youtube a partir del link
        y lo guarda en la carpeta videos.
    """
    yt = YouTube(video_link.get())
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download('videos/')


def link_handler(youtube_link:str):
    """ Toma el link de un video de youtube y guarda 4 links diferentes
        en un Array, dichos links son las miniaturas del video.

    Args:
        youtube_link (str): Link de un video de Youtube.

    Returns:
        Array: Array con los links de cada imagen de la miniatura del video
    """
    

    # Toma 3 diferentes miniaturas de un mismo video de youtube.
    template_1 = 'https://img.youtube.com/vi/{}/0.jpg'
    template_2 = 'https://img.youtube.com/vi/{}/1.jpg'
    template_3 = 'https://img.youtube.com/vi/{}/2.jpg'
    template_4 = 'https://img.youtube.com/vi/{}/3.jpg'

    # Split toma el string de un link como: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    # y lo separa en la parte antes del '=' y despues del '='
    a,b = youtube_link.split('=')

    # Toma los templates y forma los links
    formated_link_1 = template_1.format(b)
    formated_link_2 = template_2.format(b)
    formated_link_3 = template_3.format(b)
    formated_link_4 = template_4.format(b)

    # Crea un array con diferentes links.
    links = [formated_link_1, formated_link_2, formated_link_3, formated_link_4]

    return links


def get_thumbnail():
    """ Utiliza el metodo link_handler y descarga las miniaturas de un video. 

        Posteriormente coloca esas imagenes en un Frame de Tkinter
    """

    # Toma los links
    img_link = link_handler(video_link.get())[0]
    img_link_1 = link_handler(video_link.get())[1]
    img_link_2 = link_handler(video_link.get())[2]
    img_link_3 = link_handler(video_link.get())[3]
    
    

    # Descargar la imagen con la libreria requests.
    # 1.
    data = requests.get(img_link).content
    with open('img_temp/sample_image.png','wb') as file:
        file.write(data)
    # 2.
    data_1 = requests.get(img_link_1).content
    with open('img_temp/sample_image_1.png','wb') as file:
        file.write(data_1)

    # 3. 
    data_2 = requests.get(img_link_2).content
    with open('img_temp/sample_image_2.png','wb') as file:
        file.write(data_2)

    # 4. 
    data_3 = requests.get(img_link_3).content
    with open('img_temp/sample_image_3.png','wb') as file:
        file.write(data_3)


    # Carga la imagen en el contexto de Tkinter y la coloca en un label.

    # Comprueba si las imagenes ya existen
    if os.path.exists('img_temp/sample_image.png') and os.path.exists('img_temp/sample_image_1.png') :
        
        # Todos los Frame ya existen, aqui lo que hace es editarlos.

        # Coloca la 1er miniatura en el Frame
        loaded_img = Image.open("img_temp/sample_image.png")
        resize_img = loaded_img.resize((250,180))
        imge = ImageTk.PhotoImage(resize_img)
        img_logo_temp.configure(image=imge)
        img_logo_temp.image = imge

        # Coloca la 2da miniatura en el Frame
        loaded_img_1 = Image.open("img_temp/sample_image_1.png")
        resize_img_1 = loaded_img_1.resize((100,60))
        imge_1 = ImageTk.PhotoImage(resize_img_1)
        img_logo_temp_1.configure(image = imge_1)
        img_logo_temp_1.image = imge_1
   
        # Coloca la 3er miniatura en el Frame
        loaded_img_2 = Image.open("img_temp/sample_image_2.png")
        resize_img_2 = loaded_img_2.resize((100,60))
        imge_2 = ImageTk.PhotoImage(resize_img_2)
        img_logo_temp_2.configure(image = imge_2)
        img_logo_temp_2.image = imge_2

        # Coloca la 4ta miniatura en el Frame
        loaded_img_3 = Image.open("img_temp/sample_image_3.png")
        resize_img_3 = loaded_img_3.resize((100,60))
        imge_3 = ImageTk.PhotoImage(resize_img_3)
        img_logo_temp_3.configure(image = imge_3)
        img_logo_temp_3.image = imge_3
  
  


# --- MAIN CODE ---

root = Tk() # Objeto Tkinter
root.config(bd=15) # Margen
root.geometry('500x500') # Tamanio de la ventanda
root.title("Herramienta para descargar videos") # Titulo

text_prompt = "Ingrese el link del video que desea descargar: "
prompt = Label(root, text = text_prompt, font = ('Courier', '15'),fg = 'black',)
prompt.place(x=19,y=30)

# Logo de Feyneur
loaded_img = Image.open("img/feyneur_logo.jpeg")
resize_img = loaded_img.resize((150,80))
img = ImageTk.PhotoImage(resize_img)
img_logo = Label(root, image = img)
img_logo.place(x = 310, y = 380)


# Input 
video_link = Entry(root, width = 40, font = ('Courier', '15'))
video_link.grid(row=1, column=1)
video_link.place(x=45,y=65)


# Boton de buscar
btn_buscar = Button(root, text = 'Buscar', command=lambda:[get_video_name(), get_thumbnail()])
btn_buscar.place(x=110,y=100)

btn_descargar = Button(root, text = 'Descargar', command=download_video)
btn_descargar.place(x=245,y=100)

# Miniaturas del video a descargar

img_logo_temp = Label(root, image = '')
img_logo_temp.place(x = 30, y = 148)

img_logo_temp_1 = Label(root, image = '')
img_logo_temp_1.place(x = 283, y = 148)

img_logo_temp_2 = Label(root, image = '')
img_logo_temp_2.place(x = 283, y = 207)       

img_logo_temp_3 = Label(root, image = '')
img_logo_temp_3.place(x = 283, y = 269)  

# Nombre del video

video_name = Label(root, text = '', font = ('Courier', '12'),fg = 'black',)
video_name.place(x=35,y=350)


root.mainloop()