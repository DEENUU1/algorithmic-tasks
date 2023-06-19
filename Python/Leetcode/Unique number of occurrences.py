from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        val_lst = []
        for val in counter.values():
            if val in val_lst:
                return False
            val_lst.append(val)
        
        return True 