# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 21:52:54 2021

@author: akram1987
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 07:59:52 2021

@author: akram1987
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 09:22:00 2020

@author: akram1987
"""

from tkinter import *
from tkinter import PhotoImage
import string
from random import randint, choice 

def generer():
    passmin=3
    passmax=8
    allchar=string.ascii_letters+string.punctuation+string.digits
    password="".join(choice(allchar) for x in range(randint(passmin,passmax)))
    pswentry.delete(0,END)
    pswentry.insert(0,password)
    file1=open("students.txt","a")
    file1.write(password)
    file1.write("\n")

window=Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background="#4065A4")

#creer un Frame
frame=Frame(window,bg="#4065A4")
              

              
              
#crأ©ation d'images
width=300
height=300
images=PhotoImage(file="paswd.png").zoom(35).subsample(32)
canvas=Canvas(frame,width=width, height=height, bg="#4065A4",bd=0,highlightthickness=0)  
canvas.create_image(width/2,height/2,image=images)
canvas.pack(expand=YES)
canvas.grid(row=0,column=0,sticky=W)


#creer sous frame
rightframe=Frame(frame,bg="blue")

#creer unt titre
label=Label(frame,text="Mot de passe",font="helvetica 20", bg="#4065A4", fg="white")
label.grid(row=0,column=1,sticky=N)



#champ text
pswentry=Entry(rightframe,font="helvetica 20", bg="white", fg="black")
pswentry.pack()

#Bouton
b1=Button(rightframe,text="Generer Pasword",font="helvetica 15", bg="gray", fg="white", command=generer)
b1.pack(fill=X)




rightframe.grid(row=0,column=1,sticky=W)

frame.pack(expand=YES) 
     
window.mainloop()
            