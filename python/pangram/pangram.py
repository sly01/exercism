import string

def is_pangram(sentence):
    result = "".join([s for s in set(sentence.lower()) if s.isalpha()])
    return set(string.ascii_lowercase).issubset(result)