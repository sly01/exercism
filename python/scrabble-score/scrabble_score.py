def score(word):
    score_list = {"AEIOULNRST":1 ,"DG":2 ,"BCMP":3 ,"FHVWY":4 ,"K":5 ,"JX":8 ,"QZ":10}
    keys = list(score_list.keys())
    count = 0
    for w in word.upper():
        for key in keys:
            if w in key:
                count += score_list[key] 
    return count
