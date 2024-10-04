import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('Suma cyfr nie może przekroczyć 10, tutaj wynosi %s' %
            (sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addsUpToTen)
print(response)
