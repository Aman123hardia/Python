# import tkinter
# import tkinter.messagebox as tkMessageBox

# top = tkinter.Tk(className=" GUI DICE GAME OF TWO PLAYER")
# top.geometry("500x400")
# def helloCallBack():
#    tkMessageBox.showinfo( "Hello Python", "Hello World")

# B = tkinter.Button(top, text ="CLICK TO START GAME ", command = helloCallBack)

# B.pack()
# top.mainloop()


from tkinter import *

gui = Tk(className='Python Examples - Button')
gui.geometry("500x200")

# create button
button = Button(gui, text='My Button', width=40, height=3, bg='black', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
# add button to gui window
button.pack()

gui.mainloop() 