from tkinter import *
import tkinter.messagebox

def validate():
    name= entry_1.get()
    email= entry_2.get()
    cpassword= entry_5.get()
    country= c.get()
    password= entry_6.get()
    gender= var.get()
    if (name=="" or email=="" or country== 'Select your country'or password == "" or gender == 0 or cpassword == ""):
        tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")

    else:
        tkinter.messagebox.showinfo('Success Message',"Successfully registered!")
        

   
root = Tk()
root.geometry('500x500')
root.title("Registration Form")


label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_6 = Label(root, text="Password",width=20,font=("bold", 10))
label_6.place(x=80,y=230)

entry_6 = Entry(root,show='*')
entry_6.place(x=240,y=230)

label_5 = Label(root, text="Confirm Password",width=20,font=("bold", 10))
label_5.place(x=80,y=280)

entry_5 = Entry(root,show='*')
entry_5.place(x=240,y=280)


label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=330)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=330)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=330)


label_4 = Label(root, text="Country",width=20,font=("bold", 10))
label_4.place(x=70,y=380)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa','America','Australia'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select your country') 
droplist.place(x=240,y=380)


Button(root, text='Submit',width=20,bg='green',fg='white', command = validate).place(x=180,y=430)

root.mainloop()
