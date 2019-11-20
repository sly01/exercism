import string
from collections import Counter


def count_words(sentence):
    normalized_sentence = sentence.lower()

    for punc in string.punctuation.replace("'", "") + string.whitespace:
        normalized_sentence = normalized_sentence.replace(punc, " ")
    words = []
    for word in normalized_sentence.split():
        words.append(word.strip("'"))
    return dict(Counter(words))