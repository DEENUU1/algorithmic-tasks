class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price

            result = max(result, price - lowest)
        return result 
            


# Solution 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]

        return result
