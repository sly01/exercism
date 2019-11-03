def is_isogram(string):
    text = string.lower()
    character_map = []
    for word in text:
        if word.isalpha():
            character_map.append(word)
        if character_map.count(word) > 1:
            return False
    return True
    
