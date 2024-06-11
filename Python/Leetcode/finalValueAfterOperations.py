class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0

        for operation in operations:
            if "+" in operation:
                res += 1
            if "-" in operation:
                res -= 1
        
        return res
