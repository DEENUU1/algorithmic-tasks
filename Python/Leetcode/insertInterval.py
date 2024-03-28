class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)

        intervals.sort(key=lambda x: x[0])  
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:  
                merged[-1][1] = max(merged[-1][1], interval[1])  
            else:
                merged.append(interval) 
        
        return merged
