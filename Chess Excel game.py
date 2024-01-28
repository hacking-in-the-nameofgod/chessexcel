import pygame as pyg
pyg.init()
screen = pyg.display.set_mode((800, 600))
pyg.display.set_caption('ChessExcel by Vansh, Mervyn, Aarush')

import pygame as pyg

pyg.init()

WIDTH = 800
HEIGHT = 800

screen = pyg.display.set_mode([WIDTH, HEIGHT])
pyg.display.set_caption('ChessExcel by Vansh, Mervyn, Aarush')

font = pyg.font.Font('freesansbold.ttf', 20)
medium_font = pyg.font.Font('freesansbold.ttf', 40)
big_font = pyg.font.Font('freesansbold.ttf', 50)

# timer = pyg.time.Clock()
#fps = 60

# game variables and images
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

# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
which_turn = 0
selection = 100
chalega_kya = []

# load in images
bqueen = pyg.image.load(r'bq.png')
bqueen = pyg.transform.scale(bqueen, (80, 80))
bqueens = pyg.transform.scale(bqueen, (45, 45))
bking = pyg.image.load(r'bk.png')
bking = pyg.transform.scale(bking, (80, 80))
bkings = pyg.transform.scale(bking, (45, 45))
brook = pyg.image.load(r'br.png')
brook = pyg.transform.scale(brook, (80, 80))
brooks = pyg.transform.scale(brook, (45, 45))
bbishop = pyg.image.load(r'bb.png')
bbishop = pyg.transform.scale(bbishop, (80, 80))
bbishops = pyg.transform.scale(bbishop, (45, 45))
bknight = pyg.image.load(r'bn.png')
bknight = pyg.transform.scale(bknight, (80, 80))
bknights = pyg.transform.scale(bknight, (45, 45))
bpawn = pyg.image.load(r'bp.png')
bpawn = pyg.transform.scale(bpawn, (65, 65))
bpawns = pyg.transform.scale(bpawn, (45, 45))
wqueen = pyg.image.load(r'wq.png')
wqueen = pyg.transform.scale(wqueen, (80, 80))
wqueens = pyg.transform.scale(wqueen, (45, 45))
wking = pyg.image.load(r'wk.png')
wking = pyg.transform.scale(wking, (80, 80))
wkings = pyg.transform.scale(wking, (45, 45))
wrook = pyg.image.load(r'wr.png')
wrook = pyg.transform.scale(wrook, (80, 80))
wrooks = pyg.transform.scale(wrook, (45, 45))
wbishop = pyg.image.load(r'wb.png')
wbishop = pyg.transform.scale(wbishop, (80, 80))
wbishops = pyg.transform.scale(wbishop, (45, 45))
wknight = pyg.image.load(r'wn.png')
wknight = pyg.transform.scale(wknight, (80, 80))
wknights = pyg.transform.scale(wknight, (45, 45))
wpawn = pyg.image.load(r'wp.png')
wpawn = pyg.transform.scale(wpawn, (65, 65))
wpawns = pyg.transform.scale(wpawn, (45, 45))

white_images = [wpawn, wqueen, wking,
                wknight, wrook, wbishop]
small_white_images = [wpawns, wqueens, wkings, wknights,
                      wrooks, wbishops]

black_images = [bpawn, bqueen, bking,
                bknight, brook, bbishop]
small_black_images = [bpawns, bqueens, bkings, bknights,
                      brooks, bbishops]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

counter = 0
winner = ''
game_over = False


# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pyg.draw.rect(screen, 'light gray', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pyg.draw.rect(screen, 'light gray', [
                             700 - (column * 200), row * 100, 100, 100])
        pyg.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pyg.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pyg.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(
            status_text[which_turn], True, 'black'), (20, 820))
        for i in range(9):
            pyg.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pyg.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))


# draw pieces onto board
def draw_pieces():
    for i in range(len(wpieces)):
        index = piece_list.index(wpieces[i])
        if wpieces[i] == 'pawn':
            screen.blit(
                wpawn, (wlocs[i][0] * 100 + 22, wlocs[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (wlocs[i]
                        [0] * 100 + 10, wlocs[i][1] * 100 + 10))
        if which_turn < 2:
            if selection == i:
                pyg.draw.rect(screen, 'red', [wlocs[i][0] * 100 + 1, wlocs[i][1] * 100 + 1,
                                                 100, 100], 2)

    for i in range(len(bpieces)):
        index = piece_list.index(bpieces[i])
        if bpieces[i] == 'pawn':
            screen.blit(
                bpawn, (blocs[i][0] * 100 + 22, blocs[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (blocs[i]
                        [0] * 100 + 10, blocs[i][1] * 100 + 10))
        if which_turn >= 2:
            if selection == i:
                pyg.draw.rect(screen, 'blue', [blocs[i][0] * 100 + 1, blocs[i][1] * 100 + 1,
                                                  100, 100], 2)


# function to check all pieces valid options on board
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


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    for i in range(4):  # up-right, up-left, down-right, down-left
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


# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    for i in range(4):  # down, up, right, left
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


# check valid pawn moves
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


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = blocs
        friends_list = wlocs
    else:
        friends_list = blocs
        enemies_list = wlocs
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if which_turn < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    if which_turn < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pyg.draw.circle(
            screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured pieces on side of screen
def draw_captured():
    for i in range(len(cap_pieces_w)):
        captured_piece = cap_pieces_w[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50 * i))
    for i in range(len(cap_pieces_b)):
        captured_piece = cap_pieces_b[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50 * i))


# draw a flashing square around king if in check
def draw_check():
    if which_turn < 2:
        if 'king' in wpieces:
            king_index = wpieces.index('king')
            king_location = wlocs[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    
                     pyg.draw.rect(screen, 'dark red', [wlocs[king_index][0] * 100 + 1,
                                                              wlocs[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in bpieces:
            king_index = bpieces.index('king')
            king_location = blocs[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    
                    pyg.draw.rect(screen, 'dark blue', [blocs[king_index][0] * 100 + 1,
                                                               blocs[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    pyg.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(
        f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!',
                True, 'white'), (210, 240))


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
    draw_captured()
    draw_check()
    if selection != 100:
        chalega_kya = check_valid_moves()
        draw_valid(chalega_kya)
    # event handling
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
        print("Can't declare winner")
        game_over = True
        draw_game_over()

    pyg.display.flip()

pyg.quit()
