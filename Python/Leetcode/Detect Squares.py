class DetectSquares:

    def __init__(self):
        self.count_points = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.count_points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != (abs(px - x)) or x == px or y == py):
                continue
            res += self.count_points[(x, py)] * self.count_points[(px, y)]
        return res

    # Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)