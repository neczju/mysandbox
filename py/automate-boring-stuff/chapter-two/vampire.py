name = 'Celina'
age = 3000
if name == 'Alicja':
    print('Cześć, Alicja.')
elif age < 12:
    print('Nie jesteś Alicją, dzieciaku.')
elif age > 2000:
    print('W przeciwieństiwe do Ciebie, Alicja nie jest nieśmiertlenym wampirem.') # to sie wykona
elif age > 100:
    print('Nie jesteś Alicją, dziadku.') # to sie nie wykona bo poprzedni elif został wykonany
