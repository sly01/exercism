import re

def abbreviate(words):
    letters = re.findall(r"[\s_-]([A-Za-z])", words)
    acronym = words[0]
    for i in letters:
        acronym = acronym + i.upper()

    return acronym