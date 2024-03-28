class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])  
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:  
                merged[-1][1] = max(merged[-1][1], interval[1])  
            else:
                merged.append(interval) 
        
        return merged
