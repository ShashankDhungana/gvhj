from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Insertion')


my_image = ImageTk.PhotoImage(Image.open("C:/Users/Omen/Desktop/download.jpeg"))
my_label = Label( image = my_image)
my_label.pack()
root.mainloop()


