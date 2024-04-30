class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False] * len(points)
        min_cost = [float('inf')] * len(points)
        min_cost[0] = 0
        total_cost = 0

        for _ in range(len(points)):
            u = -1
            for i in range(len(points)):
                if not visited[i] and (u == -1 or min_cost[i] < min_cost[u]):
                    u = i
            
            visited[u] = True
            total_cost += min_cost[u]

            for v in range(len(points)):
                if not visited[v]:
                    cost = self.calculate(points[u], points[v])
                    min_cost[v] = min(min_cost[v], cost)

        return total_cost

    @staticmethod
    def calculate(l1: List[int], l2: List[int]) -> int:
        return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])
