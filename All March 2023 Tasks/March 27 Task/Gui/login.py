from tkinter import *
from functools import partial

def Login(username, password):
	print("Enter Username entered :", username.get())
	print("Enter password entered :", password.get())
	return

tk = Tk()  
tk.geometry('400x150')  
tk.title('Using Tkinter Login Form ')

usernameLabel = Label(tk, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tk, textvariable=username).grid(row=0, column=1)  

passwordLabel = Label(tk,text="Password").grid(row=1, column=0)  
password = StringVar()
pass_Field = Entry(tk, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(Login, username, password)

loginButton = Button(tk, text="Login", command=validateLogin).grid(row=4, column=0)  

tk.mainloop()