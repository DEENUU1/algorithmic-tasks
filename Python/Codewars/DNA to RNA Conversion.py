def dna_to_rna(dna):
    rna = ""
    for char in dna:
        if char == "T":
            rna += "U"
        if char == "G" or char == "C" or char == "A":
            rna += char

    return rna