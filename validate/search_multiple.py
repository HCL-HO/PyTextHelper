from common import *

context = get_text_from_file('context.txt')
keywords = get_text_from_file('keywords.txt')

count = {}


def trim(word):
    return word.replace('\n', '').rstrip().lstrip()


def search():
    for keyword in keywords:
        count[trim(keyword)] = 0

    for line in context:
        for keyword in keywords:
            if trim(keyword) in line:
                count[trim(keyword)] += 1

    print(count)


search()
