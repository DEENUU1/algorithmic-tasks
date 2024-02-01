# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


def check(text1: str, text2: str) -> bool:
    n1 = len(text1)
    n2 = len(text2)

    if n1 != n2:
        return False

    text1_sorted, text2_sorted = sorted(text1), sorted(text2)
    str1, str2 = " ".join(text1_sorted), " ".join(text2_sorted)

    for i in range(0, n1, 1):
        if str1[i] != str2[i]:
            return False
    return True


print(check("test", "ttew"))
print(check("kot", "tok"))
