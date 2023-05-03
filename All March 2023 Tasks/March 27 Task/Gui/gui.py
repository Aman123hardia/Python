# from tkinter import *
# root = Tk()
# a = Label(root, text ="Hello World")
# a.pack()

# root.mainloop()


# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()


# from tkinter import *
# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()

import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 4,40,588,300
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()