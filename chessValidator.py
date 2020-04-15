boardPositions = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '10w': 'wking', '4L': 'wknight'}

def isValidChessBoard(board):

    # Check for valid space placement
    for key in board.keys():
        validSpace = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
                      '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h'
                      '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
                      '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
                      '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
                      '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
                      '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
                      '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h',]

        if key in validSpace:
            print(key + ' is valid.')
        else:
            print(key + ' is invalid.')

    

    # Check for 1 black and white king
    wKingCount = 0
    bKingCount = 0
    bCount     = 0
    wCount     = 0

    for value in board.values():
        if value == 'bking':
            bKingCount = bKingCount + 1
            print('There are ' + str(bKingCount) + ' black kings.')
        elif value == 'wking':
            wKingCount = wKingCount + 1
            print('There are ' + str(wKingCount) + ' white kings.')

    # Count for at most 16 pieces
    
    for character in board.values():
        if character[0] == 'b':
            bCount = bCount + 1
            print('There are ' + str(bCount) + ' black pieces.')
        if character[0] == 'w':
            wCount = wCount + 1
            print('There are ' + str(wCount) + ' white pieces.')

isValidChessBoard(boardPositions)