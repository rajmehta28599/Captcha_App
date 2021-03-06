import random
from tkinter import Tk,StringVar,Label,Entry,Button,messagebox

text="abcdefghijklmnopqrstuvwxyz01243456789!@#$%^&*()_+"
window=Tk()
window.title("Captcha Application")
window.geometry("500x200")
captcha=StringVar()
user_input=StringVar()

def set_captcha():
    s=random.choices(text,k=6)
    captcha.set(''.join(s))

def check():
    if captcha.get()==user_input.get():
        messagebox.showinfo("Success","Correct")
    else:
        messagebox.showerror("Error","Incorrect")
    set_captcha()

Label(window,textvariable=captcha,font="Arial 20 bold").pack()
Entry(window,textvariable=user_input,font="Arial 15 bold").pack(ipady=5)
Button(window,command=check,text="Check",font="Arial 15 bold").pack()
 
set_captcha()
window.mainloop()

