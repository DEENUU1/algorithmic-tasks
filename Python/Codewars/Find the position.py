import string 

def position(alphabet):
    alpha = list(string.ascii_lowercase)
    check_index = alpha.index(alphabet) + 1
    return f"Position of alphabet: {check_index}"