from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

        
root=Tk()
root.geometry("1350x800+0+0")
root.configure(bg="#fff")
root.title("Login sytem")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
    if username=='Rosan'and password=='1234':
      screen=Toplevel(root)
      screen.title("App")
      screen.geometry('925x500+300+200')
      screen.config(bg='white')
      Label(screen,text=f"Hello {username}",bg="white",font=("lucida",50,'bold')).pack(expand=True)
    elif username=='' or password=='':
      messagebox.showerror("Invalid","You must enter username  and password")
    elif username!="Rosan" and password!=1234:
        messagebox.showerror("Invalid","Invalid username or passsword")
img=PhotoImage(file='login.png')
Label(root,image=img,bg="white").place(x=50,y=50)
frame=Frame(root, width=350,height=350,bg="light blue")
frame.place(x=480,y=70)
heading=Label(frame,text='sign in',fg='#57a1f8',bg="white",font=("Microsoft YaHai UI Light",23,"bold"))
heading.place(x=100,y=5)
####_____________________________________________
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,'username')


user=Entry(frame,width=25,fg="black",border=2,bg="white",font=('Microsoft YaHai UI light',11))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=250,height=2,bg='black').place(x=25,y=107)
###--------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    password=code.get()
    if password=="":
        code.insert(0,'password')


code=Entry(frame,width=25,fg='black',border=2,bg="white",font=("Microsoft YaHai UI light",11))
code.place(x=30,y=120)
code.insert(0,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=250,height=2,bg="black").place(x=25,y=150)
#_____________________________________________________________
Button(frame,width=40,pady=7,text='Sign in',bg='dark blue',fg='white',border=0,command=signin).place(x=36,y=200)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('times new roman',9))
label.place(x=75,y=270)
sign_up=Button(frame,text="Sign Up",fg='green',bg='light blue',font=('lucida',9),border=0,curso='hand2')
sign_up.place(x=215,y=270)
root.mainloop()