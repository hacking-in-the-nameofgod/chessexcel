import tkinter
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import os
mainWindow =tkinter.Tk()
mainWindow.title("PVP")
mainWindow.geometry("5000x5000")


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

BQ = (Image.open("BQ.png"))
BQ1 = BQ.resize((50,50))
BQ1 = ImageTk.PhotoImage(BQ1)
BQpanel = Label(mainWindow, image = BQ1)
BQpanel.place(x=236, y=85)

BK = (Image.open("BK.png"))
BK1 = BK.resize((50,50))
BK1 = ImageTk.PhotoImage(BK1)
BKpanel = Label(mainWindow, image = BK1)
BKpanel.place(x=311, y=85)

BB1 = (Image.open("BB.png"))
BB11 = BB1.resize((50,50))
BB11 = ImageTk.PhotoImage(BB11)
BB11panel = Label(mainWindow, image = BB11)
BB11panel.place(x=386, y=85)

BB2 = (Image.open("BB.png"))
BB21 = BB2.resize((50,50))
BB21 = ImageTk.PhotoImage(BB21)
BB21panel = Label(mainWindow, image = BB21)
BB21panel.place(x=161, y=85)

BH1 = (Image.open("BH.png"))
BH11 = BH1.resize((50,50))
BH11 = ImageTk.PhotoImage(BH11)
BH11panel = Label(mainWindow, image = BH11)
BH11panel.place(x=86, y=85)

BH2 = (Image.open("BH.png"))
BH21 = BH2.resize((50,50))
BH21 = ImageTk.PhotoImage(BH21)
BH21panel = Label(mainWindow, image = BH21)
BH21panel.place(x=461, y=85)

BR1 = (Image.open("BR.png"))
BR11 = BR1.resize((50,50))
BR11 = ImageTk.PhotoImage(BR11)
BR11panel = Label(mainWindow, image = BR11)
BR11panel.place(x=11, y=85)

BR2 = (Image.open("BR.png"))
BR21 = BR2.resize((50,50))
BR21 = ImageTk.PhotoImage(BR21)
BR21panel = Label(mainWindow, image = BR21)
BR21panel.place(x=536, y=85)

BP1 = (Image.open("BP.png"))
BP11 = BP1.resize((50,50))
BP11 = ImageTk.PhotoImage(BP11)
BP11panel = Label(mainWindow, image = BP11)
BP11panel.place(x=11, y=160)

BP2 = (Image.open("BP.png"))
BP21 = BP2.resize((50,50))
BP21 = ImageTk.PhotoImage(BP21)
BP21panel = Label(mainWindow, image = BP21)
BP21panel.place(x=86, y=160)

BP3 = (Image.open("BP.png"))
BP31 = BP3.resize((50,50))
BP31 = ImageTk.PhotoImage(BP31)
BP31panel = Label(mainWindow, image = BP31)
BP31panel.place(x=161, y=160)

BP4 = (Image.open("BP.png"))
BP41 = BP4.resize((50,50))
BP41 = ImageTk.PhotoImage(BP41)
BP41panel = Label(mainWindow, image = BP41)
BP41panel.place(x=236, y=160)

BP5 = (Image.open("BP.png"))
BP51 = BP5.resize((50,50))
BP51 = ImageTk.PhotoImage(BP51)
BP51panel = Label(mainWindow, image = BP51)
BP51panel.place(x=311, y=160)

BP6 = (Image.open("BP.png"))
BP61 = BP6.resize((50,50))
BP61 = ImageTk.PhotoImage(BP61)
BP61panel = Label(mainWindow, image = BP61)
BP61panel.place(x=386, y=160)

BP7 = (Image.open("BP.png"))
BP71 = BP7.resize((50,50))
BP71 = ImageTk.PhotoImage(BP71)
BP71panel = Label(mainWindow, image = BP71)
BP71panel.place(x=461, y=160)

BP8 = (Image.open("BP.png"))
BP81 = BP8.resize((50,50))
BP81 = ImageTk.PhotoImage(BP81)
BP81panel = Label(mainWindow, image = BP81)
BP81panel.place(x=536, y=160)

