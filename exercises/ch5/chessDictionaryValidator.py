def generateBoard():
    letterCoordinates = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    board = {}

    for i in range(1, 9):
        for l in letterCoordinates:
            board[str(i) + l] = ' '

    return board

chessBoard = generateBoard()
chessPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king'] # list of valid chess pieces

def isValidChessBoard(board):
    # Dictionary storing the total pieces for each player and total pawn pieces
    totalPieces = {'wTotalPieces': 0, 'bTotalPieces': 0, 'wPawns': 0, 'bPawns': 0}
    wKing = False
    bKing = False

    for pos, piece in board.items():
        if pos not in chessBoard: # Check if the key (position) is a valid key in the defined chessboard
            return 'Key ' + pos + ' is invalid. Keys must be a valid space between "1a" to "8h".'
        
        if piece[1:] not in chessPieces: # Check the names of the pieces
            return 'Pieces should be one of "pawn", "knight", "bishop", "rook", "queen", "king"'

        # check if the pieces are prefixed with 'w' or 'b'
        if piece[0] == 'w':
            totalPieces['wTotalPieces'] += 1
        elif piece[0] == 'b': 
            totalPieces['bTotalPieces'] += 1
        else: 
            return 'Pieces should be prefixed with colour keys "w" for white or "b" for black.'
        
        # Check for the black and white king
        if piece == 'wking':
            wKing = True
        elif piece == 'bking':
            bKing = True

        # Check for pawn pieces
        if piece == 'wpawn':
            totalPieces['wPawns'] += 1
        elif piece == 'bpawn':
            totalPieces['bPawns'] += 1

    # Check if both Kings are present
    if (wKing == False or bKing == False):
        return 'A valid board must have both a white king and a black king.'

    # Check if total # of pieces exceeded
    if totalPieces['bTotalPieces'] > 16 or totalPieces['wTotalPieces'] > 16:
        return 'Invalid board. Max total pieces per player is 16.'

    # Check if total # of pawn exceeded
    if totalPieces['wPawns'] > 8 or totalPieces['bPawns'] > 8:
        return 'Invalid board. Max total pawns per player is 8.'

    return 'Valid board.'

input = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(input))




