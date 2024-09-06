def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

collatz_result = 0
while(collatz_result != 1):
    print('Podaj liczbe całkowitą: ')
    try:
        num = int(input())
        collatz_result = collatz(num)
        print(collatz_result)
    except ValueError:
        print('Błąd! Podaj liczbę całkowitą.')

