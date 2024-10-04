import pyinputplus as pyip

while True:
    promopt = 'Czy chcesz dowiedzieć się, jak zająć kogoś godzinami?\n'
    response = pyip.inputYesNo(promopt, yesVal='tak', noVal='nie')
    if response == 'nie':
        break
print('Dziękuję i życzę Ci miłego dnia.')
