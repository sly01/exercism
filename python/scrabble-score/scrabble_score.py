def score(word):
    score_list = {1: "AEIOULNRST" , 2: "DG" ,3: "BCMP", 4: "FHVWY" ,5: "K" , 8: "JX" ,10: "QZ"}
    values = list(score_list.values())
    keys = list(score_list.keys())
    index_table = []
    count = 0
    for w in word.upper():
        for v in values:
            if w in v:
                index_table.append(values.index(v))
    for i in index_table:
        count += int(keys[i])
    return count
