from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x180')  
tkWindow.title('Login Form')

label_0 = Label(tkWindow, text="Login form",width=20,font=("bold", 20))
label_0.place(x=30,y=10)

#username label and text entry box
usernameLabel = Label(tkWindow, text="Email").place(x=100,y=60)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=180,y=60)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").place(x=100,y=90)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=180,y=90) 

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login",width=20,bg='green',fg='white',command=validateLogin).place(x=135,y=123)  

tkWindow.mainloop()