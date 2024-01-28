import pygame;import pygame.font;import pygame.time;from utils.functions import get_moves
pygame.init()#initializing the game window

font = pygame.font.SysFont("segoeui", 26);winner_font = pygame.font.SysFont("segoeui", 50)# Declare font sizes

# Create the screen
screen_width, screen_height = 800, 600#Screen Size Declaration
screen = pygame.display.set_mode((screen_width, screen_height))#screen_display


pygame.display.set_caption("Caterply")#title
exit = False;game_over = False#game_over value intialize

# Chessboard properties
board_size = 8;square_size = min(screen_width, screen_height) // (board_size + 1)#boardSize and SqaureSize
bgColor = (128, 128, 128)#background color values
selected_color = (255, 90, 48);color1 = (238,238,210);color2 = (118,150,86)#RGB Tuple Values declaration
pieces = {#board Pieces Dictionary Declaration
    "black_pawn": pygame.image.load("images/Egg_black_pawn.png"),#Drawing black pawn on Board
    "black_rook": pygame.image.load("images/Heavy_caterpillar_black_rook.png"),#Drawing black rook on Board
    "black_knight": pygame.image.load("images/Caterpillar_black_knight.png"),
    "black_bishop": pygame.image.load("images/Cockoon_black_bishop.png"),#Drawing black bishop on Board
    "black_queen": pygame.image.load("images/Butterfly_black_queen.png"),#Drawing black Queen on Board
    "black_king": pygame.image.load("images/Butterfly_black_King.png"),#Drawing black King on Board
    "white_pawn": pygame.image.load("images/Egg_white_pawn.png"),#Drawing White pawn on Board
    "white_rook": pygame.image.load("images/Heavy_caterpillar_white_rook.png"),#Drawing White rook on Board
    "white_knight": pygame.image.load("images/Caterpillar_white_knight.png"),#Drawing white knight on Board
    "white_bishop": pygame.image.load("images/Cockoon_white_bishop.png"),#Drawing white bishop on Board
    "white_queen": pygame.image.load("images/Butterfly_white_queen.png"),#Drawing white queen on Board
    "white_king": pygame.image.load("images/Butterfly_white_King.png")#Drawing white king on Board
}

captured_pieces = [];winner = None#Initializing Captured Box Pieces List and Winner
time_limit = 180000;start_time =pygame.time.get_ticks();white_time = time_limit;black_time = time_limit# Timer's limit's Values Declare
# Create the chessboard representation as a 2D list
chessBoard = [[None for _ in range(board_size)] for _ in range(board_size)]# Drawing chessboard

# Draw the chessboard

# Draw the black pieces
chessBoard[0][0] = "black_rook";chessBoard[0][1] = "black_knight";chessBoard[0][2] = "black_bishop";chessBoard[0][3] = "black_king";chessBoard[0][4] = "black_queen";chessBoard[0][5] = "black_bishop";chessBoard[0][6] = "black_knight";chessBoard[0][7] = "black_rook";chessBoard[1][0] = "black_pawn";chessBoard[1][1] = "black_pawn";chessBoard[1][2] = "black_pawn";chessBoard[1][3] = "black_pawn";chessBoard[1][4] = "black_pawn";chessBoard[1][5] = "black_pawn";chessBoard[1][6] = "black_pawn";chessBoard[1][7] = "black_pawn"
"""chessBoard[0][0] = "black_rook"
chessBoard[0][1] = "black_knight"
chessBoard[0][2] = "black_bishop"
chessBoard[0][3] = "black_king"
chessBoard[0][4] = "black_queen"
chessBoard[0][5] = "black_bishop"
chessBoard[0][6] = "black_knight"
chessBoard[0][7] = "black_rook"
chessBoard[1][0] = "black_pawn"
chessBoard[1][1] = "black_pawn"
chessBoard[1][2] = "black_pawn"
chessBoard[1][3] = "black_pawn"
chessBoard[1][4] = "black_pawn"
chessBoard[1][5] = "black_pawn"
chessBoard[1][6] = "black_pawn"
chessBoard[1][7] = "black_pawn"""

# Draw the white pieces
chessBoard[7][0] = "white_rook";chessBoard[7][1] = "white_knight";chessBoard[7][2] = "white_bishop";chessBoard[7][3] = "white_king";chessBoard[7][4] = "white_queen";chessBoard[7][5] = "white_bishop";chessBoard[7][6] = "white_knight";chessBoard[7][7] = "white_rook";chessBoard[6][0] = "white_pawn";chessBoard[6][1] = "white_pawn";chessBoard[6][2] = "white_pawn";chessBoard[6][3] = "white_pawn";chessBoard[6][4] = "white_pawn";chessBoard[6][5] = "white_pawn";chessBoard[6][6] = "white_pawn";chessBoard[6][7] = "white_pawn"
"""""
chessBoard[7][0] = "white_rook"
chessBoard[7][1] = "white_knight"
chessBoard[7][2] = "white_bishop"
chessBoard[7][3] = "white_king"
chessBoard[7][4] = "white_queen"
chessBoard[7][5] = "white_bishop"
chessBoard[7][6] = "white_knight"
chessBoard[7][7] = "white_rook"
chessBoard[6][0] = "white_pawn"
chessBoard[6][1] = "white_pawn"
chessBoard[6][2] = "white_pawn"
chessBoard[6][3] = "white_pawn"
chessBoard[6][4] = "white_pawn"
chessBoard[6][5] = "white_pawn"
chessBoard[6][6] = "white_pawn"
chessBoard[6][7] = "white_pawn"""

