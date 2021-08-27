from tkinter import*
root = Tk()
root.title('Check Box')
root.iconbitmap('C:/Users/Omen/Desktop/A/deep.ico')

def show():
    myLabel = Label(root, text=var.get()).pack()
var = StringVar()

#anything can be written in on or off string input

checkButton = Checkbutton(root, text="Check this box!",variable = var, onvalue="On", offvalue="Off")

#Automatic selection on check box will be removed
checkButton.deselect()
checkButton.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()




