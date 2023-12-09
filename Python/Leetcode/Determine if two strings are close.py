class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        w1, w2 = {}, {}
        for char in word1:
            if char not in w1:
                w1[char] = 1
            else:
                w1[char] += 1

        for char in word2:
            if char not in w2:
                w2[char] = 1
            else:
                w2[char] += 1

        return set(w1.keys()) == set(w2.keys()) and sorted(w1.values()) == sorted(w2.values())