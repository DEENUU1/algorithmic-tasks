
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        max_count = max(c.values())
        min_time = (max_count -1) * (n + 1) + sum(map(lambda count: count == max_count, c.values()))
        return max(min_time, len(tasks))