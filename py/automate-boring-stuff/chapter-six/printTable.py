tableData = [['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
['Alicja', 'Bartek', 'Celina', 'Dawid'],
['psy', 'koty', 'łosie', 'gęsi', 'sraka']]


def getColWidths(tableData):
    colWidths = [0] * len(tableData)
    for y in range(len(tableData)):
        for x in range(len(tableData[y])):
            if len(tableData[y][x]) > colWidths[y]:
                colWidths[y] = len(tableData[y][x])
    return max(colWidths)


def printTable(tableData, col):
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(col), end='')
        print()
        


printTable(tableData, getColWidths(tableData))
