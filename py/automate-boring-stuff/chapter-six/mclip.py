#! python3
# mclip.py - Program schowka dla wielu ciągów tekstowych.

import sys, pyperclip

TEXT = {'zgoda': 'Tak, zgadzam się. To brzmi rozsądnie.',
        'zajęty': 'Przepraszam, ale jestem zajęty. Czy mogę się tym zająć w przyszłym tygodniu?',
        'pytanie': 'Czy rozważasz dokonywanie comiesięcznych wpłat?'}

if len(sys.argv) < 2:
        print('Użycie: python mclip.py [skrót] - skopiowanie wskazanej wiadomości')
        sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Wiadomość dla skrótu ' + keyphrase + ' została skopiowana do schowka')
else:
        print('Nie istnieje wiadomość dla skrótu ' + keyphrase + '.')
