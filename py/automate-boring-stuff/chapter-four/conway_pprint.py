import random, pprint

WIDTH = 60
HEIGHT = 20

nextCells = []
for x in range(WIDTH):  # Tworzy 60 list zawierających 20 różnych kombinacji komórek
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)

pprint.pp(nextCells, width=WIDTH*2, compact=True)
