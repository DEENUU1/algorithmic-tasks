class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengt of the two  strings are not equal, they cannot be anagrams
        if len(s) != len(t): 
            return False

        # Then we check if both strings have the same characters
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT