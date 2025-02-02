import ast
import re
from tkinter import*
from tkinter import messagebox


window=Tk()
window.title('Login')
window.geometry('925x500+300+200')
window.configure(bg="light green")
window.resizable (False, False)

def signin():
    username=user.get()
    password=code.get()
    confirm_password=confirm_code.get()
    if password==confirm_password:
     try:
         file=open('datasheet.txt','r+')
         d=file.read()
         r=ast.literal_eval(d)

         dict2={username:password}
         r.update(dict2)
         file.truncate(0)
         file.close()
         
         file=open('datasheet.txt','w')
         w=file.write(str(r))
        
         messagebox.showinfo('Signup', 'Sucessfully sign up') 
     
     except:
     
          file=open('datasheet.txt','w')
          pp=str({'Username':'password'})
          file.write(pp)
          file.close()
    else:
        messagebox.showerror('Invalid', "Both passwords should match")


frame=Frame(window,width=350,height=390,bg="white") 
frame.place(x=480,y=70)

heading=Label(frame,text='Create Account',fg='black', bg='white', font=('Microsoft YaHei UI Light(bold)', 23, 'bold'))
heading.place(x=60,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11)) 
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11)) 
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def on_enter(e):
    confirm_code .delete(0,'end')

def on_leave(e):
    if confirm_code.get()=='':
        confirm_code .insert(0,'Confirm Password')

confirm_code = Entry(frame,width=25,fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11)) 
confirm_code .place(x=30,y=220)
confirm_code .insert(0,'Confirm Password')
confirm_code .bind('<FocusIn>', on_enter)
confirm_code .bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

Button(frame,width=39,pady=7,text='Sign Up',bg='black',fg='white',border=0,command=signin).place(x=35,y=280)
label=Label(frame,text="I already have an account",fg='black',bg='white',font=('Arial',9))
label.place(x=55,y=340)

signin=Button(frame,width=6,text='Sign In',border=0,bg='white',cursor='hand2',fg='blue')
signin.place(x=200,y=340)

window.mainloop()
