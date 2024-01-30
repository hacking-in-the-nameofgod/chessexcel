import pygame as pyg
#how to make screen?

pyg.init()

WIDTH = 800
HEIGHT = 800

screen = pyg.display.set_mode([WIDTH, HEIGHT])
pyg.display.set_caption('ChessExcel by Vansh, Mervyn, Aarush')

wpieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
wlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
bpieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
blocs = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

cap_pieces_w = []
cap_pieces_b = []

which_turn = 0
selection = 100
chalega_kya = []

# load in images
bqueen = pyg.image.load(r'bq.png')
bqueen = pyg.transform.scale(bqueen, (80, 80))
bking = pyg.image.load(r'bk.png')
bking = pyg.transform.scale(bking, (80, 80))
brook = pyg.image.load(r'br.png')
brook = pyg.transform.scale(brook, (80, 80))
bbishop = pyg.image.load(r'bb.png')
bbishop = pyg.transform.scale(bbishop, (80, 80))
bknight = pyg.image.load(r'bn.png')
bknight = pyg.transform.scale(bknight, (80, 80))
bpawn = pyg.image.load(r'bp.png')
bpawn = pyg.transform.scale(bpawn, (65, 65))
wqueen = pyg.image.load(r'wq.png')
wqueen = pyg.transform.scale(wqueen, (80, 80))
wking = pyg.image.load(r'wk.png')
wking = pyg.transform.scale(wking, (80, 80))
wrook = pyg.image.load(r'wr.png')
wrook = pyg.transform.scale(wrook, (80, 80))
wbishop = pyg.image.load(r'wb.png')
wbishop = pyg.transform.scale(wbishop, (80, 80))
wknight = pyg.image.load(r'wn.png')
wknight = pyg.transform.scale(wknight, (80, 80))
wpawn = pyg.image.load(r'wp.png')
wpawn = pyg.transform.scale(wpawn, (65, 65))

white_images = [wpawn, wqueen, wking,
                wknight, wrook, wbishop]

black_images = [bpawn, bqueen, bking,
                bknight, brook, bbishop]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pyg.draw.rect(screen, 'blue', [600 - (column * 200), row * 100, 100, 100])
        else:
            pyg.draw.rect(screen, 'blue', [700 - (column * 200), row * 100, 100, 100])
        pyg.draw.rect(screen, 'white', [0, 800, WIDTH, 75])


def draw_pieces():
    for i in range(len(wpieces)):
        index = piece_list.index(wpieces[i])
        if wpieces[i] == 'pawn':
            screen.blit(
                wpawn, (wlocs[i][0] * 100 + 22, wlocs[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (wlocs[i]
                        [0] * 100 + 10, wlocs[i][1] * 100 + 10))

    for i in range(len(bpieces)):
        index = piece_list.index(bpieces[i])
        if bpieces[i] == 'pawn':
            screen.blit(
                bpawn, (blocs[i][0] * 100 + 22, blocs[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (blocs[i]
                        [0] * 100 + 10, blocs[i][1] * 100 + 10))


def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    for i in range(4): 
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    for i in range(4): 
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in wlocs and \
                (position[0], position[1] + 1) not in blocs and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in wlocs and \
                (position[0], position[1] + 2) not in blocs and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in blocs:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in blocs:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in wlocs and \
                (position[0], position[1] - 1) not in blocs and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in wlocs and \
                (position[0], position[1] - 2) not in blocs and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in wlocs:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in wlocs:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def check_valid_moves():
    if which_turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# main game loop
black_options = check_options(bpieces, blocs, 'black')
print ("Black options are :", black_options)
white_options = check_options(wpieces, wlocs, 'white')
print ("White options are ", white_options)
run = True
while run:
    
        
    screen.fill('dark gray')
    draw_board()
    draw_pieces()

    if selection != 100:
        chalega_kya = check_valid_moves()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            print (" END : quit detected")
            run = False
        if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            print ("Mouse event, and game not ended")
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            print (" Detected the cordinates of click" , click_coords)
            if which_turn <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in wlocs:
                    selection = wlocs.index(click_coords)
                    if which_turn == 0:
                        which_turn = 1
                if click_coords in chalega_kya and selection != 100:
                    wlocs[selection] = click_coords
                    if click_coords in blocs:
                        black_piece = blocs.index(click_coords)
                        cap_pieces_w.append(bpieces[black_piece])
                        if bpieces[black_piece] == 'king':
                            winner = 'white'
                        bpieces.pop(black_piece)
                        blocs.pop(black_piece)
                    black_options = check_options(
                        bpieces, blocs, 'black')
                    white_options = check_options(
                        wpieces, wlocs, 'white')
                    which_turn = 2
                    selection = 100
                    chalega_kya = []
            if which_turn > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in blocs:
                    selection = blocs.index(click_coords)
                    if which_turn == 2:
                        which_turn = 3
                if click_coords in chalega_kya and selection != 100:
                    blocs[selection] = click_coords
                    if click_coords in wlocs:
                        white_piece = wlocs.index(click_coords)
                        cap_pieces_b.append(wpieces[white_piece])
                        if wpieces[white_piece] == 'king':
                            winner = 'black'
                        wpieces.pop(white_piece)
                        wlocs.pop(white_piece)
                    black_options = check_options(
                        bpieces, blocs, 'black')
                    white_options = check_options(
                        wpieces, wlocs, 'white')
                    which_turn = 0
                    selection = 100
                    chalega_kya = []
        if event.type == pyg.KEYDOWN and game_over:
            print (" Game is over. Lets declare");
            if event.key == pyg.K_RETURN:
                game_over = False
                winner = ''
                wpieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                wlocs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                bpieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                blocs = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                cap_pieces_w = []
                cap_pieces_b = []
                which_turn = 0
                selection = 100
                chalega_kya = []
                black_options = check_options(
                    bpieces, blocs, 'black')
                white_options = check_options(
                    wpieces, wlocs, 'white')

    if winner != '':
        game_over = True
        print("The winner is: " , winner)
        break
        
    pyg.display.flip()

pyg.quit()
