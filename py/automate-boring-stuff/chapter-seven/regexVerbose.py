import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Numer kierunkowy
    (\s|-|\.)?          # Separator
    \d{3}               # Pierwsze trzy cyfry
    (\s|-|\.)           # Separator
    \d{4}               # Ostatnie cztery cyfry
    (\s*(ext|x|ext.)\s*\d{2,5})?    # Numer wewnętrzny
    )''', re.VERBOSE)
