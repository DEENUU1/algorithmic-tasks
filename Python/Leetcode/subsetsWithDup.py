class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        result = []
        seen = set()  
        def backtrack(start: int, path: List[int]):
            path_tuple = tuple(path)
            if path_tuple not in seen: 
                seen.add(path_tuple)
                result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
