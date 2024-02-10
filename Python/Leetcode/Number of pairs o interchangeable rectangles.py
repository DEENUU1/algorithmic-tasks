class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratio_count = {}
        total = 0

        for w, h in rectangles:
            ratio = w / h
            if ratio in ratio_count:
                total += ratio_count[ratio]
                ratio_count[ratio] += 1
            else:
                ratio_count[ratio] = 1
        
        return total
