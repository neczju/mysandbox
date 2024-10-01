import re


def is_strong_password(password):
    is_lowercase = re.compile(r'[a-z]+')
    is_uppercase = re.compile(r'[A-Z]+')
    is_number = re.compile(r'[0-9]+')
    if len(password) < 8:
        return False
    elif not is_lowercase.search(password):
        return False
    elif not is_uppercase.search(password):
        return False
    elif not is_number.search(password):
        return False
    else:
        return True


print('Wprowadź hasło: ', end='')
password = input()

if is_strong_password(password):
    print('Hasło jest silne!')
else:
    print('Hasło jest słabe!')
