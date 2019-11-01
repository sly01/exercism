def distance(strand_a, strand_b):
    if len(strand_a) is not len(strand_b):
        raise ValueError("Error")
    return [ x != y for x,y in zip(strand_a, strand_b)].count(True)