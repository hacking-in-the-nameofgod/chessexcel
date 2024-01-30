x = True
y = True
r = 0
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

def w_move_pawn(master_board, piece_position, w_moved_position):
    piece_colour = "w"
    row_difference = ord(w_moved_position[1]) - ord(piece_position[1]) 
    if row_difference == 1 and w_moved_position[0] == piece_position[0]:  
        return True  
    elif row_difference == 2 and piece_position[1] == "2" and w_moved_position[0] == piece_position[0] and master_board[chr(ord(piece_position[1]) + 1) + piece_position[0]] == "":  
        return True 
    elif row_difference == 1 and abs(ord(w_moved_position[0]) - ord(piece_position[0])) == 1 and master_board[w_moved_position][0] != piece_colour: 
        return True  
    else:
        return False


def w_move_rook(master_board, piece_position, w_moved_position):
    piece_colour = "w"
    if piece_position[0] == w_moved_position[0]:
        return True
    elif piece_position[1]== w_moved_position[1]:
        return True
    else:
        return False




def w_move_knight(master_board, piece_position, w_moved_position):
    piece_colour = "w"
    row_difference = abs(ord(w_moved_position[1]) - ord(piece_position[1]))
    column_difference = abs(ord(w_moved_position[0]) - ord(piece_position[0]))
    if (row_difference == 2 and column_difference == 1) or (row_difference == 1 and column_difference == 2):
        if master_board[w_moved_position] == "" or master_board[w_moved_position][0] != piece_colour:
            return True  # Valid move
    else:
        return False  # Invalid move


def w_move_bishop(master_board, piece_position, w_moved_position):
    piece_colour = "w"
    row_difference = abs(ord(w_moved_position[1]) - ord(piece_position[1]))
    column_difference = abs(ord(w_moved_position[0]) - ord(piece_position[0]))

    if row_difference == column_difference:
        row_increment = 1 if w_moved_position[1] > piece_position[1] else -1
        col_increment = 1 if w_moved_position[0] > piece_position[0] else -1
        current_row = ord(piece_position[1]) + row_increment
        current_col = ord(piece_position[0]) + col_increment
        while current_row != ord(w_moved_position[1]):
            if master_board[chr(current_row) + chr(current_col)] != "":
                return False  
            current_row += row_increment
            current_col += col_increment

        if master_board[w_moved_position] == "" or master_board[w_moved_position][0] != piece_colour:
            return True  
            # Valid move
        else:
            return False
    else:
        return False  


def w_move_queen(master_board, piece_position, w_moved_position):
    piece_colour = "w"

def w_move_king(master_board, piece_position, w_moved_position):
    piece_colour = "w"

def b_move_pawn(master_board, piece_position, b_moved_position):
    piece_colour = "b"

    row_difference = ord(b_moved_position[1]) - ord(piece_position[1]) 

    if row_difference == -1 and b_moved_position[0] == piece_position[0]:  
        return True  
    elif row_difference == -2 and piece_position[1] == "7" and b_moved_position[0] == piece_position[0] and master_board[chr(ord(piece_position[1]) - 1) + piece_position[0]] == "":  
        return True  
    elif row_difference == -1 and abs(ord(b_moved_position[0]) - ord(piece_position[0])) == 1 and master_board[b_moved_position][0] != piece_colour:  
        return True  
    else:
        return False  
        
def b_move_rook(master_board, piece_position, b_moved_position):
    piece_colour = "b"
    if piece_position[0] == b_moved_position[0]:
        return True
    elif piece_position[1]== b_moved_position[1]:
        return True
    else:
        return False

def b_move_knight(master_board, piece_position, b_moved_position):
    piece_colour = "b"
    row_difference = abs(ord(b_moved_position[1]) - ord(piece_position[1]))
    column_difference = abs(ord(b_moved_position[0]) - ord(piece_position[0]))
    if (row_difference == 2 and column_difference == 1) or (row_difference == 1 and column_difference == 2):
        if master_board[b_moved_position] == "" or master_board[b_moved_position][0] != piece_colour:
            return True 
    else:
        return False 

def b_move_bishop(master_board, piece_position, b_moved_position):
    piece_colour = "b"
    row_difference = abs(ord(w_moved_position[1]) - ord(piece_position[1]))
    column_difference = abs(ord(w_moved_position[0]) - ord(piece_position[0]))

    if row_difference == column_difference:
        if w_moved_position[1] > piece_position[1]:
            row_increment = 1
        else:
            row_increment = -1
        col_increment = 1 if w_moved_position[0] > piece_position[0] else -1
        current_row = ord(piece_position[1]) + row_increment
        current_col = ord(piece_position[0]) + col_increment
        while current_row != ord(w_moved_position[1]):
            if master_board[chr(current_row) + chr(current_col)] != "":
                return False  
            current_row += row_increment
            current_col += col_increment

        if master_board[w_moved_position] == "" or master_board[w_moved_position][0] != piece_colour:
            return True  
            # Valid move
        else:
            return False
    else:
        return False  



def b_move_queen(master_board, piece_position, b_moved_position):
    piece_colour = "b"

def b_move_king(master_board, piece_position, b_moved_position):
    piece_colour = "b"


while r != "End": #main game loop
    while x == True:
        w_moved_piece = input("Enter the white piece to be moved to: ")
        w_moved_position = input("Enter position to be moved to: ")

        for i in list(master_board.keys()):
            if master_board[i] == w_moved_piece:
                piece_position = i
        piece_type = w_moved_piece[1]  #piece type from the piece name

        if w_moved_position in list(master_board.keys()): # in the box check
            if w_moved_piece in list(master_board.values()):
                if master_board[w_moved_position][0] != "w":
                    if piece_type == "p":
                        validity = w_move_pawn(master_board, piece_position, w_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue                  

                    elif piece_type == "r":
                        validity = w_move_rook(master_board, piece_position, w_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "n":
                        validity = w_move_knight(master_board, piece_position, w_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "k":
                        validity = w_move_king(master_board, piece_position, w_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "b":
                        validity = w_move_bishop(master_board, piece_position, w_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "q":
                        validity = w_move_queen(master_board, piece_position, w_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
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

        for i in list(master_board.keys()):
            if master_board[i] == b_moved_piece:
                piece_position = i
        piece_type = b_moved_piece[1]  #piece type from the piece name
        
        if b_moved_position in list(master_board.keys()): # in the box check
            if b_moved_piece in list(master_board.values()):
                if master_board[b_moved_position][0] != "b":

                    if piece_type == "p":
                        validity = b_move_pawn(master_board, piece_position, b_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "r":
                        validity = b_move_rook(master_board, piece_position, b_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "n":
                        b_move_knight(master_board, piece_position, b_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "k":
                        b_move_king(master_board, piece_position, b_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "b":
                        b_move_bishop(master_board, piece_position, b_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
                    elif piece_type == "q":
                        b_move_queen(master_board, piece_position, b_moved_position)
                        if validity == True:
                            master_board[w_moved_position] = w_moved_piece
                            print(master_board)
                            break
                        else:
                            print("Invalid Move)")
                            continue   
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


    