# Calculating chessboard's origin's Positon to x and y axis
start_x = (screen_width - (board_size * square_size)) // 2;start_y = (screen_height - (board_size * square_size)) // 2
def draw_board():#drawing chess board
    for row in range(board_size):#iterating over board size for each row and colum in 2d Array List(Matrix)
        for column in range(board_size):
            if (row + column) % 2 == 0:color = color1#validating for Even row and column value for color 1 and 2
            else:color = color2#
            if (possible_moves is not None and (row, column) in possible_moves) or (selected_piece_row ==row and selected_piece_col == column):
                color = selected_color #checking all the best possible moves for user selction using initial bfs approach
                #drawing the rectangle on the screen
            pygame.draw.rect(screen, color, pygame.Rect((start_x + column * square_size), (start_y + row * square_size), square_size, square_size))


            current_turn_text = font.render(f"Current Turn: {turn.capitalize()}", True, (255, 255, 255))# User's Black input move String text value Display
            screen.blit(current_turn_text, (280, 0))#displaying the current move on screen

            white_time_text = font.render(f"White Time: {white_time // 1000}", True, (255, 255, 255)) #displaying String text for each White player's remaining time
            screen.blit(white_time_text, (60, 0))#displaying the current move on screen

            black_time_text = font.render(f"Black Time: {black_time // 1000}", True, (255, 255, 255)) #displaying String text for each Black player's remaining time
            screen.blit(black_time_text, (540, 0))#displaying the current move on screen


            if game_over:# Checking the game over for winning the game and printing it's Text
                pygame.draw.rect(screen, bgColor, pygame.Rect((start_x + column * square_size), (start_y + row * square_size), square_size, square_size))  # Drawing the Rectangle on screen
                winner_text = winner_font.render(f"Winner: {winner.capitalize()}", True, (255,255,255) if winner == "white" else (0,0,0))#winner's text Declare
                text_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 2))#rectangular Text
                screen.blit(winner_text, text_rect)#drawing winner and rectangular text on screen

            piece = chessBoard[row][column]#Board Piece Declaration
            if piece:#checking piece is on Board
                piece_img = pygame.transform.scale(pieces[piece], (square_size, square_size))# Board's Piece Value decalre
                screen.blit(piece_img, (start_x + column * square_size, start_y + row * square_size))#displaying the Boardpieces

#initlaizing Board Selected Pieces's row and Colm
selected_piece = None;selected_piece_row = None;selected_piece_col = None
turn = "white"#White pieces Value Declare
possible_moves = []#initializing possible moves

def handleClick(row,col):
    print("Caterply's Pieces Inputs!", row, col)#printing User's Input
    global selected_piece, selected_piece_row, selected_piece_col, turn, possible_moves, winner, game_over, exit#Values declareation globally

    # Checking selected piece and it's the player's Moves
    if selected_piece and possible_moves is not None and (row,col) in possible_moves and selected_piece.startswith(turn):
        # If the king is captured declare the winner and set game_over to True
        if chessBoard[row][col] and chessBoard[row][col].endswith("king"):
            print("Game over!")#printing game over
            winner = turn#winner's move's value
            game_over = True#Game Over's True Value Initlizing
            chessBoard[row][col] = selected_piece# Moving the selected piece to the new Index position
            chessBoard[selected_piece_row][selected_piece_col] = None# Returning the Initilized Moves on Board Moves
            return
        
        # If the selected piece is a pawn and it reaches the other side of the board, promote it to a queen
        if selected_piece.endswith("pawn") and (row == 0 or row == board_size - 1):
            selected_piece = selected_piece.replace("pawn", "queen")
        # Move the selected piece to the new position
        chessBoard[row][col] = selected_piece
        # Clear the old position
        chessBoard[selected_piece_row][selected_piece_col] = None
        # Switch turn to the other player
        turn = "white" if turn == "black" else "black"
        selected_piece = None
    elif chessBoard[row][col] and chessBoard[row][col].startswith(turn):
        # If the clicked square contains a piece of the player's color, select it
        selected_piece = chessBoard[row][col]
        selected_piece_row, selected_piece_col = row, col
        possible_moves = get_moves(chessBoard[row][col], row, col, chessBoard, board_size, turn)
    else:
        # If the clicked square is empty or contains an opponent's piece, deselect
        selected_piece = None



#Game loop
while not exit:
    for event in pygame.event.get():
        #'Exiting the game using 'ESC' or 'X' key values
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mouse_x, mouse_y = event.pos
            # Handle logic if clicked inside the board
            if start_x <= mouse_x <= start_x + (board_size * square_size) and start_y <= mouse_y <= start_y + (board_size * square_size):
                #row and colm drawing
                col = (mouse_x - start_x) // square_size;row = (mouse_y - start_y) // square_size
                handleClick(row, col)

    if not game_over:#Timer Update
        if turn == "white":white_time -= pygame.time.get_ticks() - start_time
        else:black_time -= pygame.time.get_ticks() - start_time;start_time = pygame.time.get_ticks()
        #checking the white and black piece Game Over time
        if white_time <=0 :game_over = True;winner = "black"
        elif black_time <= 0:game_over = True;winner = "white"
    screen.fill(bgColor);draw_board();pygame.display.update()#drawing and displayin the upadted screen
