import re

def isPhoneNumber(text):
    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumberRegex.findall(text)
    return mo

message = 'Zadzwoń pod numer 415-555-1011 po przerwie. 415-555-9999 to moje biuro.'
numbers = isPhoneNumber(message)
for i in range(len(numbers)):
    print('Znaleziono numer telefonu: ' + numbers[i])
print('Gotowe')
