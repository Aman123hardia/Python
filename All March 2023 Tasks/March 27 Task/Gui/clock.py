from tkinter import *
import time
tkOb=Tk(className='Digital Clock')
tkOb.geometry("200x150")


label = Label(tkOb, font='bold', bg='white', fg='Black', bd=60)
label.grid(row=0, column=1)

def clock(): 
   time1 = time.strftime("%H:%M:%S")
   label.config(text=time1,font=63) 
   label.after(200, clock)

clock()
tkOb.mainloop() 