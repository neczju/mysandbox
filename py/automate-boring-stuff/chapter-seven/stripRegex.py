import re


def stripRegex(text, char=None):
    if char is None:
        spaceStart = re.compile(r'^(\s)+')
        spaceEnd = re.compile(r'(\s)+$')
        completeText = spaceStart.sub('', text)
        completeText = spaceEnd.sub('', completeText)
        return completeText
    else:
        charStart = re.compile(r'^(%s)+' % char)
        charEnd = re.compile(r'(%s)+$' % char)
        completeText = charStart.sub('', text)
        completeText = charEnd.sub('', completeText)
        return completeText


test = 'xxxxxxxfasfaaxxxxx'
print(stripRegex(test, 'x'))
