import re


def is_day_correct(date):
    day, month, year = date.split('/')
    leap_year = False
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap_year = True

    if month in ['04', '06', '09', '11'] and day > '30':
        return False
    if leap_year and month in '02' and day > '29':
        return False
    elif not leap_year and month in '02' and day > '28':
        return False
    else:
        return True


date = '29/02/2023'

dateRegex = re.compile(r'''^(
(0[1-9]|1[0-9]|2[0-9]|3[0-1])       # Dzień
/                                   # Separator
(0[1-9]|1[0-2])                     # Miesiąc
/                                   # Separator
(1[0-9]{3}|2[0-9]{3})               # Rok
)$''', re.VERBOSE)

day_correct = False
if dateRegex.search(date):
    day_correct = is_day_correct(date)

if day_correct:
    print('Wprowadzona data jest poprawna!')
else:
    print('Wprowadzona data jest nieprawidłowa!')
