from tkinter import *


import pyttsx3

x=pyttsx3.init()
x.setProperty("rate",125)
x.say("your distance calculator will open sooner please wait ")

x.runAndWait()
root=Tk()
root.config(bg='black')
root.attributes("-fullscreen",True)
def graph():
    import os
    os.system("pymatrix-rain")
lbl=Button(root,text="DISTANCE CALCULATOR",command=graph)
lbl.config(font=("callibri",24,"bold"),fg="white",bg="black")
lbl.pack(side=TOP,padx=20,pady=20)
btn=Button(root,text="KILL",command=root.destroy)
btn.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btn.pack(side=RIGHT,padx=10)
def display():
    import webbrowser
    webbrowser.open("https://www.github.com")

btns=Button(root,text="GIT HUB",command=display)
btns.config(font=("callibri",20,"bold italic"),bg="red",fg="black")
btns.pack(side=LEFT,padx=10)
img=PhotoImage(file="home.png")
lbl1=Label(root,image=img)
lbl1.config(width=1000, height=400)
lbl1.pack()

lbl2=Label(root,text="ENTER PASSWORD:")
lbl2.config(font=("callibri",24,"bold"),fg="green",bg="black")
lbl2.pack(padx=20,pady=20)

entry=Entry(root)
entry.config(font=("callibri",20,"bold"))
entry.pack(padx=10,pady=20)
def sample1():
    x=entry.get()
    y=str(x)
    if(y=="durk"):
        import os
        os.system("python distance.py")
    
    

btn=Button(root,text="LOGIN",command=sample1)
btn.config(font=("callibri",20,"bold"),bg="green",fg="black")
btn.pack(padx=100,pady=20)
root.mainloop()
