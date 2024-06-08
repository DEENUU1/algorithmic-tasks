class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        stack, result = [], []

        def backtrack(idx: int, target: int):
            if target == 0:
                result.append(stack[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] <= target:
                    stack.append(candidates[i])
                    backtrack(i + 1, target - candidates[i])
                    stack.pop()
                else:
                    break
        
        backtrack(0, target)
        return result
