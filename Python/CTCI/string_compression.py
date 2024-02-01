# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints:#92, #110


def compress(text: str) -> str:

    res = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            res.append(text[i - 1] + str(count))
            count = 1

    res.append(text[-1] + str(count))
    return "".join(res)

print(compress("aaabbbbbddddsdjjdjdddss"))