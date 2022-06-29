import json
from difflib import get_close_matches
data = json.load(open('files/data.json'))


def getKey(keyword):
    if keyword in data.keys():
        outsring = '\n'.join(data[keyword])
        return outsring
    else:
        return 'There is no "%s" in the dictionary! Enter another one:' % keyword


def getLower(keyword):
    if keyword in data:
        return keyword
    elif keyword.islower():
        keyword2 = keyword.title()
        if keyword2 in data:
            return keyword2
        else:
            return keyword
    else:
        keyword3 = keyword.lower()
        if keyword3 not in data:
            return keyword
        if keyword3 in data:
            return keyword3


def wordSpelling (word):
    word2 = getLower(word)
    if word2 in data:
        return True, word2, word
    elif len(get_close_matches(word2, data.keys())) > 0:
        return False, get_close_matches(word2, data.keys())[0], word
    else:
        return True, word2, word