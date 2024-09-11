import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    headstailsList = []
    for i in range(100):
        if random.randint(0, 1):
            headstailsList.append('O')
        else:
            headstailsList.append('R')

    streakO = 0
    streakR = 0
    for y in range(0, len(headstailsList) - 1):

        if 'O' == headstailsList[y]:
            streakO += 1
            streakR = 0
        elif 'R' == headstailsList[y]:
            streakR += 1
            streakO = 0

        if streakO == 6:
            numberOfStreaks += 1
            break
        elif streakR == 6:
            numberOfStreaks += 1
            break

print('Prawdopodobieństwo wystąpienia serii: ' + str(numberOfStreaks / 100))
