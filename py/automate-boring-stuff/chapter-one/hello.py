# Ten program wyświetla powitanie i prosi o podanie imienia.

print('Witaj, Świecie!')
print('Jak masz na imię?')
myName = input()
print('Miło Cię poznać, ' + myName + '.')
print('Liczba znaków w Twoim imieniu wynosi:')
print(len(myName))
print('Ile masz lat?')
myAge = input()
print('Za rok będziesz mieć ' + str(int(myAge) + 1) + ' lat.')
