import re
from collections import Counter


def top_3_words(text):
    text = re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))
    c = Counter(text)
    return [w for w, _ in c.most_common(3)]