from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bankSet = set(bank)
        options = ["A", "C", "G", "T"]

        queue = deque()
        queue.append(startGene)

        visited = set()
        visited.add(startGene)

        res = 0

        while queue:
            size = len(queue)
            for i in range(size):
                gene = queue.popleft()
                if gene == endGene:
                    return res
                for j in range(8):
                    for option in options:
                        newGene = gene[:j] + option + gene[j + 1:]
                        if newGene in bankSet and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            res += 1
        return -1