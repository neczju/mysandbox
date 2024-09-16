def validNotationGenerator():
    validNotation = []
    for x in range(9):
        for y in 'abcdefgh':
            validNotation.append(str(x + 1) + y)
    return tuple(validNotation)


def validChessBoardGenerator():
    validChessBoard = {}
    figureName = ('king', 'queen', 'knight', 'bishop', 'rook', 'pawn')
    figurePrefix = ('w', 'b')
    for p in figurePrefix:
        for n in figureName:
            if n == 'king':
                validChessBoard.setdefault(p + n, 1)
            elif n == 'queen':
                validChessBoard.setdefault(p + n, 1)
            elif n in ['knight', 'bishop', 'rook']:
                validChessBoard.setdefault(p + n, 2)
            elif n == 'pawn':
                validChessBoard.setdefault(p + n, 8)
    validChessBoard.setdefault('', 64)
    return validChessBoard


def isValidChessBoard(validBoard, board):
    validNotation = validNotationGenerator()
    for notation, figure in board.items():
        # notation check
        if notation not in validNotation:
            print('There is no ' + notation + ' position on the chessboard.')
            return False
        # piece name check
        elif figure not in validBoard.keys():
            print('There is no ' + figure + ' piece in chess.')
            return False

        # checking if amount of figure on board is greater than validAmount
        amount = 0
        for currentFigure in board.values():
            if currentFigure == figure:
                amount += 1
        for validFigure, validAmount in validBoard.items():
            if figure == validFigure and amount > validAmount:
                print('Too many ' + figure +
                      ' pieces on the chessboard, amount '
                      + str(amount) + ' expected ' + str(validAmount) + '.')
                return False

    return True


testBoard = {'1a': 'bking', '2a': 'bqueen', '3a': 'brook', '4a': 'brook',
             '5a': 'bknight', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
             '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn',
             '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn',
             '1c': 'wking', '2c': 'wqueen', '3c': 'wrook', '4c': 'wrook',
             '5c': 'wbishop', '6c': 'wbishop', '7c': 'wknight', '8c': 'wknight',
             '1e': 'wpawn', '2e': 'wpawn', '3e': 'wpawn', '4e': 'wpawn',
             '5e': 'wpawn', '6e': 'wpawn', '7e': 'wpawn', '8e': 'wpawn',
             '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '',
             '7f': '', '8f': '', '1g': '', '2g': '', '3g': '', '4g': '',
             '5g': '', '6g': '', '7g': '', '8g': '', '1h': '', '2h': '',
             '3h': '', '4h': '', '5h': '', '6h': '', '7h': '', '8h': ''}
print(isValidChessBoard(validChessBoardGenerator(), testBoard))
