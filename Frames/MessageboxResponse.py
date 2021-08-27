from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')


# root.iconbitmap()

def popup():



Button(root, text="Popup", command=popup).pack()

root.mainloop()
