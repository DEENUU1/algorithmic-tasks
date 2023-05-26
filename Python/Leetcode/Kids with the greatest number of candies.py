class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        for num in candies:
            if num + extraCandies >= max(candies):
                lst.append(True)
            if num + extraCandies < max(candies):
                lst.append(False)

        return lst