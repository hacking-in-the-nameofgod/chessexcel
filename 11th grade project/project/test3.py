import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import os
mainWindow =tkinter.Tk()
mainWindow.title("PVP")
mainWindow.geometry("5000x5000")

a = 75
b = True

def move(button):
    click_btn1= PhotoImage(file='BK.png')
    #button1= Button(image=click_btn1, borderwidth=0,width = 75, height = 75)
    #button1.place(x=a+75, y = 75)
    button.place(x=a+75, y = 75)
    button.pack()
    print("function")
    
    
    

revert = Button(text = "Revert",bg = "yellow")
revert.place(x = 675, y = 75, height = 150, width = 150)

A8 = Button()
A8.place(x=0,y=75, height = 75, width = 75)

B8 = Button(bg = "green")
B8.place(x=75,y=75, height = 75, width = 75)

C8 = Button()
C8.place(x=150,y=75, height = 75, width = 75)

D8 = Button(bg = "green")
D8.place(x=225,y=75, height = 75, width = 75)

E8 = Button()
E8.place(x=300,y=75, height = 75, width = 75)

F8 = Button(bg = "green")
F8.place(x=375,y=75, height = 75, width = 75)

G8 = Button()
G8.place(x=450,y=75, height = 75, width = 75)

H8 = Button(bg = "green")
H8.place(x=525,y=75, height = 75, width = 75)

A7 = Button(bg = "green")
A7.place(x=0,y=150, height = 75, width = 75)

B7 = Button()
B7.place(x=75,y=150, height = 75, width = 75)

C7 = Button(bg = "green")
C7.place(x=150,y=150, height = 75, width = 75)

D7 = Button()
D7.place(x=225,y=150, height = 75, width = 75)

E7 = Button(bg = "green")
E7.place(x=300,y=150, height = 75, width = 75)

F7 = Button()
F7.place(x=375,y=150, height = 75, width = 75)

G7 = Button(bg = "green")
G7.place(x=450,y=150, height = 75, width = 75)

H7 = Button()
H7.place(x=525,y=150, height = 75, width = 75)

A6 = Button()
A6.place(x=0,y=225, height = 75, width = 75)

B6 = Button(bg = "green")
B6.place(x=75,y=225, height = 75, width = 75)

C6 = Button()
C6.place(x=150,y=225, height = 75, width = 75)

D6 = Button(bg = "green")
D6.place(x=225,y=225, height = 75, width = 75)

E6 = Button()
E6.place(x=300,y=225, height = 75, width = 75)

F6 = Button(bg = "green")
F6.place(x=375,y=225, height = 75, width = 75)

G6 = Button()
G6.place(x=450,y=225, height = 75, width = 75)

H6 = Button(bg = "green")
H6.place(x=525,y=225, height = 75, width = 75)

A5 = Button(bg = "green")
A5.place(x=0,y=300, height = 75, width = 75)

B5 = Button()
B5.place(x=75,y=300, height = 75, width = 75)

C5 = Button(bg = "green")
C5.place(x=150,y=300, height = 75, width = 75)

D5 = Button()
D5.place(x=225,y=300, height = 75, width = 75)

E5 = Button(bg = "green")
E5.place(x=300,y=300, height = 75, width = 75)

F5 = Button()
F5.place(x=375,y=300, height = 75, width = 75)

G5 = Button(bg = "green")
G5.place(x=450,y=300, height = 75, width = 75)

H5 = Button()
H5.place(x=525,y=300, height = 75, width = 75)

A4 = Button()
A4.place(x=0,y=375, height = 75, width = 75)

B4 = Button(bg = "green")
B4.place(x=75,y=375, height = 75, width = 75)

C4 = Button()
C4.place(x=150,y=375, height = 75, width = 75)

D4 = Button(bg = "green")
D4.place(x=225,y=375, height = 75, width = 75)

E4 = Button()
E4.place(x=300,y=375, height = 75, width = 75)

F4 = Button(bg = "green")
F4.place(x=375,y=375, height = 75, width = 75)

G4 = Button()
G4.place(x=450,y=375, height = 75, width = 75)

H4 = Button(bg = "green")
H4.place(x=525,y=375, height = 75, width = 75)

A3 = Button(bg = "green")
A3.place(x=0,y=450, height = 75, width = 75)

B3 = Button()
B3.place(x=75,y=450, height = 75, width = 75)

C3 = Button(bg = "green")
C3.place(x=150,y=450, height = 75, width = 75)

D3 = Button()
D3.place(x=225,y=450, height = 75, width = 75)

E3 = Button(bg = "green")
E3.place(x=300,y=450, height = 75, width = 75)

F3 = Button()
F3.place(x=375,y=450, height = 75, width = 75)

G3 = Button(bg = "green")
G3.place(x=450,y=450, height = 75, width = 75)

H3 = Button()
H3.place(x=525,y=450, height = 75, width = 75)

A2 = Button()
A2.place(x=0,y=525, height = 75, width = 75)

B2 = Button(bg = "green")
B2.place(x=75,y=525, height = 75, width = 75)

C2 = Button()
C2.place(x=150,y=525, height = 75, width = 75)

D2 = Button(bg = "green")
D2.place(x=225,y=525, height = 75, width = 75)

E2 = Button()
E2.place(x=300,y=525, height = 75, width = 75)

F2 = Button(bg = "green")
F2.place(x=375,y=525, height = 75, width = 75)

G2 = Button()
G2.place(x=450,y=525, height = 75, width = 75)

H2 = Button(bg = "green")
H2.place(x=525,y=525, height = 75, width = 75)

A1 = Button(bg = "green")
A1.place(x=0,y=600, height = 75, width = 75)

B1 = Button()
B1.place(x=75,y=600, height = 75, width = 75)

C1 = Button(bg = "green")
C1.place(x=150,y=600, height = 75, width = 75)

D1 = Button()
D1.place(x=225,y=600, height = 75, width = 75)

E1 = Button(bg = "green")
E1.place(x=300,y=600, height = 75, width = 75)

F1 = Button()
F1.place(x=375,y=600, height = 75, width = 75)

G1 = Button(bg = "green")
G1.place(x=450,y=600, height = 75, width = 75)

H1 = Button()
H1.place(x=525,y=600, height = 75, width = 75)

print("hi")


click_btn= PhotoImage(file= 'BK.png')
button= Button(image=click_btn, borderwidth=0,width = 75, height = 75)
button['command'] = move(button)
button.place(x = a, y = 75)
    


mainWindow.mainloop()

