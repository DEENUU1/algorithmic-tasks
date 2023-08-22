from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = Counter(nums)

        mc = c.most_common(k)

        res = []
        for i in mc:
            res.append(i[0])
        
        return res 