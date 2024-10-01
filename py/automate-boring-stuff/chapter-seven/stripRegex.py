import re


def stripRegex(text, letter=None):
    if letter is None:
        spaceRemove = re.compile(r'(\s+)?(.*)(\s+)?')
        return spaceRemove.search(text).group(2)
    else:
        # TODO: Tomorrow


test = ' xx fasfaa'

print(stripRegex(test))
