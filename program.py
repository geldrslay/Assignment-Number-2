from tkinter import*
from tkinter import messagebox
import ast

from PIL import Image, ImageTk

# Main Window 

window = Tk()
window.title("BSCPE 1-5 Information Sheet")
window.geometry('925x600+300+200')
window.configure(bg='#6495ED')
window.resizable(False,False)

# Pop-Up Window

def pop_up():
    pop_up_window = Toplevel (window)
    pop_up_window.title("Registration Complete")
    pop_up_window.geometry("500x200")
    pop_up_window.configure(bg='white')
    alert =Label(pop_up_window, text="Information has been submitted. Welcome to Cincode!",fg='black',border=0, bg='white',font=('Microsoft Yahei UI Light', 10,'bold')).place(x=70, y=40)
    button1= Button(pop_up_window, text="Okay!",width=15, pady=7,bg='gray', fg='black', border=0, command=pop_up_window.destroy).place(x=180, y=90)
    alert.pack()
    button1.pack()
    pop_up_window.mainloop ()

# Background

image = PhotoImage(file="cpe.png")
Label (window, image=image,border =0,bg="#6495ED").place(x=10, y=50)

# Text Frame

frame=Frame(window, width= 350, height=390, bg="#6495ED")
frame.place(x=500, y=90)

# Heading

heading1=Label(frame,text='INFORMATION SHEET',fg="#104E8B", bg='#6495ED',font =('Microsoft Yahei UI Light', 17, 'bold'))
heading1.place(x=90, y=0)
heading2=Label(frame,text='BSCPE 1-5',fg="#104E8B", bg='#6495ED',font =('Microsoft Yahei UI Light', 15, 'bold'))
heading2.place(x=160, y=35)

# Name Variable

def on_enter(e):
    name.delete(0,'end')
def on_leave(e):
    if name.get()=='':
        name.insert(0,'Name')

name = Entry(frame,width=100,fg='black',border=0, bg='#6495ED',font=('Microsoft Yahei UI Light', 10))
name.place(x=60, y=90)
name.insert(0,'Name')
name.bind("<FocusIn>", on_enter)
name.bind("<FocusOut>", on_leave)
Frame(frame, width=300, height=2, bg='black').place(x=60, y=120)

# Age Variable

def on_enter(e):
    age.delete(0,'end')
def on_leave(e):
    if age.get()=='':
        age.insert(0,'Age')
        
age = Entry(frame,width=100,fg='black',border=0, bg='#6495ED',font=('Microsoft Yahei UI Light', 10))
age.place(x=60, y=150)
age.insert(0,'Age')
age.bind("<FocusIn>", on_enter)
age.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=60, y=180)

# Address Variable

def on_enter(e):
    address.delete(0,'end')
def on_leave(e):
    if address.get()=='':
       address.insert(0,'Address')
        
address = Entry(frame,width=100,fg='black',border=0, bg='#6495ED',font=('Microsoft Yahei UI Light', 10))
address.place(x=60, y=210)
address.insert(0,'Address')
address.bind("<FocusIn>", on_enter)
address.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=60, y=240)

# Check Button

check_button = Checkbutton (frame, text="I certify that the information provided in this form is correct.", fg='black',border=0, bg='#6495ED',font=('Microsoft Yahei UI Light', 7))
check_button.place(x=75, y=270)

# Submit Button

submit = Button(frame, width=30, pady=7, text='Submit Information',bg='white', fg='black', border=0, command=pop_up).place(x=100,y=310)

window.mainloop()