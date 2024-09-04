# To jest gra typ "odgadnij liczbę"
import random

secrectNumber = random.randint(1, 20)

print('Mam na myśli pewną liczbę z zakresu od 1 do 20')

# Sześciokrotnie prosimy gracza o odgadnięcie liczby
for guessesTaken in range(1, 7):
    print('Spróbuj odgadnąć liczbę.')
    guess = int(input())

    if guess < secrectNumber:
        print('Podana liczba jest za mała.')
    elif guess > secrectNumber:
        print('Podana liczba jest za duża.')
    else:
        break

if guess == secrectNumber:
    print('Doskonale! Odgadłeś liczbę w ciągu ' + str(guessesTaken) + ' prób!')
else:
    print('Nie udało się. Liczba, którą miałem na myśli to ' + str(secrectNumber))
