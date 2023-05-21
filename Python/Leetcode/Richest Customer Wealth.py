class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for account in accounts:
            res.append(sum(account))

        return max(res)