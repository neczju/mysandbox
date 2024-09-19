# Zmiana tekstu w języku angielskim na świńską łacinę
print('Podaj tekst w języku angielskim, który będzie zmieniony na świńską łacinę:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # List słów zapisanych w świńskiej łacinie
for word in message.split():
    # Usunięcie znaków innych niż litery znajdujących się na początku danego słowa.
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Usunięcie znaków innych niż litery znajdujące się na końcu danego słowa
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Zchowanie informacji, jeśli słowo było zapisane wielkimi literami lub w stylu tytułu
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Zmiana liter słowa na małe, które są używane podczas konwersji.

    # Usunięcie spółgłosek znajdujących się na początku słowa.
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Dodanie przyrostka tworzącego słowo w świńskiej łacinie.
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Przywrócenie pierwotnej wielkości liter słowa.
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Przywrócenie znaków innych niż litery na początku i na końcu słowa.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Połączenie wszystkich słów z powrotem na postać pojedynczego ciągu tekstowego.
print(' '.join(pigLatin))
