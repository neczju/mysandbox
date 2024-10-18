import sys
import pyperclip

print('num: ', end='')
number = input()

if number == 'paste':
    number = pyperclip.paste()

fib = [1, 1]
for i in range(100):
    fib.append(fib[i] + fib[i + 1])

try:
    if int(number) in fib:
        print('number %s is fibonnaci number' % number)
    else:
        print('number %s is not fibonnaci number' % number)
except ValueError:
    print('type number!')
    sys.exit()