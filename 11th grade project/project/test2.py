
import tkinter
from tkinter import *


win= tkinter.Tk()
win.title("Rounded Button")


win.geometry("700x300")




   

click_btn= PhotoImage(file='BK.png')
button= Button(win, image=click_btn,
borderwidth=0)
button.place(x = 0, y = 0)

click_btn1= PhotoImage(file='BQ.png')
button1= Button(win, image=click_btn1,
borderwidth=0)
button1.place(x = 75,y = 75)

text= Label(win, text= "")
text.pack(pady=30)

win.mainloop()
