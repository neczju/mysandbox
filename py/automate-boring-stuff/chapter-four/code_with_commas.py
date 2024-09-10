import copy

def to_commas(temp_list):
    temp_list.insert(-1, 'i') # dodaje i przed ostatnią wartością
    str_output = ''
    white_space = False

    for i in range(len(temp_list)):
        if i == (len(temp_list) - 3) or white_space:
            str_output += temp_list[i] + ' '
            white_space = True
        else:
            str_output += temp_list[i] + ', '
    return str_output


spam = ['jabłka', 'banany', 'tofu', 'koty']

print(to_commas(copy.copy(spam)))
