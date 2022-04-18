#chessValidator
"""
Validotr for chess board: 
A valid board will have exactly one black king and exactly one white king. 
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; 
that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, 
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
This function should detect when a bug has resulted in an improper chess board.

Problems: 
- how to check that key is from 1a, 2b, ... 7h, 8h ? or 8x8 matrix 
    Got it, simple but should work

"""
validChessBoard = False
board_points = []
for i in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    for n in range(1,9):
        board_points.append(i+str(n))

def validateChessBoard(board):
    for space, v in board:
        
        if space not in board_points:
            print("Invalid space for ")

        if (1,2,3,4,5,6,7,8) or ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  not in k:
            print("Sorry but it seems your chessboard is out of bounds.")




def validatePlayer(playerBoard):
    pawn, king, bish, rook, queen, knight = 0, 0, 0, 0, 0, 0
    

    for k, v in board.items():
        for n,l in k:
            if 
        if k not in 