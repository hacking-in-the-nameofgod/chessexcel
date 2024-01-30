import pygame
r = 0
x = True
y= True

#Ill define all the functions:



# (row,column)

master_board = {
    "a1": "wr1",  "b1":"wn1",  "c1":"wb1",  "d1":"wq",  "e1":"wk",  "f1":"wb2",  "g1":"wn2",  "h1":"wr2",
    "a2": "wp1",  "b2":"wp2",  "c2":"wp3",  "d2":"wp4",  "e2":"wp5",  "f2":"wp6",  "g2":"wp7",  "h2":"wp8",
    "a3": "", "b3":"", "c3":"", "d3":"", "e3":"", "f3":"", "g3":"", "h3":"",
    "a4": "", "b4":"", "c4":"", "d4":"", "e4":"", "f4":"", "g4":"", "h4":"",
    "a5": "", "b5":"", "c5":"", "d5":"", "e5":"", "f5":"", "g5":"", "h5":"",
    "a6": "", "b6":"", "c6":"", "d6":"", "e6":"", "f6":"", "g6":"", "h6":"",
    "a7": "bp1",   "b7":"bp2",   "c7":"bp3",   "d7":"bp4",   "e7":"bp5",   "f7":"bp6",   "g7":"bp7",   "h7":"bp8",
    "a8": "br1",   "b8":"bn1",   "c8":"bb1",   "d8":"bq",   "e8":"bk",   "f8":"bb2",   "g8":"bn2",   "h8":"br2"
}


while r != "End": #main game loop
    x = True

    while x == True:
        w_moved_piece = input ("Enter the white piece to be moved to: ")
        w_moved_position=input("Enter position to be moved to: ")
#        while w_moved_position not in master_board.keys():
#            w_moved_piece=input("Error that position doesnt exist; Enter piece to be moved to: ")
#            w_moved_position=input("Error that position doesnt exist; Enter position to be moved to: ")
#        while w_moved_piece not in master_board.values():
#            w_moved_piece=input("Error that piece doesnt exist; Enter piece to be moved to: ")
#            w_moved_position=input("Error that piece doesnt exist; Enter position to be moved to: ")
#        while master_board[w_moved_position][0] == "w":
#            w_moved_piece=input("Error that position cannot be accessed; Enter piece to be moved to: ")
#            w_moved_position=input("Error that position cannot be accessed; Enter position to be moved to: ")

        if w_moved_position not in master_board.keys(): # in the box check
            if w_moved_piece in master_board.values():
                if master_board[w_moved_position][0] != "w":
                    for i in list(master_board.keys()):
                        if master_board[i] == w_moved_piece:
                            master_board[i] = "" # replace the origional square

                    master_board[w_moved_position] = w_moved_piece
                    print(master_board)
                    break
                else:
                    print ("Error")
                    print ("Please Enter again 1")
                    continue # figure out a way to send code back to line 20
            else:
                print ("Error")
                print ("Please Enter again ")
                continue # figure out a way to send code back to line 20
        else:
            print ("Error")
            print ("Please Enter again: ") # figure out a way to send code back to line 20
            continue
        




    while y == True:
        b_moved_piece = input ("Enter the white piece to be moved to: ")
        b_moved_position=input("Enter position to be moved to: ")
#        while b_moved_position not in master_board.keys():
#            b_moved_piece=input("Error that position doesnt exist; Enter piece to be moved to: ")
#            b_moved_position=input("Error that position doesnt exist; Enter position to be moved to: ")
#        while b_moved_piece not in master_board.values():
#            b_moved_piece=input("Error that piece doesnt exist; Enter piece to be moved to: ")
#            b_moved_position=input("Error that piece doesnt exist; Enter position to be moved to: ")
#        while master_board[b_moved_position][0] == "w":
#            b_moved_piece=input("Error that position doesnt exist; Enter piece to be moved to: ")
#            b_moved_position=input("Error that position doesnt exist; Enter position to be moved to: ")
        
        if b_moved_position not in master_board.keys(): # in the box check
            if b_moved_piece in master_board.values():
                if master_board[b_moved_position][0] != "b":
                    for i in list(master_board.keys()):
                        if master_board[i] == b_moved_piece:
                            master_board[i] = ""

                    master_board[b_moved_position] = b_moved_piece
                    print(master_board)
                    break
                else:
                    print ("Error")
                    print ("Please Enter again 1")
                    continue # figure out a way to send code back to line 20
            else:
                print ("Error")
                print ("Please Enter again ")
                continue # figure out a way to send code back to line 20
        else:
            print ("Error")
            print ("Please Enter again: ") # figure out a way to send code back to line 20
            continue






