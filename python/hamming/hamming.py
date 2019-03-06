def distance(strand_a, strand_b):

    if strand_a is None  or strand_b is None:
        raise ValueError("Not valid strands")
    
    if len(strand_a) != len(strand_b):
        raise ValueError("length of strands do not match")
    
    return len([i for i,j in zip(strand_a,strand_b) if i !=j])