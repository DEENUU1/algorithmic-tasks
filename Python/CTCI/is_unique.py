
#  Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #7 7 7, #732


# Solution 1
def is_unique(text: str) -> bool:
    return len(set(text)) == len(text)


# Solution 2
# def is_unique(text: str) -> bool:
#     lst = []
#     for w in text:
#         if w not in lst:
#             lst.append(w)
#         else:
#             return False
#     return True


print(is_unique("blalalslsdllasld dlaladsllads"))
print(is_unique("kot"))