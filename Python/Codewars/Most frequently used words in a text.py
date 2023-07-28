import re
from collections import Counter

alphabet_lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]


def top_3_words(text):
    text = re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))
    c = Counter(text)
    return [w for w, _ in c.most_common(3)]