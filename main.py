import os
cwd=os.getcwd()
import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("1420x800")
root.title("Type writing")
root.iconbitmap("typewrite.ico")

minutes=["1 Minute","2 Minutes","3 Minutes","5 Minutes"]
minute=StringVar()
minute.set(minutes[0])
drop=OptionMenu(root,minute,*minutes)
drop.config(width=14,fg="green",font="Aerial 12 bold")
drop.place(x=1210,y=400)

i=0

def sets():
    global i
    start_btn.config(state="normal")
    if minute.get()=="1 Minute":
        i=60
        label.config(text=minute.get())
    if minute.get()=="2 Minutes":
        i=120
        label.config(text=minute.get())
    if minute.get()=="3 Minutes":
        i=180
        label.config(text=minute.get())
    if minute.get()=="5 Minutes":
        i=300
        label.config(text=minute.get())
        
def reset():
    global text
    global i
    text.delete(1.0,END)
    if minute.get()=="1 Minute":
        i=61
    if minute.get()=="2 Minutes":
        i=121
    if minute.get()=="3 Minutes":
        i=181
    if minute.get()=="5 Minutes":
        i=301
    

def starts(c):
    global i
    global label
    sets.config(state="disabled")
    start_btn.config(state="disabled")
    drop.config(state ="disabled")
    text.config(state="normal")
    text.focus()

    if c==1:
        restart_btn.config(state="normal")
        i-=1
        label.configure(text=i)
        if i==0:
            c=0
            start_btn.config(state="disabled")
            restart_btn.config(state="disabled")
            drop.config(state ="normal")
            sets.config(state="normal")
            txt=text.get(1.0,END)
            txt=txt.split()
            count=0
            letters=[]
            for letter in txt:
                letters+=("".join(letter))    
            
            for word in txt:
                count+=1
            msg=messagebox.showinfo('performance',f' \n\nIn {minute.get()}\n\nWORDS : {count}\n\n LETTERS : {len(letters)}' )
            text.delete(1.0,END)
            text.config(state="disabled")
                
    if c==1:   
        label.after(1000,lambda:starts(c))
        
    
    
number=0  

def forward():
    global number
    global img_label
    
    number+=1
    
    img_label.pack_forget()
    img_label=Label(frame3,image=img_list[number],width=900,height=320)
    img_label.pack()
    frame3.pack()
    

    backward=Button(root,text="<<",width=5,fg="red",bd=3,bg="skyblue",command=backword)
    backward.place(x=150,y=140)

    if number==3:
        forword=Button(root,text=">>",width=5,fg="red",state="disabled",bd=3)
        forword.place(x=1300,y=140)

def backword():
    global number
    global img_label
    
    number-=1
    
    img_label.pack_forget()
    img_label=Label(frame3,image=img_list[number],width=900,height=320)
    img_label.pack()

    
    forword=Button(root,text=">>",width=5,fg="red",bd=3,command=forward,bg="skyblue")
    forword.place(x=1300,y=140)
    
    if number==0:
        backward=Button(root,text="<<",width=5,fg="red",state="disabled",bd=3)
        backward.place(x=150,y=140)
    

frame1=Frame(root)
frame2=Frame(root).pack(side='bottom')
frame3=Frame(root)
frame3.pack(side='top')
frame4=Frame(root)


image1=PhotoImage(file="one.png")
image2=PhotoImage(file="Slide15.png")
image3=PhotoImage(file="Tricky-Words.png")
image4=PhotoImage(file="words.png")

img_list=[image1,image2,image3,image4]

img_label=Label(frame3,image=image1,width=800,height=320)
img_label.pack()


forword=Button(root,text=">>",width=5,fg="red",bd=3,bg="skyblue",command=forward)
forword.place(x=1300,y=140)

backward=Button(root,text="<<",width=5,fg="red",bd=3,state="disabled")
backward.place(x=150,y=140)


label=Label(frame1,text=i,font="Times 50 bold",fg="brown")
label.pack()
frame1.pack()


scrollbar=Scrollbar(frame4,orient="vertical")
scrollbar.pack(side="right",fill=Y)

text=Text(frame4,width=70,height=9,font="Helvitica 16",yscrollcommand=scrollbar.set,state="disabled",fg='red')
text.pack()

scrollbar.config(command=text.yview)
frame4.pack()


start_btn= Button(frame2,text='Start',width=8,bd=2,fg='blue',font="Times 15",command=lambda:starts(1),state="disabled")
start_btn.place(x=500,y=640)

restart_btn= Button(root,text='Restart',width=8,bd=2,fg='blue',font="Times 15",command=reset,state="disabled")
restart_btn.place(x=650,y=640)

sets= Button(root,text='Set Minutes',width=9,bd=2,fg='blue',font="Times 15",command=sets)
sets.place(x=800,y=640)


root.mainloop()
