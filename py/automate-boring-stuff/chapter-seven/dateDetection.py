import re
import sys

date = '29/02/2024'
day, month, year = date.split('/')
leap_year = False

year = int(year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    leap_year = True

if month in ['04', '06', '09', '11'] and day > '30':
    sys.exit()
if leap_year and month in '02' and day > '29':
    sys.exit()
elif not leap_year and month in '02' and day > '28':
    sys.exit()

dateRegex = re.compile(r'''^(
(0[1-9]|1[0-9]|2[0-9]|3[0-1])       # Dzień
/                                   # Separator
(0[1-9]|1[0-2])                     # Miesiąc
/                                   # Separator
(1[0-9]{3}|2[0-9]{3})               # Rok
)$''', re.VERBOSE)

mo = dateRegex.search(date)
if mo:
    print(mo.group())
else:
    print('Niepoprawna data!')

