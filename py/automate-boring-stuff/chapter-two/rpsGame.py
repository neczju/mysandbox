import random
import sys

print('KAMIEŃ, PAPIER, NOŻYCE')

# Te zmienne przechowują informacje o liczbie zwycięstw, porażek i remisów.
wins = 0
losses = 0
ties = 0

while True:  # Pętla główna gry
    print('%s zwycięstw, %s porażek, %s remisów' % (wins, losses, ties))
    while True:  # Pętla danych wejściowych gracza.
        print('Podaj swój wybór: (k)amień, (p)apier, (n)ożyce lub (w)yjście')
        playerMove = input()
        if playerMove == 'w':
            sys.exit()  # Zakończenie działania programu.
        elif playerMove == 'k' or playerMove == 'p' or playerMove == 'n':
            break  # Opuszczenie pętli danych wejściowych gracza.
        print('Wpisz literę k, p, n lub w.')

    # Wyświetlenie wyboru dokonanego przez gracza.
    if playerMove == 'k':
        print('KAMIEŃ kontra...')
    elif playerMove == 'p':
        print('PAPIER kontra...')
    elif playerMove == 'n':
        print('NOŻYCE kontra...')

    # Wyświetlenie wyboru dokonanego przez komputer.
    randomNumber = random.randint(1, 3)
    computerMove = ''
    if randomNumber == 1:
        computerMove = 'k'
        print('KAMIEŃ')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPIER')
    elif randomNumber == 3:
        computerMove = 'n'
        print('NOŻYCE')

    # Wyświetlenie i zarejestrowanie stanu gry.
    if playerMove == computerMove:
        print('Mamy remis!')
        ties = ties + 1
    elif playerMove == 'k' and computerMove == 'n':
        print('Wygrałeś!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'k':
        print('Wygrałeś!')
        wins = wins + 1
    elif playerMove == 'n' and computerMove == 'p':
        print('Wygrałeś!')
        wins = wins + 1
    elif playerMove == 'k' and computerMove == 'p':
        print('Przegrałeś')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'n':
        print('Przegrałeś')
        losses = losses + 1
    elif playerMove == 'n' and computerMove == 'k':
        print('Przegrałeś')
        losses = losses + 1
