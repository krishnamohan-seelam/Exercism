def to_rna(dna_strand):
    VALID_DNA_CHARS ='GCTA'
    if dna_strand is None:
        raise ValueError("None is passed for dna_strand")

    if not all(el in VALID_DNA_CHARS for el in dna_strand):
        raise ValueError("Invalid DNA sequence")

    return dna_strand.upper().translate(str.maketrans(VALID_DNA_CHARS,'CGAU'))
   
