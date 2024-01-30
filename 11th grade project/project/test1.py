import tkinter
mainWindow =tkinter.Tk()

board_canvas = tkinter.Canvas(mainWindow, borderwidth=1)
board_canvas.grid(row=1, column=0, sticky='ew', columnspan=8, rowspan=8)

x = 0
y = 0

for i in range(0,8):
    square = board_canvas.create_rectangle(x,y,x+75,y+75,bg = "green")
    
    


 
