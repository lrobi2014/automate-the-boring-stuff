import copy

def comma(ls):
    if (ls == []):
        return 'List should not be empty'

    lsStr = '';
    for i in range(len(ls)):
        if (i == (len(ls) - 1)):
            lsStr += 'and ' + ls[i]
            return lsStr

        lsStr += ls[i] + ', '
    return lsStr

spam = ['apples', 'bananas', 'tofu', 'cats']
emp = []

print(comma(spam))
