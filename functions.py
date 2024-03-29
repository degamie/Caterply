def get_moves(piece_name, row, col, chessBoard, board_size, turn):
    if piece_name.endswith("pawn"):print("It's a Pawn");moves = []#pwan movement
    if piece_name.startswith("white"):#white movement
         if chessBoard[row-1][col] is None:
            #initlizaing board's row nd colm
                if row == 6:moves.append((row-1, col)); moves.append((row-2, col))#appending board's 6th row
                else:moves.append((row-1, col));moves.append(check_side_captures_for_pawn(chessBoard, row - 1, col - 1, turn));moves.append(check_side_captures_for_pawn(chessBoard, row - 1, col + 1, turn))#checking pawns capturing next move on board
        elif piece_name.startswith("black"):
            if chessBoard[row+1][col] is None:
                if row == 1:moves.append((row + 1, col));moves.append((row + 2, col))#appending to the move
                else:moves.append((row + 1, col));moves.append(check_side_captures_for_pawn(chessBoard, row + 1, col - 1, turn,));moves.append(check_side_captures_for_pawn(chessBoard, row + 1, col + 1, turn,))#checking pawns capturing next move on board and appending the next row with same col            
        return moves#printing pawns board movements

     if piece_name.endswith("knight"):#Knight's Possible moves
        print("It's a Knight")#printing Knight after its next move
        moves = []#initalizing moves list 
        #appending moves from each row nd colm
        moves.append(check_possible_move(chessBoard, row - 2, col - 1, turn));moves.append(check_possible_move(chessBoard, row - 2, col + 1, turn));moves.append(check_possible_move(chessBoard, row - 1, col - 2, turn));moves.append(check_possible_move(chessBoard, row - 1, col + 2, turn));moves.append(check_possible_move(chessBoard, row + 1, col - 2, turn));moves.append(check_possible_move(chessBoard, row + 1, col + 2, turn));moves.append(check_possible_move(chessBoard, row + 2, col - 1, turn));moves.append(check_possible_move(chessBoard, row + 2, col + 1, turn))
        return moves#printing moves
    
        if piece_name.endswith("bishop"):#Possible moves for a Bishop
        print("It's a Bishop")
        moves = []
        # Check possible moves in diagonal direction (up and down)
        for i in range(1,board_size):
            if row + i < board_size and col + i < board_size:
                if check_possible_move(chessBoard, row+i, col+i, turn):
                    if chessBoard[row+i][col+i] and not chessBoard[row+i][col+i].startswith(turn):
                        moves.append((row+i, col+i))
                        break
                    moves.append((row + i, col + i))
                else:
                    break
        for i in range(1, board_size):
            if row - i >= 0 and col - i >= 0:
                if check_possible_move(chessBoard, row-i, col-i, turn):
                    if chessBoard[row-i][col-i] and not chessBoard[row-i][col-i].startswith(turn):
                        moves.append((row-i, col-i))
                        break
                    moves.append((row - i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row+i < board_size and col - i >= 0:
                if check_possible_move(chessBoard, row+i, col-i, turn):
                    if chessBoard[row+i][col-i] and not chessBoard[row+i][col-i].startswith(turn):
                        moves.append((row+i, col-i))
                        break
                    moves.append((row + i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row-i >= 0 and col + i < board_size:
                if check_possible_move(chessBoard, row-i, col+i, turn):
                    if chessBoard[row-i][col+i] and not chessBoard[row-i][col+i].startswith(turn):
                        moves.append((row-i, col+i))
                        break
                    moves.append((row - i, col + i))
                else:
                    break
        return moves


     if piece_name.endswith("queen"):#Queen's Possible moves
        print("It's a Queen")#printing Queen
        moves = []#initializing Queen's Movement list

        for i in range(row + 1, board_size):#iterating row and colmns on board
            if check_possible_move(chessBoard, i, col, turn):#checking best possible moves
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):#beginning with board's column
                    moves.append((i, col))#appending movement's column
                    break
                moves.append((i, col))##appending movement's other column
            else:break

        for i in range(row - 1, -1, -1):#iterating to opposite row
            if check_possible_move(chessBoard, i, col, turn):#checking all possible moves
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):#begin with chessboard's column move
                    moves.append((i, col))#appending queen's movement's every colm
                    break
                moves.append((i, col))#appending queen's other movement's every colm
            else:break

         # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):#iterating next colm with its board size
            if check_possible_move(chessBoard, row, j, turn):#checking for every row in every piece's moves
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):moves.append((row, j))#appending to the board' row and col
                break
                moves.append((row, j))#board row and col
            else:break


        # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break

        for j in range(col - 1, -1, -1):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break

        # Check possible moves in diagonal direction (up and down)
        for i in range(1,board_size):
            if row + i < board_size and col + i < board_size:
                if check_possible_move(chessBoard, row+i, col+i, turn):
                    if chessBoard[row+i][col+i] and not chessBoard[row+i][col+i].startswith(turn):
                        moves.append((row+i, col+i))
                        break
                    moves.append((row + i, col + i))
                else:
                    break
        for i in range(1, board_size):
            if row - i >= 0 and col - i >= 0:
                if check_possible_move(chessBoard, row-i, col-i, turn):
                    if chessBoard[row-i][col-i] and not chessBoard[row-i][col-i].startswith(turn):
                        moves.append((row-i, col-i))
                        break
                    moves.append((row - i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row+i < board_size and col - i >= 0:
                if check_possible_move(chessBoard, row+i, col-i, turn):
                    if chessBoard[row+i][col-i] and not chessBoard[row+i][col-i].startswith(turn):
                        moves.append((row+i, col-i))
                        break
                    moves.append((row + i, col - i))
                else:
                    break
        for i in range(1, board_size):
            if row-i >= 0 and col + i < board_size:
                if check_possible_move(chessBoard, row-i, col+i, turn):
                    if chessBoard[row-i][col+i] and not chessBoard[row-i][col+i].startswith(turn):
                        moves.append((row-i, col+i))
                        break
                    moves.append((row - i, col + i))
                else:
                    break
        return moves
    
      if piece_name.endswith("king"):#Possible moves for a King
        print("It's a King")#printing King
        moves = []#Initializing Moveement List
        moves.append(check_possible_move(chessBoard, row - 1, col - 1, turn))#appending Best possible Movements for each row and column
        moves.append(check_possible_move(chessBoard, row - 1, col, turn))#appending Best possible Movements for each row
        moves.append(check_possible_move(chessBoard,row - 1, col + 1, turn))##appending Best possible Movements for next colm 
        moves.append(check_possible_move(chessBoard, row, col-1, turn))##appending Best possible Movements for prev colm
        moves.append(check_possible_move(chessBoard, row,col+1, turn))##appending Best possible Movements for next colm
        moves.append(check_possible_move(chessBoard, row + 1, col - 1, turn))##appending Best possible Movements for prev colm and next row 
        moves.append(check_possible_move(chessBoard, row + 1, col, turn))#appending Best possible Movements for next row 
        moves.append(check_possible_move(chessBoard, row + 1, col + 1, turn))#appending Best possible Movements for next row 
        return moves#printing King's Movements


     if piece_name.endswith("rook"):print("It's a Rook")#printing Rook 
        moves = []#movements List Initializing

        # Check possible moves in vertical direction (up and down)
        for i in range(row + 1, board_size):#Iterating within next move with the board size
            if check_possible_move(chessBoard, i, col, turn):#checking Rook's all possible moves 
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):moves.append((i, col))#appending  the board's next colm  
                break;moves.append((i, col))#appending the board's colm 
            else:break#to next board colm

        for i in range(row - 1, -1, -1):#iterating within board's prev row 
            if check_possible_move(chessBoard, i, col, turn):#checking rook's prev move on board's colm
                if chessBoard[i][col] and not chessBoard[i][col].startswith(turn):  moves.append((i, col))
                    break;moves.append((i, col))#appending the board's colm 
            else:break;#to next board colm


        # Check possible moves in horizontal direction (left and right)
        for j in range(col + 1, board_size):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break

        for j in range(col - 1, -1, -1):
            if check_possible_move(chessBoard, row, j, turn):
                if chessBoard[row][j] and not chessBoard[row][j].startswith(turn):
                    moves.append((row, j))
                    break
                moves.append((row, j))
            else:
                break
        return moves
    

# This function checks whether the box user clicked is empty or blocked with their own piece
def check_possible_move(chessBoard, row, col, turn):
    try:
        if chessBoard[row][col] is None or not chessBoard[row][col].startswith(turn):
            return row,col
        else:
            return False
        
    # If the index is out of range return False
    except IndexError:
        return False

# This function checks whether there are any pieces that pawns can capture
def check_side_captures_for_pawn(chessBoard, row, col, turn):
    try:
        if chessBoard[row][col] is not None and not chessBoard[row][col].startswith(turn):
            return row,col
        else:
            return False
    # If the index is out of range return False
    except IndexError:
        return False
