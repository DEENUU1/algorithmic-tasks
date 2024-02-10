
# Solution 1 - correct
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res
        
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        
        if p_count == s_count:
            res.append(0)
        
        for i in range(len(p), len(s)):
            s_count[s[i]] += 1
            s_count[s[i - len(p)]] -= 1
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]
            if p_count == s_count:
                res.append(i - len(p) + 1)
        
        return res

# Solution 2 - time limit 

import itertools

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) <= len(p):
            return res
        anagrams = self.get_anagrams(p)
        for i in range(len(s) - len(p) + 1):
            window = s[i:i+len(p)]
            if window in anagrams:
                res.append(i)
        
        return res

    def get_anagrams(self, p: str) -> List[str]:
        return ["".join(perm) for perm in itertools.permutations(p)]