WQ = (Image.open("WQ.png"))
WQ1 = WQ.resize((50,50))
WQ1 = ImageTk.PhotoImage(WQ1)
WQpanel = Label(mainWindow, image = WQ1,relief="solid")
WQpanel.place(x=236, y=610)

WK = (Image.open("WK.png"))
WK1 = WK.resize((50,50))
WK1 = ImageTk.PhotoImage(WK1)
WKpanel = Label(mainWindow, image = WK1,relief="solid")
WKpanel.place(x=311, y=610)

WB1 = (Image.open("WB.png"))
WB11 = WB1.resize((50,50))
WB11 = ImageTk.PhotoImage(WB11)
WB11panel = Label(mainWindow, image = WB11,relief="solid")
WB11panel.place(x=386, y=610)

WB2 = (Image.open("WB.png"))
WB21 = WB2.resize((50,50))
WB21 = ImageTk.PhotoImage(WB21)
WB21panel = Label(mainWindow, image = WB21,relief="solid")
WB21panel.place(x=161, y=610)

WH1 = (Image.open("WH.png"))
WH11 = WH1.resize((50,50))
WH11 = ImageTk.PhotoImage(WH11)
WH11panel = Label(mainWindow, image = WH11,relief="solid")
WH11panel.place(x=86, y=610)

WH2 = (Image.open("WH.png"))
WH21 = WH2.resize((50,50))
WH21 = ImageTk.PhotoImage(WH21)
WH21panel = Label(mainWindow, image = WH21,relief="solid")
WH21panel.place(x=461, y=610)

WR1 = (Image.open("WR.png"))
WR11 = WR1.resize((50,50))
WR11 = ImageTk.PhotoImage(WR11)
WR11panel = Label(mainWindow, image = WR11,relief="solid")
WR11panel.place(x=11, y=610)

WR2 = (Image.open("WR.png"))
WR21 = WR2.resize((50,50))
WR21 = ImageTk.PhotoImage(WR21)
WR21panel = Label(mainWindow, image = WR21,relief="solid")
WR21panel.place(x=536, y=610)

WP1 = (Image.open("WP.png"))
WP11 = WP1.resize((50,50))
WP11 = ImageTk.PhotoImage(WP11)
WP11panel = Label(mainWindow, image = WP11,relief="solid")
WP11panel.place(x=11, y=535)

WP2 = (Image.open("WP.png"))
WP21 = WP2.resize((50,50))
WP21 = ImageTk.PhotoImage(WP21)
WP21panel = Label(mainWindow, image = WP21,relief="solid")
WP21panel.place(x=86, y=535)

WP3 = (Image.open("WP.png"))
WP31 = WP3.resize((50,50))
WP31 = ImageTk.PhotoImage(WP31)
WP31panel = Label(mainWindow, image = WP31,relief="solid")
WP31panel.place(x=161, y=535)

WP4 = (Image.open("WP.png"))
WP41 = WP4.resize((50,50))
WP41 = ImageTk.PhotoImage(WP41)
WP41panel = Label(mainWindow, image = WP41,relief="solid")
WP41panel.place(x=236, y=535)

WP5 = (Image.open("WP.png"))
WP51 = WP5.resize((50,50))
WP51 = ImageTk.PhotoImage(WP51)
WP51panel = Label(mainWindow, image = WP51,relief="solid")
WP51panel.place(x=311, y=535)

WP6 = (Image.open("WP.png"))
WP61 = WP6.resize((50,50))
WP61 = ImageTk.PhotoImage(WP61)
WP61panel = Label(mainWindow, image = WP61,relief="solid")
WP61panel.place(x=386, y=535)

WP7 = (Image.open("WP.png"))
WP71 = WP7.resize((50,50))
WP71 = ImageTk.PhotoImage(WP71)
WP71panel = Label(mainWindow, image = WP71,relief="solid")
WP71panel.place(x=461, y=535)

WP8 = (Image.open("WP.png"))
WP81 = WP8.resize((50,50))
WP81 = ImageTk.PhotoImage(WP81)
WP81panel = Label(mainWindow, image = WP81,relief="solid")
WP81panel.place(x=536, y=535)


mainWindow.mainloop()
