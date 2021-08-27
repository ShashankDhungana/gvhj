from tkinter import*
root = Tk()
frame = LabelFrame(root, text="My Frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

button1 = Button(frame, text="Don't Click")
button1.grid(row=0, column=0)
button2 = Button(frame, text="Please Click")
button2.grid(row=1, column=1)
root.mainloop()
