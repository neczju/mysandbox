def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

result = 0
while(result != 1):
    print('Podaj liczbe całkowitą: ')
    try:
        num = int(input())
        result = collatz(num)
        print(result)
    except ValueError:
        print('Błąd! Podaj liczbę całkowitą.')

