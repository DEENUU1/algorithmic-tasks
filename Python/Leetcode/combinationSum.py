class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort(reverse=True)

        results, current_result = [], []

        def dfs(target: int, start_index: int = 0):
            if target == 0:
                results.append(current_result[:])
                return
            if target <= 0:
                return
            
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                if candidate <= target:
                    current_result.append(candidate)
                    dfs(target - candidate, i)
                    current_result.pop()

        dfs(target)
        return results
