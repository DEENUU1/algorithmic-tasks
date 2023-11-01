class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited, res = set(), set()

        for i in range(len(s) - 9):
            cur = s[i:i + 10]
            if cur in visited:
                res.add(cur)
            visited.add(cur)

        return res