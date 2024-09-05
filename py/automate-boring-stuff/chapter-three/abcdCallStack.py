def a():
    print('Rozpoczęcie wykonywania funkcji a()')
    b()
    d()
    print('Zakończenie wykonwyania funkcji a()')

def b():
    print('Rozpoczęcie wykonywania funckji b()')
    c()
    print('Zakończenie wykonywania funkcji b()')

def c():
    print('Rozpoczęcie wykonywania funkcji c()')
    print('Zakończenie wykonywania funkcji c()')

def d():
    print('Rozpoczęcie wykonywania funckji d()')
    print('Zakończenie wykonwyania funkcji d()')

a()
