name = ''
while not name:
    print('Podaj swoje imię:')
    name = input()
print('Ilu gości się spodziewasz?')
numOfGuests = int(input())
if numOfGuests:
    print('Upewni się, że przygotowane zostały miejsca dla wszystkich gości.')
print('Gotowe!')
