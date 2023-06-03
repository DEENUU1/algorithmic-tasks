class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op == "+":
                res.append(res[-1] + res[-2])
            elif op == "C":
                res.pop()
            elif op == "D":
                res.append(2 * res[-1])
            else:
                res.append(int(op))
        
        return sum(res)