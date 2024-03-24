class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.get_euclidean_result(point[0], point[1], 0, 0), point) for point in points]
        
        distances.sort()
        
        return [point for _, point in distances[:k]]
    
    @staticmethod
    def get_euclidean_result(x1: int, y1: int, x2: int, y2: int) -> float:
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
