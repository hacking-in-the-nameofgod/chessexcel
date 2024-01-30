import pygame
r = 0
x = True


# (row,column)

white_pieces = {"wr1":[1,1], "wn1": [1,2], "wb1":[1,3], "wq": [1,4], "wk": [1,5], "wb2": [1,6], "wn2":[1,7], "wr2":[1,8],
"wp1":[2,1], "wp2":[2,2], "wp3":[2,3], "wp4":[2,4], "wp5":[2,5], "wp6":[2,6], "wp7":[2,7], "wp8":[2,8]} 

black_pieces = {"bp1":[7,1], "bp2":[7,2], "bp3":[7,3], "bp4":[7,4], "bp5":[7,5], "bp6":[7,6], "bp7":[7,7], "bp8":[7,8],
"br1":[8,1], "bn1": [8,2], "bb1":[8,3], "bq": [8,4], "bk": [8,5], "bb2": [8,6], "bn2":[8,7], "br2":[8,8]}


#Game loop. Till game ends it runs and returns the win or loss or stalemate
while r != "End":
    x = True
## Black Pieces entry.... check the loop in case of illegal move

    while x == True:
        w_moved_piece = input ("Enter the white piece to be moved to: ")
        w_moved_row = int (input ("Enter the row to be moved to: "))
        w_moved_file = int(input ("Enter the file to be moved to: "))

        if w_moved_row <=8 and w_moved_row>0 and w_moved_file <=8 and w_moved_row>0: # in the box check
            if w_moved_piece in white_pieces:
                if [w_moved_row, w_moved_file] not in list(white_pieces.values()):
                    white_pieces[w_moved_piece] = [w_moved_row, w_moved_file]
                    print (w_moved_piece, "moved to" , white_pieces[w_moved_piece])
                    break
                else:
                    print ("Error")
                    print ("Please Enter again 1")
                    continue # figure out a way to send code back to line 20
            else:
                print ("Error")
                print ("Please Enter again 1")
                continue # figure out a way to send code back to line 20
        else:
            print ("Error")
            print ("Please Enter again: ") # figure out a way to send code back to line 20
            continue


## Black Pieces entry.... check the loop in case of illegal move

    while x == True:
        b_moved_piece = input ("Enter the black piece to be moved to: ")
        b_moved_row = int(input ("Enter the row to be moved to: "))
        b_moved_file = int(input ("Enter the file to be moved to: "))

        if b_moved_row <=8 and b_moved_row>0 and b_moved_file <=8 and b_moved_row>0: # in the box check
            if b_moved_piece in black_pieces:
                if [b_moved_row, b_moved_piece] not in list(black_pieces.values()):
                    black_pieces[b_moved_piece] = [b_moved_row, b_moved_piece]
                    print (b_moved_piece, "moved to" , black_pieces[b_moved_piece])
                    break
                else:
                    print ("Error")
                    print ("Please Enter again 1")
                    continue # figure out a way to send code back to line 20
            else:
                print ("Error")
                print ("Please Enter again 1")
                continue # figure out a way to send code back to line 20
        else:
            print ("Error")
            print ("Please Enter again: ") # figure out a way to send code back to line 20
            continue


        