def score(word):
    score_list = {"AEIOULNRST":1 ,"DG":2 ,"BCMP":3 ,"FHVWY":4 ,"K":5 ,"JX":8 ,"QZ":10}
    return sum([score_list[key] for w in word.upper() for key in score_list.keys() if w in key])