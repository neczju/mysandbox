import pprint


def validPositionGenerator():
    pos = []
    for x in range(9):
        for y in 'abcdefgh':
            pos.append(str(x + 1) + y)
    return pos


def validChessBoardGenerator():
    validChessBoard = {'wking': {'amount': 1,
                                 'validPos': validPositionGenerator()},
                       'bking': {'amount': 1,
                                 'validPos': validPositionGenerator()},
                       'wqueen': {'amount': 1,
                                  'validPos': validPositionGenerator()},
                       'bqueen': {'amount': 1,
                                  'validPos': validPositionGenerator()},
                       'wknight': {'amount': 2,
                                   'validPos': validPositionGenerator()},
                       'bknight': {'amount': 2,
                                   'validPos': validPositionGenerator()},
                       'wbishop': {'amount': 2,
                                   'validPos': validPositionGenerator()},
                       'bbishop': {'amount': 2,
                                   'validPos': validPositionGenerator()},
                       'wrook': {'amount': 2,
                                 'validPos': validPositionGenerator()},
                       'brook': {'amount': 2,
                                 'validPos': validPositionGenerator()},
                       'wpawn': {'amount': 8,
                                 'validPos': validPositionGenerator()},
                       'bpawn': {'amount': 8,
                                 'validPos': validPositionGenerator()}
                       }
    return validChessBoard


def isValidChessBoard(validBoard, board):
    # TODO: this will be complicated so for tommorow
    return None

# TODO: testBoard = {}
