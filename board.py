import tkinter
from PIL import ImageTk, Image
import os
mainWindow =tkinter.Tk()
mainWindow.title("PVP")
mainWindow.geometry("5000x5000")

board_canvas = tkinter.Canvas(mainWindow, borderwidth=1, width = 1000, height = 1000)
board_canvas.grid(row=8, column=8, columnspan=8, rowspan=8)

x = 75
y = 75
a = 0
b = 0

for j in range(0,4):
    x = 75
    b = b+75
    y = y + 75
    a = 0
    for i in range(0,4):

        a1 = board_canvas.create_rectangle(a, b, a+x, y, fill='white')
        a2 = board_canvas.create_rectangle(a+x, b, a+(2*x), y, fill='green')
        a = a + (2*x)

    a = 0
    x = 75
    b = b+75
    y = y+75

    for i in range(0,4):
        a1 = board_canvas.create_rectangle(a, b, a+x, y, fill='green')
        a2 = board_canvas.create_rectangle(a+x, b, a+(2*x), y, fill='white')
        a = a + (2*x)

img = ImageTk.PhotoImage(Image.open("D:\Aarush 11B\project\pieces\BQ"))
panel = tk.Label(root, image = img)


mainWindow.mainloop()
