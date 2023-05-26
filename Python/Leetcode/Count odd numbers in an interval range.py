class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2

        if low % 2 != 0 or high % 2 != 0:
            count += 1

        return count


# That was my first solution but it got error - Memory Limit 

# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         nums = list(range(low, high + 1))

#         count = 0
#         for i in nums:
#             if i % 2 != 0:
#                 count += 1

#         return count