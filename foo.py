from tkinter import *
import urllib.request, io
from PIL import ImageTk, Image
from pytube import YouTube
import requests 


response = requests.get('https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg')
print(response.status_code == 200)
file = open("img_temp/sample_image.png", "wb")
file.write(response.content)
file.close()

template = 'https://img.youtube.com/vi/{}/0.jpg'
link1 = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

a,b = link1.split('=')

new = template.format(b)

print(new)