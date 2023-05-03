from tkinter import *
from PIL import *
tk=Tk()
tk.geometry("400x300")
frame=Frame(tk,width=300,height=300)
frame.pack()


frame.place(anchor='center', relx=0.5, rely=0.5)


img = Image.PhotoImage(Image.open("forest.jpg"))

label = Label(frame, image = img)
label.pack()

win.mainloop()