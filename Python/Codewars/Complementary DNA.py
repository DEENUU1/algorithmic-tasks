def DNA_strand(dna):
    new_char = ""
    for char in dna:
        if char == "A":
            new_char += "T"
        if char == "T":
            new_char += "A"
        if char == "G":
            new_char += "C"
        if char == "C":
            new_char += "G"
    return new_char